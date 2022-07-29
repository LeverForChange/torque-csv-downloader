import json

from torqueclient import Torque

if __name__ == '__main__':
  try:
    kwargs = json.load(open('args.local.json'))
  except:
    kwargs = json.load(open('args.json'))
    
  torque = Torque(
    "https://torque.leverforchange.org/GlobalView",
    kwargs['username'], kwargs['api_key']
  )
  
  comps = torque.competitions.keys()
  fields = []
  for comp in comps:
    fields.extend(torque.competitions[comp].fields)
  fields = sorted(list(set(fields)))
  fields = '\n'.join(fields)
  print(fields)