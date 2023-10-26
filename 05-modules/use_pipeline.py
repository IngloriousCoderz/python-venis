from pipeline.input.rest import fetch
from pipeline.input import rest
import pipeline.input.rest

print(pipeline.input.rest.fetch('http://localhost:3000/api/resources'))
print(rest.fetch('http://localhost:3000/api/resources'))
print(fetch('http://localhost:3000/api/resources'))

# import pipeline.input.rest.fetch
