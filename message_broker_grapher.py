import matplotlib.pyplot as plt
import networkx as nx

def draw(emitters = {'Class1':['signal1', 'signal3']}, listeners = {'Class2':['signal1', 'signal2']}):
  G = nx.DiGraph()

  classes = {}
  has_owner = {}
  has_listener = {}

  for key in emitters.keys():
    if key not in classes:
      classes[key] = True
    
    cache = {}
    for emitter in emitters[key]:
      if emitter not in has_owner:
        has_owner[emitter] = True
      
      if emitter not in cache:
        cache[emitter] = True
        edge = [key, emitter]
        G.add_edge(*edge)

  for listener in listeners.keys():
    if listener not in classes:
      classes[key] = True
    
    cache = {}
    for emitter in listeners[listener]:
      if emitter not in classes:
        has_listener[emitter] = True

      if emitter not in cache:
        cache[emitter] = True
        edge = [emitter, listener]
        G.add_edge(*edge)

  size_map = []
  color_map = []
  for node in G:
    if node in emitters or node in listeners:
      color_map.append('darkorange')
      size_map.append(4000)
      continue
    if node in has_owner and node in has_listener:
      color_map.append('C0')
    else:
      color_map.append('lightblue')
    size_map.append(1000)

  pos = nx.circular_layout(G)
  nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=size_map)
  plt.show()