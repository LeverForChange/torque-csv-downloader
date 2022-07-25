# -*- coding: utf-8 -*-
import pandas as pd
import json
import time

from torqueclient import Torque

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def clean_objs(key, val):
  if isinstance(val, list):
    val = ','.join(val)
  elif isinstance(val, dict):
    val = json.dumps(val)
  return key, val

def run(**kwargs):
  t0 = time.time()
  torque = Torque(
    "https://torque.leverforchange.org/GlobalView",
    kwargs['username'], kwargs['api_key']
  )

  # Get all Competition keys
  competitions = torque.competitions.keys()
  competitions = list(filter(lambda c: c not in kwargs['exclude_competitions'], competitions))
  print('Gathering from competitions:', ', '.join([c for c in competitions]))

  # determine fields to download
  fields = ['Application #', 'Competition Domain', 'Project Title', 'GlobalView MediaWiki Title']
  fields += kwargs['fields']

  df = []
  for comp in competitions:
    print(f'Downloading {comp} proposals...',)
    comp = torque.competitions[comp]
    proposals = comp.proposals
    torque.bulk_fetch(proposals)
    compFields = set(comp.fields) & set(fields)
    for proposal in proposals:
      res = {k:proposal[k] for k in compFields}
      res = dict(map(lambda x: clean_objs(x[0],x[1]), res.items()))
      df.append(res)

  df = pd.DataFrame(df)
  df.to_csv('data/lfc-proposals.csv', index=False)
  print(f'\nDownloaded {len(df)} proposals in', f'{round(time.time() - t0, 1)}s')
  print('Proposals written to data/lfc-proposals.csv')

if __name__ == '__main__':
  kwargs = json.load(open('args.json'))
  run(**kwargs)