def collision_check(rect1, rect2): #jeweils tuple mit (rectX.pos,rectX.size)
    r1x = rect1[0][0]
    r1y = rect1[0][1]
    r2x = rect2[0][0]
    r2y = rect2[0][1]
    r1w = rect1[1][0]
    r1h = rect1[1][1]
    r2w = rect2[1][0]
    r2h = rect2[1][1]

    if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y +r2h and r1y + r1h > r2y):  #Algorithmus zur Kollisionsabfrage
        return True
    else:
        return False