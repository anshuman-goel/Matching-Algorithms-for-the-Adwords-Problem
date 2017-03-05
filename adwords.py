import sys,csv,random,copy

def read_bidder_data():
    bidder_data=[]
    bidder_budget=[]
    with open('bidder_dataset.csv') as f:
        reader=csv.reader(f)
        next(reader,None)
        for rec in reader:
            temp1,temp2=[],[]
            temp1.append(int(rec[0]))
            temp2.append(int(rec[0]))
            temp1.append(rec[1])
            temp1.append(float(rec[2]))
            if rec[3]!='':
                temp2.append(float(rec[3]))
                bidder_budget.append(temp2)
            bidder_data.append(temp1)
    return bidder_data,bidder_budget

def read_queries():
    return open('queries.txt').read().split('\n')
    
def read():
    return read_bidder_data(),read_queries()

def greedy_revenue(bid,queries):
    revenue=0
    for each_query in queries:
        max=float('-inf')
        bidder_id=-1
        for each_bidder in bid[0]:
            if each_bidder[1]==each_query and max<each_bidder[2] and bid[1][each_bidder[0]][1]>=each_bidder[2]:
                max=each_bidder[2]
                bidder_id=each_bidder[0]
        if max!=float('-inf'):
            bid[1][bidder_id][1]=bid[1][bidder_id][1]-max
            revenue=revenue+max
    return revenue

def balance_revenue(bid,queries):
    revenue=0
    for each_query in queries:
        max=float('-inf')
        bidder_id,bid_value=-1,-1
        for each_bidder in bid[0]:
            if each_bidder[1]==each_query and max<bid[1][each_bidder[0]][1] and bid[1][each_bidder[0]][1]>=each_bidder[2]:
                max=bid[1][each_bidder[0]][1]
                bidder_id=each_bidder[0]
                bid_value=each_bidder[2]
        if max!=float('-inf'):
            bid[1][bidder_id][1]=bid[1][bidder_id][1]-bid_value
            revenue=revenue+bid_value
    return revenue

def shuffle_revenue(bid,queries,function):
    revenue=[]
    for i in range(100):
        random.shuffle(queries)
        bid_copy=copy.deepcopy(bid)
        revenue.append(function(bid_copy,queries))
    return(min(revenue))

def total_budget(bid):
    sum=0
    for each_bid_budget in bid[1]:
        sum+=each_bid_budget[1]
    return sum

def greedy():
    bid,queries=read()
    bid_copy=copy.deepcopy(bid)
    revenue=greedy_revenue(bid_copy,queries)
    print(revenue)
    bid_copy=copy.deepcopy(bid)
    revenue_alg=shuffle_revenue(bid_copy,queries,greedy_revenue)
    revenue_opt=total_budget(bid)
    print(round(revenue_alg/revenue_opt,2))

def balance():
    bid,queries=read()
    bid_copy=copy.deepcopy(bid)
    revenue=balance_revenue(bid_copy,queries)
    print(revenue)
    bid_copy=copy.deepcopy(bid)
    revenue_alg=shuffle_revenue(bid_copy,queries,balance_revenue)
    revenue_opt=total_budget(bid)
    print(round(revenue_alg/revenue_opt,2))

def msvv():
    bid,queries=read()

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
