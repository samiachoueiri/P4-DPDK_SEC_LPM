; Define pipeline input ports
port in 0 ethdev 0000:0b:00.0 rxq 2 bsz 8
port in 1 ethdev 0000:0b:00.1 rxq 2 bsz 8

; Define pipeline output ports
port out 0 ethdev 0000:0b:00.0 txq 2 bsz 8
port out 1 ethdev 0000:0b:00.1 txq 2 bsz 8

