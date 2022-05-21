import random

proxies_pool = [
  {'http': 'http://20.47.108.204:80'},
  {'http': 'http://20.47.108.204:90'},
  {'http': 'http://20.47.108.204:100'},
]

proxies = random.choice(proxies_pool)

print(proxies)