def explore_branch(branch, path_so_far):
    if branch == 12:
        print path_so_far
    else:
        explore_branch(branch+1, path_so_far+"0")
        explore_branch(branch+1, path_so_far+"1")

explore_branch(0,"")





     
        

