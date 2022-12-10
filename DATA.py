import json
  
class A ():
    def Read(self):
        with open('mydata.json', 'r') as f:
            data = f.read()
            A.y = json.loads(data)

    def Write(self, obj, val):
        A().Read()
        with open('mydata.json', 'w') as f:
            A.y.append({f"{obj}" : f"{val}"})
            json.dump(self.y, f)
        print("New item has successfully upload to the list. ")
    
    def ReWrite(self, dobj, dval):
        A().Read()
        new = [item for item in A.y if item.get(f"{dobj}") != f"{dval}"]
        A.y = new
        with open('mydata.json', 'w') as f:
            json.dump(A.y, f)
        print("The item has already successfully deleted. ")
    
    def Find(self, find):
        A().Read()
        thing = [item for item in A.y if item.get(f"{find}")]
        if len(thing) == 0:
            print("There is no item found")
        else:
            print(thing)
    
class List():
    def list(self):
        print("""
        read    --   get the item from the list
        write   --   write the item to the list
        delete  --   delete the item from the list
        find    --   find the item from the list
        exit    --   exit the system
        \n""")
