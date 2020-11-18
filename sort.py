def selectionsort(l):
    #scan slices l[0:lens(l)],l[1:lens(l)],
    for start in range(len(l)):

        #find minimum value in slices...
        minpos = start
        for i in range(start,len(l)):
            if l[i] < l[minpos]:
                minpos = i

            #... and move it to start of slice
            (l[start],l[minpos]) = (l[minpos],l[start])
