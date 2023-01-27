def sortTheStudents(score, k):
    for i in range(len(score)):
        maxx = score[i][k]
        row = i
        for j in range(i+1,len(score)):
            if score[j][k]>maxx:
                row = j
                maxx = score[j][k]
                
        score[i],score[row] = score[row],score[i]
        
    return score
            