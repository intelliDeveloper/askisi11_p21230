
'''Αριθμός Μητρώου: Π21230'''


def sos(lst):
    count = 0
    #Γραμμές
    for lists in lst:
        for a in range(0, len(lists)):
            if (a+2) < len(lists):
                if lists[a] == "s":
                    if lists[a+2] == "s":
                        if lists[a+1] == "o":
                            count += 1

    #Στήλες
    length = 0
    for lists in lst:
        length = len(lists)

    for a in range(length):
        l = []
        for b in range(len(lst)):

            l.append(lst[b][a])

        for a in range(0, len(l)):
            if (a + 2) < len(l):
                if l[a+2] == "s":
                    if l[a] == "s":
                        if l[a+1] == "o":
                            count += 1

    #Διαγώνιες
    for i in range(len(lst) - 2):
        for j in range(len(lst[i]) - 2):
            if lst[i][j]+lst[i+1][j+1]+lst[i+2][j+2] == "sos":
                count += 1

    for i in range(len(lst) - 2):
        for j in range(2, len(lst[i])):
            if lst[i][j] + lst[i+1][j-1] + lst[i+2][j-2] == "sos":
                count += 1

    '''Επιστροφή των "sos" που ζητάει η άσκηση.'''
    return count

    '''Άμα θέλουμε να κάνουμε print τη μήτρα:
    print('Η μήτρα είναι:')
    for lists in lst:
        print(lists)
        
    Εδώ κάνουμε print to count
    print('\nΤο άθροισμα όλων των sos είναι', count)'''


'''Κλήση της συνάρτησης sos(lst,t) γίνεται:'''
'''sos([["s", "o", "s", "s"], ["o", "o", "s", "o"], ["s", "o", "s", "s"], ["s", "o", "s", "s"]])'''