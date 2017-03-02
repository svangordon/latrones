import hug
import happy_birthday
from pprint import pprint

pprint(vars(hug.test.get(happy_birthday, 'happy_birthday', {'name': 'Timothy', 'age': 25}))) # Returns a Response object
