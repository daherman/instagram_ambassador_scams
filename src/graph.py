# %%
from pyvis.network import Network
import pandas as pd

# %%
node_df = pd.read_csv('data/node.csv')
mapping_df = pd.read_csv('data/mapping.csv')
# %%
net = Network()
# %%
net.add_nodes(node_df['node_id'].to_list(),
              label=node_df['node'].to_list())
# %%
source = mapping_df['source_id']
target = mapping_df['target_id']

edges = zip(source, target)

for e in edges:
    src = e[0]
    tgt = e[1]
    net.add_edge(src, tgt)
# %%
net.show('nodes.html')
