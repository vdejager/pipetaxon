from taxonomy.models import Taxonomy
from genomes.models import AssemblySummary
import networkx as nx

class TaxAssemblyInfo():

    def get_root(self,taxid):
        self.root=Taxonomy.objects.get(taxid=taxid)
        
    def tree(self):
        node = self.root
        leaves=[]
        G=nx.Graph()
        G.add_node(root.taxid)

        def buildtree(G, node):
            children = node.children()
            for c in children:
            parent = c.parent
            taxid = c.taxid
            G.add_edge(parent, taxid)
            
            if (c.children()):
                buildtree(G,c)
            else:
                is_leave=True
                leaves.append(c.taxid)
                print(c.taxid)
    return leaves
