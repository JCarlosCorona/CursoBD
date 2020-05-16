#!/bin/bash
fileid="1kgtN_ZgNGgGCaCOYy15lm-QRLrrhn0oyg_AV9AcNHV0"
filename="ProyectoEcommerce.GoogleMS.csv"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
