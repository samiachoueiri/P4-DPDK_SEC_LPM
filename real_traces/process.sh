#!/bin/bash

# Loop to run the Zeek command 3 times
for i in 1 2 3; do
    echo "Running Zeek - iteration $i..."
    
    # Run the Zeek command
    /opt/zeek/bin/zeek -r syn_flood.pcap syn_counter.zeek

    # Copy output.log to output{i}.txt
    cp output.log output${i}.txt

    # Remove lines starting with '#'
    sed -i '/^#/d' output${i}.txt
done

# Merge all three cleaned files into one
cat output1.txt output2.txt output3.txt > day.txt

# Notify completion
echo "All done! Merged file is 'day.txt'"
