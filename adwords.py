import sys
import csv
import random,copy

def read_bidder_data():
    bidder_data=[]
    bidder_budget=[]
    with open('bidder_dataset.csv') as f:
        reader=csv.reader(f)
        next(reader,None)
        for rec in reader:
            #print(rec)
            temp1,temp2=[],[]
            temp1.append(int(rec[0]))
            temp2.append(int(rec[0]))
            temp1.append(rec[1])
            temp1.append(float(rec[2]))
            if rec[3]!='':
                temp2.append(float(rec[3]))
                bidder_budget.append(temp2)
            bidder_data.append(temp1)
        #bidder_data=list(reader)
    #print(bidder_data)
    #pass
    return bidder_data,bidder_budget

def read_queries():
    return open('queries.txt').read().split('\n')
    #print(queries)
    
def read():
    return read_bidder_data(),read_queries()
    pass

def greedy_revenue(bid,queries):
    revenue=0
    for each_query in queries:
        max=float('-inf')
        bidder_id=-1
        #print(each_query)
        for each_bidder in bid[0]:
            #if each_bidder[1]==each_query and max>each_bidder[2]:
                #print(each_bidder[1])
            if each_bidder[1]==each_query and max<each_bidder[2] and bid[1][each_bidder[0]][1]>=each_bidder[2]:
                max=each_bidder[2]
                bidder_id=each_bidder[0]
        if max!=float('-inf'):
            bid[1][bidder_id][1]=bid[1][bidder_id][1]-max
            revenue=revenue+max
    return revenue

def shuffle_revenue(bid,queries,function):
    revenue=[]
    for i in range(100):
        random.shuffle(queries)
        bid_copy=copy.deepcopy(bid)
        revenue.append(function(bid_copy,queries))
    print(revenue)
    return(sum(revenue)/len(revenue))
    pass

def greedy():
    bid,queries=read()
    bid_copy=copy.deepcopy(bid)
    #print(float('-inf'))
    revenue_opt=greedy_revenue(bid_copy,queries)
    print(revenue_opt)
    bid_copy=copy.deepcopy(bid)
    revenue_alg=shuffle_revenue(bid_copy,queries,greedy_revenue)
    print(revenue_alg/revenue_opt)
    #print(queries[0])
    
    #print(queries[0])
    pass

def balance():
    bid,queries=read()
    pass

def msvv():
    bid,queries=read()
    pass

random.seed(0)

if len(sys.argv)!=2:
    print("Please Specify Algorithm to use")
    exit()

if sys.argv[1]=='greedy':
    greedy()
elif sys.argv[1]=='balance':
    balance()
elif sys.argv[1]=='msvv':
    msvv()
else:
    print("Not a valid Algorithm")
    exit()
