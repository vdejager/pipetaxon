import sys
import os
import re
import glob
import hashlib
import time
import datetime
import traceback
import logging
#django imports
import shutil
import urllib
from contextlib import closing

from django.conf import settings

from django.db import transaction
from django.db import models, transaction
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from Bio import SeqIO
from Bio import SeqUtils
from genomes.models import AssemblySummary
import logging

logger = logging.getLogger('commands')

class Command(BaseCommand):
    args = 'none'
    help = 'Loads and saves the NCBI assembly_summary data from the FTPsite'
    logger = logging.getLogger('django')
    def handle(self, *args, **kwargs):
        
        self.ncbi_assembly_summary_url = settings.NCBI_ASSEMBLY_SUMMARY
        self.summary = settings.LOCAL_ASSEMBLY_SUMMARY
        
        self.ncbi_prokaryotes_guide_url = settings.NCBI_GENOME_REPORTS_PROKARYOTES
        self.prokaryotes = settings.LOCAL_GENOME_REPORTS_PROKARYOTES 
        self.ncbi_ani_report_prokaryotes_url = settings.NCBI_ANI_REPORT_PROKARYOTES
        self.ani_report_prokaryotes = settings.LOCAL_ANI_REPORT_PROKARYOTES
        
        self.guide = {}
        
        self._get_ncbi_assembly_summary()
        self._get_ncbi_prokaryotes_guide()
        self._get_ncbi_ANI_report_prokaryotes()
        
        logger.info('Done!')


    def _check_dir(self,file):
        try:
            os.makedirs(os.path.dirname(file))
        except OSError as e:
            logger.info("%s already exists"%(os.path.dirname(file)))
            pass
            
    def _get_ncbi_assembly_summary(self):
        logger.info("Downloading assembly_summary file from %s to %s"%(self.ncbi_assembly_summary_url, self.summary))
        self._check_dir(self.summary)
        
        response = urllib.request.urlopen(self.ncbi_assembly_summary_url)
        
        if (os.path.exists(self.summary)):
            os.rename(self.summary, "%s.old"%(self.summary))
        
        f = open(self.summary, 'wb')
        self.chunk_read(response, f, report_hook=self.chunk_report)
        f.close()
        
        logger.info("Done downloading assembly_summary file.")
        

    def _get_ncbi_prokaryotes_guide(self):
        logger.info("Downloading prokaryotes file from %s to %s"%(self.ncbi_prokaryotes_guide_url, self.prokaryotes))
        self._check_dir(self.prokaryotes)
        
        response = urllib.request.urlopen(self.ncbi_prokaryotes_guide_url)
        if (os.path.exists(self.prokaryotes)):
        
            os.rename(self.prokaryotes, "%s.old"%(self.prokaryotes))
        f = open(self.prokaryotes, 'wb')
        self.chunk_read(response, f, report_hook=self.chunk_report)
        f.close()
        
        logger.info("Done downloading prokaryotes_guide file.")
        

    def _get_ncbi_ANI_report_prokaryotes(self):
        logger.info("Downloading prokaryotes file from %s to %s"%(self.ncbi_ani_report_prokaryotes_url, self.ani_report_prokaryotes))
        self._check_dir(self.ani_report_prokaryotes)
        
        response = urllib.request.urlopen(self.ncbi_ani_report_prokaryotes_url)
        if (os.path.exists(self.ani_report_prokaryotes)):
        
            os.rename(self.ani_report_prokaryotes, "%s.old"%(self.ani_report_prokaryotes))
        f = open(self.ani_report_prokaryotes, 'wb')
        self.chunk_read(response, f, report_hook=self.chunk_report)
        f.close()
        
        logger.info("Done downloading ani_report_prokaryotes file.")


    def chunk_report(self,bytes_so_far, chunk_size, total_size):
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))

        if bytes_so_far >= total_size:
            sys.stdout.write('\n')


    def chunk_read(self, response, filehandle, chunk_size=8192, report_hook=None):
        total_size = response.headers.get('content-length', -1)
        total_size = int(total_size)
        bytes_so_far = 0

        while 1:
            chunk = response.read(chunk_size)
            bytes_so_far += len(chunk)
            filehandle.write(chunk)

            if not chunk:
                break

            if report_hook:
                report_hook(bytes_so_far, chunk_size, total_size)
        
        return bytes_so_far
