from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class AssemblySummary(models.Model):
    assembly_accession          = models.CharField(max_length=255)
    bioproject                  = models.CharField(max_length=255, null=True, blank=True)
    biosample                   = models.CharField(max_length=255, null=True, blank=True)
    wgs_master                  = models.CharField(max_length=255, null=True, blank=True)
    refseq_category             = models.CharField(max_length=255, null=True, blank=True)
    taxid                       = models.CharField(max_length=255, null=True, blank=True)
    species_taxid               = models.CharField(max_length=255, null=True, blank=True)
    organism_name               = models.CharField(max_length=255, null=True, blank=True)
    infraspecific_name          = models.CharField(max_length=255, null=True, blank=True)
    isolate                     = models.CharField(max_length=255, null=True, blank=True)
    version_status              = models.CharField(max_length=255, null=True, blank=True)
    assembly_level              = models.CharField(max_length=255, null=True, blank=True)
    release_type                = models.CharField(max_length=255, null=True, blank=True)
    genome_rep                  = models.CharField(max_length=255, null=True, blank=True)
    seq_rel_date                = models.CharField(max_length=255, null=True, blank=True)
    asm_name                    = models.CharField(max_length=255, null=True, blank=True)
    submitter                   = models.CharField(max_length=255, null=True, blank=True)
    gbrs_paired_asm             = models.CharField(max_length=255, null=True, blank=True)
    paired_asm_comp             = models.CharField(max_length=255, null=True, blank=True)
    ftp_path                    = models.CharField(max_length=255, null=True, blank=True)
    excluded_from_refseq        = models.CharField(max_length=255, null=True, blank=True)
    relation_to_type_material   = models.CharField(max_length=255, null=True, blank=True)
    asm_not_live_date           = models.CharField(max_length=255, null=True, blank=True)
    group                       = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = _('Assembly Summary')
        verbose_name_plural = _('Assembly Summaries')
        ordering = ['organism_name','seq_rel_date']

    def __unicode__(self):
        return '%s (%s)' % (self.organism_name,self.assembly_accession)

class Prokaryotes(models.Model):
    guide_header = ['organism_name','taxid','bioproject_accession','bioproject_id','group',
    'subgroup','size','gc','chromosome_refseq','chromosome_insdc','plasmids_refseq','plasmids_insdc','wgs','scaffolds',
    'genes','proteins','release_date','modify_date','status','center','biosample_accession','assembly_accession','reference','ftp_path','pubmed_id','strain']
    
    organism_name           = models.CharField(max_length=255)
    taxid                   = models.CharField(max_length=255, null=True, blank=True)
    bioproject_accession    = models.CharField(max_length=255, null=True, blank=True)
    bioproject_id           = models.CharField(max_length=255, null=True, blank=True)
    group                   = models.CharField(max_length=255, null=True, blank=True)
    subgroup                = models.CharField(max_length=255, null=True, blank=True)
    gc                      = models.CharField(max_length=255, null=True, blank=True)
    chromosome_refseq       = models.CharField(max_length=255, null=True, blank=True)
    chromosome_insdc        = models.CharField(max_length=255, null=True, blank=True)
    plasmids_refseq         = models.CharField(max_length=255, null=True, blank=True)
    plasmids_insdc          = models.CharField(max_length=255, null=True, blank=True)
    wgs                     = models.CharField(max_length=255, null=True, blank=True)
    scaffolds               = models.CharField(max_length=255, null=True, blank=True)
    genes                   = models.CharField(max_length=255, null=True, blank=True)
    proteins                = models.CharField(max_length=255, null=True, blank=True)
    bioproject_accession    = models.CharField(max_length=255, null=True, blank=True)
    proteins                = models.CharField(max_length=255, null=True, blank=True)
    release_date            = models.CharField(max_length=255, null=True, blank=True)
    modify_date             = models.CharField(max_length=255, null=True, blank=True)
    status                  = models.CharField(max_length=255, null=True, blank=True)
    center                  = models.CharField(max_length=255, null=True, blank=True)
    biosample_accession     = models.CharField(max_length=255, null=True, blank=True)
    assembly_accession      = models.CharField(max_length=255, null=True, blank=True)
    reference               = models.CharField(max_length=255, null=True, blank=True)
    ftp_path                = models.CharField(max_length=255, null=True, blank=True)
    pubmed_id               = models.CharField(max_length=255, null=True, blank=True)
    strain                  = models.CharField(max_length=255, null=True, blank=True)


