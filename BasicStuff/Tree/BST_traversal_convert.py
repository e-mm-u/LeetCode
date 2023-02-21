pre_order = [8,26,9,11,14,25,35,32]
post_order = [25,14,11,9,32,35,26,8]

def pretopost(pre):
    if not pre:
        return []
        
    root = pre[0]
    print(root)
    left = []
    right = []
    for i in range(1,len(pre)):
        if pre[i]<root:
            left.append(pre[i])
        else:
            right.append(pre[i])
    print("left ",left)
    print("right", right)
    
    left_post = pretopost(left)
    right_post = pretopost(right)
    
    return left_post+right_post+[root]
def posttopre(post):
    if not post:
        return []
        
    root = post[-1]
    print(root)
    left,right = [],[]
    for i in range(len(post)-1):
        if post[i]<root:
            left.append(post[i])
        else:
            right.append(post[i])
    print(left,right) 
    left_pre = posttopre(left)
    right_pre = posttopre(right)
    
    return [root]+left_pre+right_pre
            
def pretoin(pre):
    if not pre:
        return []
        
    root = pre[0]
    print(root)
    left = []
    right = []
    for i in range(1,len(pre)):
        if pre[i]<root:
            left.append(pre[i])
        else:
            right.append(pre[i])
    print("left ",left)
    print("right", right)
    
    left_post = pretoin(left)
    right_post = pretoin(right)
    
    return left_post+[root]+right_post

def posttoin(post):
    if not post:
        return []
        
    root = post[-1]
    print(root)
    left = []
    right = []
    for i in range(len(post)-1):
        if post[i]<root:
            left.append(post[i])
        else:
            right.append(post[i])
    print("left ",left)
    print("right", right)
    
    left_post = posttoin(left)
    right_post = posttoin(right)
    
    return left_post+[root]+right_post
# get_post_order = pretopost(pre_order)
# print(get_post_order)
# get_pre_order = posttopre(post_order)
# print(get_pre_order)
# get_in_order = pretoin(pre_order)
# print(get_in_order)
get_in_order = posttoin(post_order)
print(get_in_order)