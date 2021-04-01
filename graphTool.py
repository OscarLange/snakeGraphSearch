def returnDirection(yDirection, width, height, appleX, appleY, snake):
    x = snake[0][0]
    y = snake[0][1]
    #skip
    #is the apple above me
    if(appleY < y):
        #am I on a right turn
        if((y/10)%2 == 0):
            if(not looseGame(x,y, snake, 0, 10, width, height)):
                return [0,10]
        #am I on a left turn
        else:
            if(not looseGame(x,y, snake, -10, 0, width, height)):
                return [-10,0]
    elif(appleY > y):
        if(appleY == y+10):
            if(appleX > x and (appleY/10)%2 == 0):
                if(not looseGame(x,y, snake, 0, 10, width, height)):
                    return [0,10]
            if(appleX < x and (appleY/10)%2 != 0):
                if(not looseGame(x,y, snake, 0, 10, width, height)):
                    return [0,10]
            if(appleX == x):
                if(not looseGame(x,y, snake, 0, 10, width, height)):
                    return [0,10]
        else:
            if(not looseGame(x,y, snake, 0, 10, width, height)):
                return [0,10]
    #normal
    if(x == 0 and y != 0):
        return [0,-10]
    if(x == width-10 or x == 10):
        if(y == height-10):
            return [-10, 0]
        elif(yDirection != 10 and (y != 0 or x == width-10)):
            return [0, 10]
    if((y/10)%2 == 0):
        return [10,0]
    else:
        return [-10,0]

def looseGame(x,y, snake, xDirection, yDirection, width, height):
    if(yDirection == 10 and x == 10):
        return True
    x_tmp = x + xDirection
    y_tmp = y + yDirection
    for row in snake:
        if(row[0] == x_tmp and row[1] == y_tmp):
            return True
        current = score(x, y, width, height)
        future = score(x_tmp, y_tmp, width, height)
        tail = score(row[0], row[1], width, height)
        if(current < tail and future > tail):
            return True
    if(x_tmp < 0 or x_tmp >= width or y_tmp < 0 or y_tmp >= height or x == 0):
        return True
    return False

def score(x,y, width, height):
    nMinus10 = ((width-10)-10)
    if(x == 0):
        if(y == 0):
            return 0
        else:
            return (height+10)*nMinus10 + (height-10-y)
    else:
        if((y/10)%2 == 0):
            return nMinus10*y+x
        else:
            return nMinus10*y+(width-x)