class ANI_report_prokaryotes(models.Model):
    genbank_accession       = models.CharField(max_length=255)
    refseq_accession        = models.CharField(max_length=255, null=True, blank=True)
    taxid                   = models.CharField(max_length=255, null=True, blank=True)
    species_taxid           = models.CharField(max_length=255, null=True, blank=True)
    organism_name           = models.CharField(max_length=255, null=True, blank=True)
    species_name            = models.CharField(max_length=255, null=True, blank=True)
    assembly_name           = models.CharField(max_length=255, null=True, blank=True)
    assembly_type_category  = models.CharField(max_length=255, null=True, blank=True)
    excluded_from_refseq    = models.CharField(max_length=255, null=True, blank=True)
    declared_type_assembly  = models.CharField(max_length=255, null=True, blank=True)
    declared_type_organism_name = models.CharField(max_length=255, null=True, blank=True)
    declared_type_category  = models.CharField(max_length=255, null=True, blank=True)
    declared_type_ANI       = models.CharField(max_length=255, null=True, blank=True)
    declared_type_gcoverage = models.CharField(max_length=255, null=True, blank=True)
    declared_type_scoverage = models.CharField(max_length=255, null=True, blank=True)
    best_match_type_assembly = models.CharField(max_length=255, null=True, blank=True)
    best_match_species_taxid = models.CharField(max_length=255, null=True, blank=True)
    best_match_species_name  = models.CharField(max_length=255, null=True, blank=True)
    best_match_type_category = models.CharField(max_length=255, null=True, blank=True)
    best_match_type_ANI      = models.CharField(max_length=255, null=True, blank=True)
    best_match_type_gcoverage = models.CharField(max_length=255, null=True, blank=True)
    best_match_type_scoverage = models.CharField(max_length=255, null=True, blank=True)
    best_match_status        = models.CharField(max_length=255, null=True, blank=True)
    comment                  = models.TextField(null=True, blank=True)
    taxonomy_check_status    = models.CharField(max_length=255, null=True, blank=True)
    
