from queue import Queue
import random 

# Function to find page faults using FIFO 
def __FIFO(pages, n, frame): 

	s = set() 

	indexes = Queue()                       # To store the pages in FIFO manner
	page_faults = 0
	for i in range(n): 
		if (len(s) < frame):
			if (pages[i] not in s): 
				s.add(pages[i])
				page_faults += 1
				indexes.put(pages[i])       # Push the current page into the queue

		# If the set is full then need to perform FIFO 
		# i.e. remove the first page of the queue from 
		# set and queue both and insert the current page 
		else:
			if (pages[i] not in s):
				val = indexes.queue[0]      # Pop the first page from the queue
				indexes.get()
				s.remove(val)               # Remove the indexes page
				s.add(pages[i])             # insert the current page 
				indexes.put(pages[i]) 
				page_faults += 1

	return print('pageFaults of FIFO algorithm = %d' % page_faults) 

def __Optimal(pages, n, frame):
    x = 0
    page_faults = 0
    page = []
    FREE = -1
    for i in range(frame):
        page.append(FREE)

    for i in range(n):
        flag = 0
        for j in range(frame):
            if(page[j] == pages[i]):
                flag = 1
                break
            
        if flag == 0:
            # look for an empty one
            faulted = False
            new_slot = FREE
            for q in range(frame):
                if page[q] == FREE:
                    faulted = True
                    new_slot = q
            
            if not faulted:
                # find next use farthest in future
                max_future = 0
                max_future_q = FREE
                for q in range(frame):
                    if page[q] != FREE:
                        found = False
                        for ii in range(i, n):
                            if pages[ii] == page[q]:
                                found = True
                                if ii > max_future:
                                    # print "\n\tFound what will be used last: a[%d] = %d" % (ii, a[ii]),
                                    max_future = ii
                                    max_future_q = q

                                break
                        
                        if not found:
                            # print "\n\t%d isn't used again." % (page[q]),
                            max_future_q = q
                            break

                faulted = True
                new_slot = max_future_q
            
            page_faults += 1
            page[new_slot] = pages[i]
            # print ("\n%d ->" % pages[i])
            # for j in range(frame):
            #     if page[j] != FREE:
            #         print (page[j])
            #     else:
            #         print ("-")
        # else:
        #     print ("\n%d -> No Page Fault" % pages[i])
            
    return print('pageFaults of Optimal algorithm = %d' % page_faults)

def __LRU(pages, n, frame):
    x = 0
    page_faults = 0
    page = []
    for i in range(frame):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(frame):
            if(page[j] == pages[i]):
                flag = 1
                break
            
        if flag == 0:
            if page[x] != -1:
                min = 999
                for k in range(frame):
                    flag = 0
                    j =  i
                    while j>=0:
                        j-=1
                        if(page[k] == pages[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        x = k

            page[x] = pages[i]
            x=(x+1)%frame
            page_faults+=1
        #     print ("\n%d ->" % pages[i])
        #     for j in range(frame):
        #         if page[j] != -1:
        #             print (page[j])
        #         else:
        #             print ("-")
        # else:
        #     print ("\n%d -> No Page Fault" % pages[i])
            
    print ('pageFaults of LRU algorithm = %d' % page_faults) 


if __name__ == '__main__':
    # setup input
    # pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    # n = len(pages)
    print('How many length of pages : ')
    n = int(input())
    # print('How many frame : ')
    # frame = int(input())
    pages = []
    for c in range(n):
        pages.append(random.randrange(0, 10))

print('')
print('pages =',pages)
print('')

print("--------- 3 Frame ----------")
frame = 3
__FIFO(pages, n, frame)
print("-----------------")
__Optimal(pages, n, frame)
print("-----------------")
__LRU(pages, n, frame)
print("-----------------")
print('')

print("--------- 7 Frame ----------")
frame = 7
__FIFO(pages, n, frame)
print("-----------------")
__Optimal(pages, n, frame)
print("-----------------")
__LRU(pages, n, frame)
print("-----------------")
print('')

print("--------- 10 Frame ----------")
frame = 10
__FIFO(pages, n, frame)
print("-----------------")
__Optimal(pages, n, frame)
print("-----------------")
__LRU(pages, n, frame)
print("-----------------")
print('')