from rest_framework import serializers
from taxonomy.models import Taxonomy, Accession


class TaxonomySerializer(serializers.ModelSerializer):

    class Meta:
        model = Taxonomy
        fields = ('taxid', 'rank', 'name', 'parent', 'division')

   
class RecursiveTaxonomySerializer(TaxonomySerializer):
    def get_fields(self):
        fields = super(RecursiveTaxonomySerializer, self).get_fields()
        fields['children'] = RecursiveTaxonomySerializer(many=True)
        return fields

class RecursiveSerializer(serializers.Serializer, many=True):

    def __init__(self,*args, **kwargs):
        self.many = kwargs['many']
        
    def to_representation(self, taxonomy):
        # prevent lineage to keep iterating over taxid 1 ( because it is it own parent )
        if taxonomy.taxid == 1:
            return None
        serializer = self.parent.__class__(taxonomy, context=self.context)
        return serializer.data


class NestedTaxonomySerializer(serializers.ModelSerializer):
    parent = RecursiveSerializer(many=False)

    class Meta:
        model = Taxonomy
        fields = ('taxid', 'rank', 'name', 'division', 'parent')
    

