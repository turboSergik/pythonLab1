
import json
import pprint as pp

a = """
{
[1, 3, 4] : [1, 2, 3]
}
"""

b = json.loads(a)
pp.pprint(b)
