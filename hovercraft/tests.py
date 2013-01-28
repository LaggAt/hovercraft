import unittest
from pkg_resources import resource_string
from hovercraft import rest2impress
import io

class HovercraftTests(unittest.TestCase):

    def test_test(self):
        example = resource_string(__name__, 'examples/test.rst')
        result = rest2impress(example)
        print(result)
        with open('/tmp/test.html', 'wb') as outfile:
            outfile.write(result)
    
    def notest_example(self):
        example = resource_string(__name__, 'examples/slideshow.rst')
        result = publish_string(example, writer=ImpressWriter())
        
        

if __name__ == '__main__':
    unittest.main()
    
    