import json

from torqueclient import Torque

if __name__ == '__main__':
  kwargs = json.load(open('args.json'))
  torque = Torque(
    "https://torque.leverforchange.org/GlobalView",
    kwargs['username'], kwargs['api_key']
  )
  comp = torque.competitions.keys()[0]
  comp = torque.competitions[comp]
  fields = '\n'.join(comp.fields)
  print('Available Fields:')
  print(fields)