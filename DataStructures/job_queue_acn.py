# python3


import math
import random
from collections import namedtuple    


class Worker(object):
    def __init__(self, identifier, time):
        self.id = identifier
        self.time = time

class WorkerTree(object): 
    def __init__(self, n_workers, Max=False):
        """
        creates a binary tree to represent n_workers 
        each node is a  Worker, composed of an id and a time.
        
        intially all times=0 and the ids are ascending from 0
        
        by default Max = False to make a mintree
        
        when storing the nodes, 
        index=0 is left unused and the root node starts at index=1. 
        So that the children of the node at index=k are at 2k and 2k+1.
        Also, the parent of the node at index j will be at j//2. 
        """
        self.nodes = [None]
        for i in range(n_workers):
            self.nodes.append(Worker(i,0))
        
        self.Max = Max               #set whether maxtree or mintree

        
    def countnodes(self):
        """
        returns number of nodes in the tree
        """
        
        return len(self.nodes)-1  # pos 0 not used
        
    
    def countlevels(self):
        """
        returns the number of levels in the tree
        """
        num_nodes = self.countnodes()
        
        ## throw away the decimal then add one to get right result, 
        ## eg 7 nodes is a full three levels
        ## 8 nodes is four levels (the 8th node goes to level 4)
        if num_nodes > 0:
            return int( math.log2(num_nodes) ) + 1
        else:
            return 0
        
    def __str__(self):
         s = "binary tree made from:\n" + str(self.nodes) + "\n"
         s+= "number of nodes = " + str(self.countnodes()) + "\n"
         s+= "number of levels =" + str(self.countlevels()) + "\n"
         s+= "type ="
         if self.Max==True:
             s+=" maxtree"
         else:
             s+=" mintree"
         s+= "\ntree representation:\n"
         
         s+= self.drawtree()
                 
         return s
         



    def swop(self, i1, i2):
        """
        swops the two nodes at i1 and i2
        indexes are assumed to be in range
        
        """
        assert i1<len(self.nodes)
        assert i2<len(self.nodes)
        
        val1 = self.nodes[i1]
        val2 = self.nodes[i2]
        
#        print("swopping", val1, "and", val2)
        
        self.nodes[i1] = val2
        self.nodes[i2] = val1
 
    def compare_workers(self, iparent, ichild):
        """
        compares the two workers at iparent and ichild and returns the best one 
        by the following criterion:
            the one with the lowest time is best
            if the times are equal, the one with the lowest id is best
            
        if the two workers are equal returns iparent (no sift down needed)

        """ 

        if self.nodes[iparent].time < self.nodes[ichild].time:
            return iparent
        if self.nodes[iparent].time > self.nodes[ichild].time:
            return ichild

        ## the times are equal, check the ids
        if self.nodes[iparent].id < self.nodes[ichild].id:
            return iparent
        if self.nodes[iparent].id > self.nodes[ichild].id:
            return ichild
        
        ## everything is equal
        return iparent
                
        
        

    def sift_worker_down(self, i=1):
        """ 
        sifts down the worker i down until its time >= that of its
        children
        if time= that of a child, sifts down to keep lowest id on top
        
        """         
        bestindex = i   # initially assume parent is better than its children
        lastindex = self.countnodes()
        
        if 2*i <= lastindex:  # left child exists
            bestindex = self.compare_workers(i, 2*i)  #if left child better it becomes bestindex
                                                
            if 2*i +1 <= lastindex:  # right child can exist only if left child exists
                bestindex = self.compare_workers(bestindex,2*i +1) 
                  
        if bestindex != i:
            self.swop(i, bestindex)
            self.sift_worker_down(bestindex)        


        
    def takejob(self, jobtime):
        """
        time is an int, the duration of the job to take
        adds this time to the topmost worker in the heap
        (ie the one with lowest time value)
        then sifts that worker down
        
        returns the worker that took the job (id/time) where the
        time value is *before* it is incremented, so that it is equal
        to the time when this job is started
        """

        top_worker = self.nodes[1]  # top worker has lowest time
        return_val = Worker(top_worker.id, top_worker.time)
        
        top_worker.time+=jobtime  #increment the top worker's time
        self.sift_worker_down(1)              #and sift down
        
        return return_val
        
        
        
        
    def drawtree(self):
        """
        draws the binary tree with proper spacing
        
        """
        
        # num items in lowest level, if full is: bottom_items = 2**(num_levels-1) 
        # we allow 2 spaces per item, plus one space before and after, so 
        # bottom_width = bottom_items * 4 = bottom_items * 2**2
        #              = 2**(num_levels-1) * 2**2 
        #              = 2**(num_levels+1)
        #
        # bottom_width = 2**(num_levels +1)
        
        # now on any given level we have numitems = 2**level
        # where the topmost level is 0. So, one item at root, two at level 1, etc.
        # And the width available for each item = bottom_width/numitems
        # so that:
        #     itemwidth= bottom_width/numitems = 2**(num_levels+1) / 2**level
        #                                       = 2**(num_levels+ 1 - level)

        s = ""   #string for the entire binary tree

        num_levels = self.countlevels()              #get number of levels in tree
        
        level=0                                      #start at root level
        itemwidth = 2**(num_levels+ 1 - level)
        level_s = ""
        for i in range(len(self.nodes)):
            if i==0:
                continue
            worker=self.nodes[i]
            worker_s = str(worker.id)+"/"+str(worker.time)
            item_s = " "+ worker_s +" " # item with spaces before and after
            item_s = item_s.center(itemwidth)
            level_s+= item_s
            if (math.log2(i+1))%1 == 0:    #was last node of a level
                s+= level_s
                s+="\n\n"
                level_s = ""
                level+=1
                itemwidth = 2**(num_levels+ 1 - level)
        s+= level_s #in case final level not complete        
        
        return s+"\n"






def assign_jobs(n_workers, jobs):
    result = []
    
    workers = WorkerTree(n_workers)   
    
    for job in jobs:
        next_worker = workers.takejob(job)
        # print("assigning job that takes time", job, "to worker id:",next_worker.id )
        # print("worker heap is now:")
        # print(workers.drawtree())
        
        result.append(next_worker)

    return result

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        print("doing job that takes time", job)

        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        print("next free worker is at index", next_worker)
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job
        print("workers next free time", next_free_time)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    
    # print("number of workers = ", n_workers)
    # print("jobs to do:")
    # print(jobs)

#    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for worker in assigned_jobs:
        print(worker.id, worker.time)


if __name__ == "__main__":
    main()
