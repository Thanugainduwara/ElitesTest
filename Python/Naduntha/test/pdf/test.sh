#!/bin/bash

# Loop to generate 10 QR codes

for i in {1..12}
do
    python3 -m reportlab_qr_code "QR Code $i" \
        --outfile "qr_code_$i.pdf" \
        --error_correction L \
        --size 10cm \
        --padding 1cm \
        --radius 0.5 \
        --enhanced-path \
        --gradient "linear 0 1 1 0 0.1 #ff0000 0.9 #0000ff"
done

