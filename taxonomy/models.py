from django.db import models
from django.utils.functional import cached_property


ALL_RANKS = ['no rank', 'superkingdom', 'kingdom', 'subkingdom', 'superphylum', 'phylum', 'subphylum', 'genus',
             'subspecies', 'subtribe', 'class', 'parvorder', 'tribe', 'varietas', 'subfamily', 'suborder', 'subclass',
             'superfamily', 'order', 'infraorder', 'cohort', 'superorder', 'forma', 'superclass', 'species group',
             'species', 'infraclass', 'family', 'species subgroup', 'subgenus'
             ]


class Division(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False)
    short = models.CharField(max_length=3)
    long = models.CharField(max_length=30)

    def __str__(self):
        return self.long


class Taxonomy(models.Model):
    class Meta:
        ordering = ("taxid",)

    taxid = models.IntegerField(null=False, primary_key=True, auto_created=False)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    rank = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    updated_at = models.DateField(null=True, auto_now=True)

    def __str__(self):
        return "{0}:{1}:{2}".format(self.rank, self.taxid, self.name)

    @cached_property
    def lineage(self):
        entry = self
        lineage = [self]
        while entry.parent.taxid != 1:
            lineage.append(entry.parent)
            entry = entry.parent
        return lineage
    
    def children(self):
        children =[]
        children = Taxonomy.objects.filter(parent=self.taxid)
        return children
    
    def all_children(self, mode='nodes'):
        """
        option: mode = 'nodes' return nodes
        option: mode = 'taxids' return taxids
        
        """
        nodes = []
        taxids=[self.taxid]

        c=self
        def buildtree(c):
            children = c.children()
            for c in children:
                parent = c.parent
                taxid = c.taxid
                taxids.append(taxid)
                nodes.append(c)
                if (c.children()):
                    buildtree(c)
        buildtree(c)

        if mode=='taxids':
            return taxids
        else:
            return nodes

    def show_tree(self):
        return self.lineage

    def _check_rank(self, rank):
        for entry in self.lineage:
            if entry.rank == rank:
                return entry
        return False

    def species(self):
        return self._check_rank('species')

    def genus(self):
        return self._check_rank('genus')

    def family(self):
        return self._check_rank('fajomily')

    def order(self):
        return self._check_rank('order')

    def klass(self):
        return self._check_rank('class')

    def phylum(self):
        return self._check_rank('phylum')

    def kingdom(self):
        return self._check_rank('kingdom')

    def superkingdom(self):
        return self._check_rank('superkingdom')


    
    
class Accession(models.Model):
    accession = models.CharField(max_length=20, primary_key=True)
    taxonomy = models.IntegerField()

    def get_taxonomy_instance(self):
        try:
            return Taxonomy.objects.get(taxid=self.taxonomy)
        except Exception as err:
            return None
