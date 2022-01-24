import sys, os, re, hashlib, time, datetime, traceback
import subprocess, shlex, tarfile
# import the logging library
import logging
# Get an instance of a logger
# Preamble so we can use Django's DB API

#django imports
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger('commands')


class Command(BaseCommand):
    args = 'none'
    help = 'Downloads the NCBI Taxonomy data in the database'
    
    
    def handle(self, *args, **kwargs):
        logger.info("Get NCBI taxonomy")
         
        self.ncbi_taxonomy_dump = settings.NCBI_NEW_TAXONOMY_DUMP
        self.ncbi_taxonomy_dump_localpath = os.path.join(settings.LOCAL_TAXONOMY_DIR, self.ncbi_taxonomy_dump)
        self._check_dir(self.ncbi_taxonomy_dump_localpath)
        
        
        self._rsync(self.ncbi_taxonomy_dump, self.ncbi_taxonomy_dump)
        logger.info("Get NCBI taxonomy done!")
        
        self._untar(self.ncbi_taxonomy_dump_localpath, settings.LOCAL_TAXONOMY_DIR)
        logger.info("untar NCBI taxonomy done!")

         
    def _rsync(self, source, target):
        rsyncsource = "%s/%s" % (settings.NCBI_TAXONOMY_BASE, source )
        rsynctarget = "%s/%s" % (settings.LOCAL_TAXONOMY_DIR, target)
        cmd = "rsync --progress -rptgoDLK %s %s" %( rsyncsource, rsynctarget)
        logger.info("rsync command: %s" % cmd)
        cmd_args = shlex.split(cmd)
        p = subprocess.call(cmd_args)

    def _check_dir(self,file):
        logger.info(f"check: {file}")
        try:
            os.makedirs(os.path.dirname(file))
        except OSError as e:
            logger.info("%s already exists"%(os.path.dirname(file)))
            pass
    
    def _untar(self, archive_file, target_dir, delete=False):
        if not target_dir:
            target_dir, _ = os.path.split(archive_file)  # default to same directory as tar file

        if (archive_file.endswith("tar.gz")):
        
            try:
                with tarfile.open(archive_file, 'r:gz') as f:
                    f.extractall(target_dir)
                    logger.info("Extracted in directory: %s" % target_dir)
            finally:
                if delete:
                    os.remove(archive_file) 
        else:
            logger.info("Not a tarfile : %s" % archive_file)
