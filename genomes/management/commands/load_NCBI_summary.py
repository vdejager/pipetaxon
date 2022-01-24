import sys, os, re, glob, hashlib, time, datetime, traceback
# import the logging library
# Preamble so we can use Django's DB API
#sys.path.append(os.path.dirname(__file__))

#sys.path.append('/home/vdejager/workspace/d3mgv')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings.dev'

#django imports
import shutil
import urllib
import timeit

from contextlib import closing

from django.conf import settings
from django.db import transaction
from django.db import models, transaction
from django.db.models import Count, Avg

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from genomes.models import AssemblySummary, ANI_report_prokaryotes, Prokaryotes

import logging

logger = logging.getLogger('commands')
djangologger = logging.getLogger('django')
djangologger.setLevel('INFO')

class Command(BaseCommand):
    args = 'none'
    help = 'Loads the NCBI assembly_summary data in the database'
    assembly_header = ['assembly_accession','bioproject','biosample','wgs_master',
                       'refseq_category','taxid','species_taxid','organism_name',
                       'infraspecific_name','isolate','version_status','assembly_level',
                       'release_type','genome_rep','seq_rel_date','asm_name','submitter',
                       'gbrs_paired_asm','paired_asm_comp','ftp_path','excluded_from_refseq',
                       'relation_to_type_material','asm_not_live_date']
    guide_header = ['organism_name','taxid','bioproject_accession',
                    'bioproject_id','group','subgroup','size','gc',
                    'chromosome_refseq','chromosome_insdc','plasmids_refseq',
                    'plasmids_insdc','wgs','scaffolds','genes','proteins',
                    'release_date','modify_date','status','center','biosample_accession',
                    'assembly_accession','reference','ftp_path','pubmed_id','strain']

    ANI_header = ['genbank_accession','refseq_accession','taxid',
                    'species_taxid','organism_name','assembly_name',
                    'assembly_type_category', 'excluded_from_refseq','declared_type_assembly',
                    'declared_type_organism_name', 'declared_type_category','declared_type_ANI',
                    'declared_type_gcoverage','declared_type_scoverage','best_match_type_assembly',
                    'best_match_species_taxid','best_match_species_name','best_match_type_category',
                    'best_match_type_ANI', 'best_match_type_gcoverage','best_match_type_scoverage',
                    'best_match_status','comment','taxonomy_check_status']

    def handle(self, *args, **options):
        # main entry                

        self.prokaryotes = settings.LOCAL_GENOME_REPORTS_PROKARYOTES 
        self.ani_report_prokaryotes = settings.LOCAL_ANI_REPORT_PROKARYOTES
        self.summary = settings.LOCAL_ASSEMBLY_SUMMARY
        self.guide = {}
        
        #self.read_guide()
        #self._import_assembly_summary()
        self._import_ani_report_prokaryotes()
        self._import_stats()
        
    @staticmethod
    def clear_database():
        print("Removing all assembly_summary entries...")
        AssemblySummary.objects.all().delete()
            
    def read_guide(self):
        logger.info("Reading prokaryote guide file %s"%self.prokaryotes)
        
        f = open(self.prokaryotes,'r')
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue
            
            data = line.split('\t')
            data = dict(zip(self.guide_header, data))
            
            self.guide[data['assembly_accession']] = data
        
        logger.info("Done loading guide with %s items:", len(self.guide.keys()))
    
    def _import_assembly_summary(self):
        
        logger.info("Reading summary file %s"%self.summary)

        f = open(self.summary,'r')
        counter = 0
        records = [] 
        
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue

            data = line.split('\t')
            data = dict(zip(self.assembly_header, data))
            #data['group'] = 'Bacteria'
            records.append(data)

        logger.info("Records %s"%len(records))
        
        #self._create_records(records)
        self._bulk_create_records(records)
        
    @transaction.atomic     
    def _create_records(self, records):
        start = timeit.timeit()
        logger.info("Loading data into database")
        
        AssemblySummary.objects.all().delete()
        total_records = len(records)    
        for i,data in enumerate(records):
            
            accession=data['assembly_accession'].strip()
            #logger.info(data)
            (record) = AssemblySummary.objects.create(**data)
            if (i % 1000 == 0):
                logger.info("Loaded %d of %d  records"%(i+1, total_records))
        logger.info("Loaded %d of %d  records"%(i+1, total_records))
        end = timeit.timeit()
        logger.info('time:%s'%(end - start))

    @transaction.atomic     
    def _bulk_create_records(self,records):
        start = timeit.timeit()
        logger.info("Bulk Loading assembly data into database")
        total_records = len(records)
        bulk_insert_data = []
        AssemblySummary.objects.all().delete()
        
        for i,data in enumerate(records):
            #logger.info("data %s"%data)
            bulk_insert_data.append(AssemblySummary(**data))
                
        AssemblySummary.objects.bulk_create(bulk_insert_data)
        logger.info("Loaded %d of %d  records"%(i+1, total_records))
        end = timeit.timeit()
        logger.info('time:%s'%(end - start))
    
    def _import_ani_report_prokaryotes(self):
        
        logger.info("Reading ANI report_prokaryotes file %s"%self.ani_report_prokaryotes)

        f = open(self.summary,'r')
        counter = 0
        records = [] 
        
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue

            data = line.split('\t')
            data = [d[:255] for d in data]
            data = dict(zip(self.ANI_header, data))
            records.append(data)

        logger.info("Records %s"%len(records))
        self._bulk_create_ani_records(records)
        
    @transaction.atomic     
    def _bulk_create_ani_records(self,records):
        start = timeit.timeit()
        logger.info("Bulk Loading ANI data into database")
        total_records = len(records)
        bulk_insert_data = []
        ANI_report_prokaryotes.objects.all().delete()
        
        for i,data in enumerate(records):
            #logger.info("data %s"%data)
            if (i % 10000 == 0):
                logger.info("Loaded %d of %d  records"%(i+1, total_records))
            bulk_insert_data.append(ANI_report_prokaryotes(**data))
                
        ANI_report_prokaryotes.objects.bulk_create(bulk_insert_data)
        logger.info("Loaded %d of %d  records"%(i+1, total_records))
        end = timeit.timeit()
        logger.info('time:%s'%(end - start))

    def _import_stats(self):
        
        orgs = AssemblySummary.objects.all()
        logger.info("Organisms :%s"%orgs.count())
        
        stats = orgs.order_by().values('assembly_level').distinct().annotate(count=Count('assembly_level'))
        
        for d in stats:
            logger.info("%(assembly_level)s : %(count)s"%d)
        
        
            