'''
COLUMNS
Column  1: genbank-accession
GenBank accesssion for the query assembly.

Column  2: refseq-accession
RefSeq accession for the query assembly.

Column  3: taxid
Taxonomic identifier for the query assembly.

Column  4: species-taxid
Taxonomic identifier for the species of the query assembly. Will differ from the
taxid (column 3) if the assembly is at subspecies level or is from an older 
strain that had its own taxonomic identifier.

Column  5: organism-name
Taxonomic name of the query assembly (matches taxid, column 3).

Column  6: species-name
Species-name of the query assembly (matches species-taxid, column 4). Will 
differ from the organism-name (column 5) if the assembly is at subspecies 
level or is from an older strain that had its own taxonomic identifier.

Column  7: assembly-name
Identifier given to the query assembly (example: ASM12345v1)

Column  8: assembly-type-category
Either a category of type, if the query assembly is derived from a type strain,
or "na", if the query assembly is not derived from a type strain. The type 
categories are:
type     - the sequences in the genome assembly were derived from type 
           material
neotype  - the sequences in the genome assembly were derived from neotype 
           material
pathovar - the sequences in the genome assembly were derived from pathovar 
           material
reftype  - the sequences in the genome assembly were derived from reference 
           material where type material never was available and is not likely to
           ever be available
syntype  - the sequences in the genome assembly were derived from synonym type 
           material
suspected-type - the type is one of the types listed above but because it does 
           not match other type-strain assemblies for the same species, or 
           cannot be vetted for some other reason, it is not used to make taxid 
           changes even though it is used to generate ANI data.

Column  9: excluded-from-refseq
Reasons the query assembly was excluded from the NCBI Reference Sequence 
(RefSeq) project, including any assembly anomalies. See: 
https://www.ncbi.nlm.nih.gov/assembly/help/anomnotrefseq/
If the query assembly is deemed reliable enough to be included in RefSeq, this 
field is "na". Many, but not all, of these reasons also make an assembly 
untrustworthy as type. Any type-strain assembly that is untrustworthy as type 
will have "na" in the assembly-type-category column.
Multiple values are separated by "; ".

Column 10: declared-type-assembly
Type-strain assembly of the declared species which best matches the query 
assembly or "no-type" if there is no type-strain assembly for the declared 
species. If the query assembly is from a type-strain, either the best matching 
of the other type-strain assemblies for the species is reported, or "same" is 
reported when there is only one type-strain assembly for the species.

Column 11: declared-type-organism-name
Taxonomic name of the declared-type-assembly. This will either be the same 
species as the query assembly, or a subspecies or strain under this species.

Column 12: declared-type-category
Type-category of the declared-type-assembly, as listed under column 8. "no-type"
if there is no type-strain assembly for the declared species, or "na" if the 
query assembly is a type-strain assembly

Column 13: declared-type-ANI
The average nucleotide identity (ANI) of the query assembly to the type-strain 
assembly for the declared species of the query assembly, expressed as a 
percentage. "na" if there is no type-strain assembly for the declared species.
"na" is also reported if either the query coverage (column 14) or subject 
coverage (column 15) is less than 10%.

Column 14: declared-type-qcoverage
Coverage of the query assembly by the declared-type-assembly, expressed as a 
percentage. (Query coverage).

Column 15: declared-type-scoverage
Coverage of the declared-type-assembly by the query assembly, expressed as a 
percentage. (Subject coverage, where subject is the declared-type-assembly).

Column 16: best-match-type-assembly
The best-matching type-strain assembly as determined by ANI, or "none-found" if 
no type-strain assembly matches the query assembly.

Column 17: best-match-species-taxid
Taxonomic identifier for the species of the best-match-type-assembly (column 
16). 

Column 18: best-match-species-name
Species-name of the best-match-type-assembly (column 16).

Column 19: best-match-type-category
Type-category of the best-match-type-assembly. Values as listed for column 8.

Column 20: best-match-type-ANI
The average nucleotide identity (ANI) of the query assembly to the best-matching
type-strain assembly, expressed as a percentage.

Column 21: best-match-type-qcoverage
Coverage of the query assembly by the best-match-type-assembly, expressed as a 
percentage. (Query coverage).

Column 22: best-match-type-scoverage
Coverage of the best-match-type-assembly by the query assembly, expressed as a 
percentage. (Subject coverage, where subject is the best-match-type-assembly).

Column 23: best-match-status
Status of the best match.

Values that indicate the species declared for the query assembly is OK:
species-match
- the query assembly matches a type-strain assembly for the declared species.
subspecies-match
- the query assembly matches a type-strain assembly for the declared species and
  both are the same subspecies.
synonym-match 
- the query assembly matches a type-strain assembly for a synonym of the 
  declared species. A specialized synonymy list is used to handle difficult
  cases of typing.
derived-species-match
- the query assembly matches a type-strain assembly for a subspecies of the 
  declared species.
genus-match 
- the query assembly has an informal species name (usually "sp." format), and 
  the best-matching type-strain assembly shares the same genus.
approved-mismatch 
- the query assembly best matches a type-strain assembly from a different 
  species above ANI threshold, but the mismatch was manually reviewed and the 
  declared species was accepted.

Values that indicate the species declared for the query assembly is incorrect:
mismatch 
- the query assembly best matches a type-strain assembly from a different 
  species, above ANI threshold, even though a type-strain assembly for the 
  declared species is available. GenBank will address the mismatch when high 
  coverage values provide high confidence in the mismatch result, i.e. query 
  coverage and subject coverage are both over 80%.

Values that indicate the ANI data are inconclusive:
below-threshold-match 
- the query assembly matches a type-strain assembly for the declared species but
  the ANI is below the species ANI threshold.
below-threshold-mismatch 
- the query assembly best matches a type-strain assembly from a different 
  species but the ANI is below the species ANI threshold.
low-coverage 
- the query assembly did not match the best-matching type-strain assembly above
  10% query-coverage and/or 10% subject-coverage.

Column 24: comment
Assembly is the type-strain, no match is expected
- the assembly is the only type-strain assembly for the species, hence it is 
  expected that it may not match any other type-strain assembly.
Assembly is the type-strain, mismatch is within genus and expected
- the assembly is the only type-strain assembly for the species, hence it is 
  expected that its best match may be to a type-strain assembly from another 
  species on the same genus but with ANI below 98%.
Assembly is type-strain, failed to match other type-strains on its species
- a type-strain assembly is expected to match all other type-strain assemblies
  on the species.

Column 25: taxonomy-check-status
The best-match-status (column 23) and comment (column 24) are converted into 
three Taxonomy check statuses as follows.

OK 
- the ANI result is consistent with the declared species
  The best-match-status is species-match, subspecies-match, 
  derived-species-match, synonym-match, genus-match, approved-mismatch, or the 
  comment indicates either that the assembly is the type-strain and no match is 
  expected, or that the assembly is the type-strain, the mismatch is within 
  genus and is expected. 
Inconclusive 
- the ANI result is inconclusive
  The best-match-status is low-coverage, below-threshold-match, 
  below-threshold-mismatch, na, or the comment indicates that the assembly is a 
  type-strain that failed to match other type-strains on its species.
Failed 
- the ANI result is inconsistent with the declared species
  The best-match-status is mismatch and the comment is na.
'''