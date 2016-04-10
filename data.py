import blockchain
from blockchain import blockexplorer as explorer

from gcloud import datastore


dataset = datastore.Client(project='thedatalabproject')

# checkpoint the state
dataset = datastore.Client(project='thedatalabproject')

query = dataset.query(kind='Greeting')
for result in query.fetch():
    print(result)


entity = datastore.Entity(key=dataset.key('Greeting'))
entity['message'] = 'Hello, world!'

dataset.put(entity)

start = 1
end = 100

for height in range(start, end):
    blocks = blockexplorer.get_block_height(height)
    block = blocks[0]
    for tx in block.transactions:
        
