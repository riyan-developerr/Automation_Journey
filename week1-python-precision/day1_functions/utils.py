#greeting function
def greet(name,greeting="Welcome"):
    return f"{greeting} {name}"
    

#calculating discount

def Price_af_discount(price,discount=10):
    #error handling
    if discount<0 or discount>100:
        return "Invalid discount value"
    else:
        discounted_amt=(discount/100)*price
        final_amt=(price-discounted_amt)
        return round(final_amt,0)
    
# summarizer function we give list and it will give the summary of the list
def summarize(lis):
    #list will be of numbers
    # count,min,max,average and sum
    
    #error handling
    if not lis:
        return "empty list"
    min=lis[0]
    max=lis[0]
    sum=0
    count=0
    for items in lis:
        if items>max:
            max=items
        if items<min:
            min=items
        
        sum+=items
        count+=1
    #when loop ends we will have max,min and sum now to find average
    average=float(sum)/count
    
    summary={
        "count":count,
        "sum":sum,
        "min":min,
        "max":max,
        "average":average
    }
    return summary

#function to handle **kewarg

#important thing to remember
# * -> undetermined normal inputs
# ** -> undetermined named inputs
# * ** are also used for unpacking
# info={"phone":223232334,"add":"johar col","height":5.11 }
# print(profile("Riyan",18,**info))

# *arg packs them as tuple
# **kwarg packs them as dictionary
def profile(name,age,**extrainfo):
    intro=f"{name} is {age} years old"
    for key,values in extrainfo.items():
        intro+=f"\n{key} : {values}"
    
    return intro

#repeating an action / function call
def repeat_action(action,times,*arg,**kwarg):
    results=[]
    for repeat in range(times):
        result=action(*arg,**kwarg)
        results.append(result)
    return results


