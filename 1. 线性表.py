class singleNode:
  def __init__(self,item):
    self.item = item
    self.next = None
class singleLink:
  def __init__(self):
    self.head = None
  def isEmpty(self):
    return self.head == None
  def travel(self):
    if not self.head:
      return
    cur = self.head
    while cur:
      print(cur.item,end = ' ')
      cur = cur.next
  def length(self):
    result = 0
    if not self.head:
      return result
    cur = self.head
    while cur:
      result += 1
      cur = cur.next
    return result
  
    
