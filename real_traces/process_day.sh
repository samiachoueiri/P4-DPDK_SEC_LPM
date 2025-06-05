#!/bin/bash

# Set your Zeek script name
ZEEK_SCRIPT="syn_counter.zeek"
LINKS_FILE="links.txt"  # file containing the links
THREADS=8

echo ">>> Starting PCAP processing at $(date)"

# Check if axel is installed
if ! command -v axel &> /dev/null; then
    echo "Axel not found! Install it using: sudo apt install axel"
    exit 1
fi

# Process each URL
while IFS= read -r url; do
    # Extract the filename (e.g., 202406182345.pcap.gz)
    filename=$(basename "$url")
    base="${filename%.pcap.gz}"  # Remove .pcap.gz

    echo "-------------------------------"
    echo ">>> Downloading: $filename"
    axel -n $THREADS "$url" || { echo "Download failed for $url"; continue; }

    echo ">>> Unzipping: $filename"
    gunzip "$filename" || { echo "Unzip failed for $filename"; continue; }

    echo ">>> Running Zeek on: $base.pcap"
    /opt/zeek/bin/zeek -r "$base.pcap" "$ZEEK_SCRIPT" || { echo "Zeek failed for $base.pcap"; continue; }

    echo ">>> Processing output.log -> $base.txt"
    if [ -f "output.log" ]; then
        cp output.log "$base.txt"
        sed -i '/^#/d' "$base.txt"
    else
        echo "No output.log found for $base.pcap"
        continue
    fi

    echo ">>> Cleaning up temporary files..."
    rm -f "$base.pcap"
    rm -f *.log

    echo ">>> Done with: $base"
done < "$LINKS_FILE"

echo ">>> Removing first two lines.txt"
for file in 2024*.txt; do
  sed -i '1,2d' "$file"
done

# Merge all processed text files into one
echo ">>> Merging all .txt files into day.txt"
#cat *.txt > day.txt
cat 2024*.txt > day_20240619.txt

echo ">>> All done at $(date). Final output: day.txt"
