# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class PhoneBook:
    def __init__(self):
        """
        phone book is intially empty
        phone numbers are max 7 digits and so range from 0 --> 9 999 999
        we use direct addressing to store each contact's name at the position i,
        where i=the phone number
        """
        self.book = [None]*10000000
        
    def __str__(self):
        s = "phone book:\n"
        for i in range( len(self.book) ):
            if self.book[i] != None:
                s+=self.book[i] +": " + str(i) +"\n"
                
        return s
                
    def add(self, number, name):
        """
        number is an int less than 9999999 and name is a string
        """
        self.book[number] = name
        
    def delete(self, number):
        self.book[number]= None
        
    def find(self, number):
        """
        returns a string, the name of the person at position number,
        or "not found" if there is no person for that number
        """
        result = self.book[number]
        if result == None:
            return "not found"
        else:
            return result


        

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))
    
   

def process_queries(queries):
    result = []
    pb = PhoneBook()  #create empty phone book
    
    for query in queries:
        if query.type == 'add':
            pb.add(query.number, query.name)
        elif query.type == 'del':
            pb.delete(query.number)
            
        elif query.type == 'find':
            result.append(pb.find(query.number))
            
    return result
    

def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

