#!/bin/bash

echo -n '["' > stocks.json
curl -o nasdaq.txt ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqtraded.txt
cat nasdaq.txt | grep -Eo '^\w\|\w*' | sed 's/^\w|//g' | sed 'H;1h;$!d;x;y/\n/,/' | sed 's/,/\",\"/g' >> stocks.json
echo '"]' >> stocks.json
sed -i ':a;N;$!ba;s/\n//' stocks.json
rm nasdaq.txt
