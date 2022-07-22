# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class HashTable:
    _multiplier = 263
    _prime = 1000000007    
    
    def __init__(self, m):
        self.m = m          #number of buckets
                            #each bucket is a list of strings
        
        self.buckets = [None]*m
        
        
    def __str__(self):
        s = "hash table\n"
        for i in range( len(self.buckets) ):
            if self.buckets[i] != None:
                s += str(i) +": "+" ".join(self.buckets[i])
        return s
    
    def _hash_func(self, s):
        #The ord() function returns an integer representing the Unicode character.
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.m
    
    def add(self, s):
        """
        add the string s to the hash table, if not already there
        """
        hashval = self._hash_func(s)
        if self.buckets[hashval] == None:
            self.buckets[hashval]= [s]
        elif s not in self.buckets[hashval]:
            self.buckets[hashval].append(s)
        
    def delete(self, s):
        """
        remove the string s from the hash table, if it is present
        """
        hashval = self._hash_func(s)
        
        if self.buckets[hashval] != None and s in self.buckets[hashval]:
            self.buckets[hashval].remove(s)   
            
            if len(self.buckets[hashval]) == 0:
                self.buckets[hashval] = None  #set back to None if list empty
    
    def find(self, s):
        """
        return "yes" if string s is in hash table, otherwise "no"
        """
        hashval = self._hash_func(s)
        
        if self.buckets[hashval] != None and s in self.buckets[hashval]:
            return "yes"
        else:
            return "no"
 
    
    def check(self, i):
        """
        returns the content of ith list in table
        with spaces separating each element
        return blank line if list is empty
        """

        bucket = self.buckets[i]  #bucket is a list of strings
        if bucket == None:
            return ""
        else:  
            return ' '.join( reversed(bucket) )
        
        
    
    def process_queries(self, queries):
        """
        queries is a list of query objects
        queries can be add string, del string, find string, or check i
        """
        result = []  #list of strings to output as result
        for q in queries:
            if q.type == "add":
                self.add(q.s)
            elif q.type == "del":
                self.delete(q.s)
            elif q.type == "find":
                result.append(self.find(q.s))
            elif q.type == "check":
                result.append(self.check(q.ind))
        return result
            
        
def test(m):
    ht = HashTable(m)    
    ht.add("string")
    ht.delete("string")
    ht.add("helloworld")
    ht.add("world")
    ht.add("hello")
    ht.add("HellO")
    ht.add("slithytoves")
    print(ht.buckets)
    
    for i in range(m):
        print(ht.check(i))
        
    for s in ["string", "helloworld", "world", "HellO", "slithytoves"]:
        print("find", s, ": ", ht.find(s))
    
    ht.delete("HellO")
    print(ht.buckets)   
    ht.delete("world")
    print(ht.buckets)    
    ht.delete("helloworld")
    print(ht.buckets)           
    
    for s in ["string", "helloworld", "world", "HellO", "slithytoves"]:
        print("find", s, ": ", ht.find(s))

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    m = int(input())
    ht = HashTable(m)
    
    n = int(input())
    
    queries = [Query(input().split()) for i in range(n)]
    
    result = ht.process_queries(queries)
    print('\n'.join(result))
        
