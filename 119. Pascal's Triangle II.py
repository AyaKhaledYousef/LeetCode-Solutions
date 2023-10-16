def getRow (rowIndex):
    res = [1]

    for i in range(rowIndex):
        next_row = [0] *(len(res)+1) # [0,0,0,....]
        for j in range(len(res)):
            next_row[j] += res[j]
            next_row[j+1] += res[j]
            

        res = next_row

    return res

if __name__ == "__main__":
    getRow(2)
