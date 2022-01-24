#!/bin/bash
cd ..
wget https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz
mkdir data && tar -zxvf new_taxdump.tar.gz -C data/
rm new_taxdump.tar.gz

python manage.py migrate
python manage.py build_database --taxonomy data/taxonomy
python manage.py build_database --lineage data/taxonomy
#rm -rf data/taxonomy

#docker build . --tag voorloop/pipetaxon:latest
#docker push voorloop/pipetaxon:latest
z
