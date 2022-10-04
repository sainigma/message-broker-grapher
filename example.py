import message_broker_grapher

# example
# duplicate signals are omitted
emitters = {
  'Class1': ['signal1', 'signal2', 'signal4', 'signal5', 'signal5', 'signal5'],
  'Class5': ['signal2', 'signal3']
}
listeners = {
  'Class2': ['signal2', 'signal4', 'signal6'],
  'Class4': ['signal3'],
  'Class5': ['signal5']
}

message_broker_grapher.draw(emitters, listeners)