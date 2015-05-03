from newsapp.models import *

def add_data():
     source1 = NewsSource(name="The Hindu", url="http://www.thehindu.com")
     source1.save()
     source2 = NewsSource(name="The Hindu", url="http://www.thehindu.com")
     source2.save()
     category = NewsCategory(name="India")
     category.save()
     category.sources.add(source1)
     category.sources.add(source2)
     return 'Hello!'