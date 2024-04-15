def candies(ratings):
    n=len(ratings)
    candy=[1]*n
    
    for i in range(1,n):
        if ratings[i]>ratings[i-1]:
            candy[i]=candy[i-1]+1
    for j in range(n-2,-1,-1):
        if ratings[j]>ratings[j+1]:
            candy[j]=max(candy[j],candy[j+1]+1)
    print(f"Min candies: {sum(candy)}")
ratings=[1,2,1,2,3,1]
candies(ratings)