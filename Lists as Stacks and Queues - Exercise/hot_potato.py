def play_hot_potato(names, n):

    loser_ind = 0
    while(True):  
        sz = len(names)
        #I have no idea why this works
        loser_ind = (n + loser_ind - 1) % sz 
        loser = names.pop(loser_ind)

        if(sz > 1):
            print(f"Removed {loser}")
        else:
            print(f"Last is {loser}")
            break

play_hot_potato(input().split(), int(input()))

#Tracy Emily Daniel
#1000000

#George Peter Michael William Thomas
#10