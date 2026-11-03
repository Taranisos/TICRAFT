import ti_draw, time, random, ti_system, math

#varables
height = 4
graphics = 0
game = False
building = False
new_world = False
chunk = []
world_border = False
key_list=[102,92,93,94,82,83,84,72,73,74]
menu_select = 1
draw_menu = True



#colors
a=(44,129,21)
b=(93,174,58)
c=(119,203,83)
d=(103,237,108)
e=(116,76,52)
f=(144,96,66)
g=(166,112,76)
h=(183,135,94)
i=(161,155,148)
j=(104,104,104)
k=(116,116,116)
l=(127,127,127)
m=(143,143,143)
n=(56,43,24)
o=(76,61,38)
p=(95,74,43)
q=(116,90,54)
r=(145,113,66)
t=(152,120,73)
u=(126,98,55)
v=(159,132,77)
w=(175,143,85)
x=(184,148,95)
y=(194,157,98)
z=(139,193,205)
é=(168,208,217)
è=(208,234,233)
s1=(209,186,138)
s2=(213,196,150)
s3=(218,207,163)
s4=(227,219,176)
s5=(231,228,187)
s6=(237,235,203)
i1=(177,176,176)
i2=(185,185,185)
i3=(193,193,193)
i4=(209,207,207)
i5=(214,214,214)
i6=(220,220,220)
i7=(224,224,224)
i8=(230,230,230)
i9=(236,236,236)
i10=(242,242,242)
l1=(43,65,41)
l2=(49,76,47)
l3=(62,99,60)
l4=(76,121,73)
w1=(30,56,107)
w2=(32,59,112)
w3=(35,65,125)
w4=(38,71,135)
w5=(45,83,163)
black=(0,0,0)
menu_color=(111,110,113)
dark_sky=(5,23,52)
light_sky=(130, 172, 255)
s=light_sky #sky
white=(255,255,255)




#blocks
#blocks 8x8
grass = [a,[6,0],[15,0],c,[9,0],[21,0],[0,3],[18,3],[15,6],d,[0,0],[12,3],[21,3],e,[3,3,2],[0,6],[9,6,-2],[12,9],[18,9],[15,12],[6,15,2],[21,15],[9,18,2],[0,21],[18,21],f,[18,6],[3,9,2],g,[6,6],[0,9],[6,12,2],[21,12],[0,15],[12,15],[3,18],[18,18],[15,21],h,[21,9],[3,12],[12,12],[0,18],[15,18],[21,21],i,[3,6],[15,15],[6,21]]
dirt = [e,[9,0,-4],[12,0],[0,3],[21,9],[3,12],[18,12,2],[6,18,2],[0,21,2],[15,21],f,[6,0],[21,0],[12,3],[3,6,2],[18,6],[15,9,2],[6,12],[12,12],[0,15],[9,15],[15,15],[12,18],[18,18],[18,21,2],h,[3,0],[15,0],[0,6],[12,6],[0,9,2],[6,15],[21,15],[15,18],[9,21],i,[3,3],[18,3],[12,15],[3,18]]
stone = [j,[6,6,2],[21,6],[18,18,-2],[3,21,2],[15,21],k,[15,0,2],[6,3],[12,3],[3,6],[12,6,3],[0,12],[9,12,3],[21,12],[0,18,-2],[9,21,2],[21,21],m,[0,0,2],[9,0],[6,9,2],[15,9],[3,15],[9,18,3],[21,18]]
oak_log = [n,[18,0],[15,3,-2],[3,6,-2],[15,12],[18,18,-2],[6,21],o,[6,0],[3,3],[21,3,-5],[15,9],[3,12],[6,15,-2],[15,15],p,[6,3,-2],[9,3,-4],[0,18,-2],[15,18],r,[0,9,-3],[12,15,-3],[21,21],t,[18,3,-2]]
oak_planks=[q,[9,9],[18,9,2],[0,21,2],[18,21,2],t,[0,9],[12,9],[21,15,-2],[12,21],u,[9,3,-2],[3,9,2],[15,9],[6,21,2],[15,21],v,[9,0],[15,3],[21,6],[6,12],[21,12],[12,15],[18,15],[0,18,2],x,[0,0],[6,0],[0,3,2],[21,3],[3,6,2],[15,6],[0,12],[3,15,2],[9,18],y,[12,0,4],[3,12],[9,12,4]]
glass=[z,[21,6,-6],[3,21,5],é,[21,0,-2],[6,9],[0,18,-2],[21,18],[18,21,2],è,[0,0,-6],[3,0,6],[9,6],[15,15]]
sand = [s1,[15,0],[6,6],s2,[0,3],[9,3,-3],[15,3,2],[12,6],[15,9],[21,9],[0,12],[12,12],[3,15],[0,18],[9,18,2],[18,18],[3,21],[12,21],[21,21],s3,[3,9,2],s4,[9,0],[18,0],[21,3],[0,6],[18,9],[15,12],[21,12],[12,15,3],s5,[0,0],[15,6],[3,18],s6,[6,12],[15,18]]
iron=[i1,[21,3],[0,9],[21,12],[0,18],i2,[21,6,-2],[21,15,-2],[6,21,6],i4,[0,0],[9,0,5],i5,[15,9,2],[15,18,2],i6,[3,9,2],[3,18,4],i7,[9,9,2],i8,[3,6,6],[12,12,3],[3,15,6],i9,[18,3],[9,12],i10,[3,3,5],[3,12,2]]
oak_leaves=[l1,[0,0,-2],[6,0,-2],[12,3],[21,6],[9,9],[6,12],[21,21],l2,[21,0,-2],[3,3],[0,6,2],[18,6],[6,15],[0,18,2],l3,[18,3],[15,6],[0,9],[18,9,2],[3,12,-2],[9,12,-2],[6,18],[18,18],[0,21],l4,[12,0,2],[0,15],[15,15,2],[12,18,2],[21,18],[3,21],[15,21,2]]
water = [w1,[0,0],[9,0,5],[3,3,4],[0,6,2],[12,6,4],[15,9],[3,12,3],[0,15,4],[15,15,3],[3,18,2],w3,[6,9,2],[21,9],[18,12],[6,21,2],[15,21,2],w4,[6,0],w5,[21,12],[12,21]]




#blocks 4x4
grass4 = [a,[6,0],b,[12,0,-2],c,[0,0],d,[18,0],e,[0,12],[18,18],g,[18,6],[12,12],[0,18],h,[6,6,-2]]
dirt4 = [e,[6,0],[0,12],g,[12,0,-2],[6,12],[0,18],h,[6,6],[18,6],[12,18,2]]
stone4 = [j,[6,12,3],k,[0,6,3],[6,18],m,[12,0,2],[0,12,-2]]
oak_log4 = [n,[18,0,-2],[6,6,-3],o,[18,12],p,[12,0,-3],[0,12,-2],t,[12,18]]
oak_planks4 = [p,[0,0],q,[6,0,2],[18,12],r,[18,0],[0,12],u,[6,12,2],v,[6,6,2],x,[18,6],[12,18]]
oak_leaves4 = [l1,[0,12,2],l2,[0,6],l3,[12,0],[0,18],l4,[18,0,-3],[12,6],[6,18]]
glass4 = [z,[18,0,-2],é,[0,18,2]]
sand4 = [s1,[0,6,3],[6,12],s3,[0,0],[18,0],s5,[0,12,-2],s6,[6,0,2],[12,18,2]]
iron4 = [i2,[12,0],[18,0,-3],[0,18,2],i4,[6,6,2],i7,[6,12],i10,[12,12]]
water4 = [w2,[0,12,3],w3,[12,0,2],w5,[0,6,3],[0,18,2]]





#load/save
def can_load_world(world):
    try:
        return ti_system.recall_list(world)
    except Exception:
        return None

def save_world(world, saving):
    try:
        ti_system.store_list(saving, world)
        return True
    except:
        return False

def trans_for_save(world):
    print("Changing to save format.")
    warning = False
    save_worlds = []
    counter = -500
    for worlds in range(0,1000,100):
        print("Formatting world ", round((worlds+1)/100)+1, "/ 10.")
        save_world = []
        for list in range(100):
            if worlds+list == 0:
                    save_world.append(world[0])
            else:
                counter += 1
                fixchunk = world[worlds+list]
                chunk = ""
                if len(fixchunk) != 8:
                    warning = True
                    if len(fixchunk) < 8:
                        print("Console: Warning chunk corruption, chunk ", counter," is corrupted and misses ",8-len(fixchunk), " blocks, filling in with air.")
                        for fix in range(8-len(fixchunk)):
                            fixchunk.append(0)
                    else:
                        print("Console: Warning: chunk corruption, chunk ", counter," is corrupted and has ",len(fixchunk)-8, " blocks too mutch, deleting highest ones.")
                        for fix in range(len(fixchunk)-8):
                            fixchunk.pop(0)
                chunk = "1"
                for i in range(8):
                    chunk += str(fixchunk[7-i])
                save_world.append(int(chunk))
        save_worlds.append(save_world)
    if warning:
        print("Console: Info: world saved succesfully!")
        time.sleep(3)
    return save_worlds



def trans_for_use(player_x = None):
    world = can_load_world("MCWD0")
    warning = False
    load_next_chunk = False
    load_previous_chunk = False
    use_world = []
    if player_x == None:
        player_x = world[0]
    use_world.append(player_x)
    chunk_to_load = math.floor((player_x+499)/20)
    if abs(player_x + 401) > 5:
        if player_x -(chunk_to_load*20-499) < 6 or chunk_to_load == 49:
            load_previous_chunk = True
        world_to_load = math.floor(chunk_to_load/5)
        world_name = "MCWD"
        world_name += str(world_to_load)
        use_world.append(chunk_to_load)
        world = can_load_world(world_name)
        chunk1 = check_and_load_chunk(chunk_to_load)
        if not load_previous_chunk:
            load_next_chunk = True
        if load_next_chunk:
            use_world.append(chunk_to_load+1)
            chunk2 = check_and_load_chunk(chunk_to_load+1)
        elif load_previous_chunk:
            use_world.append(chunk_to_load-1)
            chunk2 = check_and_load_chunk(chunk_to_load-1)
        
    if warning:
        print("Console: Info: world loaded succesfully!")
        time.sleep(3)
    use_world.append(chunk1)
    use_world.append(chunk2)
    return use_world



def load_chunk(start,world, end):
    chunk = []
    for i in range(start,end):
        row = []
        strchunk = str(world[i])
        if len(strchunk) < 9:
            print(strchunk)
            print(world[i])
            time.sleep(3)
            warning = True
            print("Console: Warning chunk corruption, chunk ", i-50," is corrupted and misses ",9-len(strchunk), " blocks, filling in with air.")
            for fix in range(9-len(strchunk)):
                strchunk += "0"
        for index in range(1, 9):
            row.append(int(strchunk[9-index]))
        chunk.append(row)
    return chunk

def check_and_load_chunk(chunk):
    world_to_load = math.floor(chunk/5)
    world_name = "MCWD"
    world_name += str(world_to_load)
    chunk_to_load = 20*(chunk-(world_to_load*5))
    world = can_load_world(world_name)
    if chunk == 0:
        chunk_to_load = 1
        end = 20
    else:
        end = chunk_to_load+20
    chunk = load_chunk(chunk_to_load,world, end)
    return chunk

def save_chunk(chunk, chunk_x):
    world_to_save = math.floor(chunk_x/5)
    world_name = "MCWD"
    world_name += str(world_to_save)
    chunk_to_save = chunk_x-(world_to_save*5)
    saving_chunk = []
    for row in chunk:
        fixchunk = row
        save_row = "1"
        if len(fixchunk) != 8:
            warning = True
            if len(fixchunk) < 8:
                print("Console: Warning chunk corruption, chunk ", chunk_x," is corrupted and misses ",8-len(fixchunk), " blocks, filling in with air.")
                for fix in range(8-len(fixchunk)):
                    fixchunk.append(0)
            else:
                print("Console: Warning: chunk corruption, chunk ", chunk_x," is corrupted and has ",len(fixchunk)-8, " blocks too mutch, deleting highest ones.")
                for fix in range(len(fixchunk)-8):
                    fixchunk.pop(0)
        for i in range(8):
            save_row += str(fixchunk[7-i])
        saving_chunk.append(int(save_row))
    try:
        saving_world = ti_system.recall_list(world_name)
    except:
        saving_world = None
        print("Failed to save chunk")
    if saving_world is not None:
        chunk_block = chunk_to_save*20
        counter = 0
        if chunk_x != 0:
            end = chunk_block + 20
        else:
            chunk_block = 1
            counter = 0
            end = 20
        for i in range(chunk_block, end):
            saving_world[i] = saving_chunk[counter]
            counter += 1
    save_world(saving_world, world_name)
def save_player_x(player_x):
    world = can_load_world("MCWD0")
    world[0] = player_x
    save_world(world,"MCWD0")

def is_bordering_chunk(player_x, dir, chunk):
    player_x -= (chunk*20)-500
    player_x = str(player_x)
    if chunk == 0:
        if player_x == "14":
            return True
    elif dir:
        if player_x == "15":
            return True
    else:
        if player_x == "6":
            return True
    return False
def is_in_chunk(x, chunk1,chunk2):
    border = 19
    if chunk1 == 0:
        border = 18
    check = x+499-(chunk1*20)
    if check >= 0 and check <= border:
        list = [3, check]
    else:
        check = x+499 - (chunk2*20)
        list =[4, check]
        if check == 19 and chunk2 == 0:
            list = [3, 0]
    return list







#draw
def draw_block(x, y, block):
    for i in block:
        if isinstance(i, list):
            if len(i) == 2:
                ti_draw.fill_rect(i[0]+x,i[1]+y, 4, 4)
            else:
                if i[2] >= 0:
                    ti_draw.fill_rect(i[0]+x,i[1]+y, i[2]*3+1, 4)
                else:
                    ti_draw.fill_rect(i[0]+x,i[1]+y,4, abs(i[2])*3+1)
        else:
            ti_draw.set_color(*i)

def draw_block4x4(x, y, block):
    for i in block:
        if isinstance(i, list):
            if len(i) == 2:
                ti_draw.fill_rect(i[0]+x,i[1]+y,7, 7)
            else:
                if i[2] >= 0:
                    ti_draw.fill_rect(i[0]+x,i[1]+y, i[2]*6+1, 7)
                else:
                    ti_draw.fill_rect(i[0]+x,i[1]+y,7, abs(i[2])*6+1)
        else:
            ti_draw.set_color(*i)

def draw_grass(x,y,grass,grass4,graphics):
    if graphics == 0:
        ti_draw.set_color(*b)
        ti_draw.fill_rect(x,y,25,7)
        ti_draw.set_color(*f)
        ti_draw.fill_rect(x,y+6,25,19)
    if graphics == 1:
        ti_draw.set_color(*f)
        ti_draw.fill_rect(x,y,25,25)
        draw_block4x4(x,y,grass4)
    elif graphics == 2:
        ti_draw.set_color(*b)
        ti_draw.fill_rect(x,y,25,13)
        ti_draw.set_color(*f)
        ti_draw.fill_rect(x,y+12,25,13)
        draw_block(x,y,grass)

def draw_dirt(x,y,dirt,dirt4,graphics):
    if graphics == 0:
        ti_draw.set_color(*g)
        ti_draw.fill_rect(x,y,25,25)
    elif graphics == 1:
        ti_draw.set_color(*f)
        ti_draw.fill_rect(x,y,25,25)
        draw_block4x4(x,y,dirt4)
    elif graphics == 2:
        ti_draw.set_color(*g)
        ti_draw.fill_rect(x,y,25,25)
        draw_block(x,y, dirt)

def draw_stone(x,y, stone,stone4, graphics):
    ti_draw.set_color(*l)
    ti_draw.fill_rect(x,y,25,25)
    if graphics == 1:
        draw_block4x4(x,y,stone4)
    elif graphics == 2:
        draw_block(x,y, stone)
def draw_oak_log(x,y, oak_log, oak_log4, graphics):
    ti_draw.set_color(*q)
    ti_draw.fill_rect(x,y,25,25)
    if graphics == 1:
        draw_block4x4(x,y,oak_log4)
    elif graphics == 2:
        draw_block(x,y, oak_log)
def draw_oak_planks(x,y, oak_planks,oak_planks4,graphics):
    ti_draw.set_color(*w)
    ti_draw.fill_rect(x,y,25,25)
    if graphics == 1:
        draw_block4x4(x,y,oak_planks4)
    elif graphics == 2:
        draw_block(x,y, oak_planks)
def draw_oak_leaves(x,y, oak_leaves,oak_leaves4,graphics):
    if graphics == 0:
        ti_draw.set_color(*l4)
        ti_draw.fill_rect(x,y,25,25)
    else:
        ti_draw.set_color(*s)
        ti_draw.fill_rect(x,y,25,25)
        if graphics == 1:
            draw_block4x4(x,y,oak_leaves4)
        else:
            draw_block(x,y,oak_leaves)
def draw_glass(x,y, glass, glass4, graphics):
    if graphics == 0:
        ti_draw.set_color(*è)
        ti_draw.fill_rect(x,y,25,25)
        ti_draw.set_color(*s)
        ti_draw.fill_rect(x+6,y+6,13,13)
    if graphics == 1:
        ti_draw.set_color(*è)
        ti_draw.fill_rect(x,y,25,25)
        ti_draw.set_color(*s)
        ti_draw.fill_rect(x+6,y+6,13,13)
        draw_block4x4(x,y,glass4)
    elif graphics == 2:
        ti_draw.set_color(*s)
        ti_draw.fill_rect(x,y,25,25)
        draw_block(x,y, glass)
def draw_sand(x,y, sand, sand4, graphics):
    if graphics == 0:
        ti_draw.set_color(*s2)
        ti_draw.fill_rect(x,y,25,25)        
    if graphics == 1:
        ti_draw.set_color(*s2)
        ti_draw.fill_rect(x,y,25,25)
        draw_block4x4(x,y,sand4)
    elif graphics == 2:
        ti_draw.set_color(*s3)
        ti_draw.fill_rect(x,y,25,25)
        draw_block(x,y,sand)
def draw_iron(x,y, iron, iron4, graphics):
    if graphics == 0:
        ti_draw.set_color(*i3)
        ti_draw.fill_rect(x,y,25,25)
    if graphics == 1:
        ti_draw.set_color(*i1)
        ti_draw.fill_rect(x,y,25,25)
        draw_block4x4(x,y,iron4)
    elif graphics == 2:
        ti_draw.set_color(*i3)
        ti_draw.fill_rect(x,y,25,25)
        draw_block(x,y, iron)
def draw_water(x,y,water,water4,graphics):
    if graphics == 0:
        ti_draw.set_color(*w2)
        ti_draw.fill_rect(x,y,25,25)
    if graphics == 1:
        ti_draw.set_color(*w4)
        ti_draw.fill_rect(x,y,25,25)
        draw_block4x4(x,y,water4)
    elif graphics == 2:
        ti_draw.set_color(*w2)
        ti_draw.fill_rect(x,y,25,25)
        draw_block(x,y,water)


def draw_big_water(x,y,water):
    ti_draw.set_color(*w2)
    ti_draw.fill_rect(x,y,161,161)
    for i in water:
        if isinstance(i, list):
            if len(i) == 2:
                ti_draw.fill_rect((i[0]/3*20)+x,(i[1]/3*20)+y, 21, 21)
            else:
                if i[2] >= 0:
                    ti_draw.fill_rect((i[0]/3*20)+x,(i[1]/3*20)+y, i[2]*20+1, 21)
                else:
                    ti_draw.fill_rect((i[0]/3*20)+x,(i[1]/3*20)+y,21, abs(i[2])*20+1)
        else:
            ti_draw.set_color(*i)
#fancy worldgen
def change_height(height):
    if height <= 1:
        height += random.randint(0, 1)
    else:
        if height >= 6:
            height -= random.randint(0, 1)
        else:
            height += random.randint(-1, 1)
    return height

def can_generate_tree(world, tree):
    if world[tree+500].count(0) > 4:
        return True
    return False


def generate_trees(world):
    solved = False
    while not solved:
        trees = [random.randint(-498,499)]
        if can_generate_tree(world, trees[0]):
            solved = True
    for i in range(1,80):
        solved = False
        while not solved:
            trees.append(random.randint(-498,499))
            presolved = True
            for tree in range(len(trees)-1):
                    if abs(trees[i] - trees[tree]) <= 5:
                        presolved = False
            if can_generate_tree(world, trees[i]) and presolved:
                solved = True
            if not solved:
                trees.pop()
    return trees
def draw_trees(world, trees):
    for tree in trees:
        height = world[tree+500].count(0)
        for i in range(1,3):
            world[tree+500][height - i] = 4
        for i in range(3,5):
            world[tree+500][height - i] = 6
        for i in range(-1,2,2):
            world[tree-i+500][height-3] = 6
    return world
#010
#111
#020
#020


def draw_rects(almighty_list):
    check_2 = False
    border = 19
    ti_draw.set_color(*s)
    ti_draw.fill_rect(-1,-1,321,211)
    player_x = almighty_list[0][0]
    if almighty_list[0][1] == 0:
        border = 18
    elif almighty_list[0][2] == 0:
        check_2 = True
    for x in range(-6,7):
        counter = 17
        xlocal = 287+((x*24)-144)
        check = player_x+499+x - almighty_list[0][1]*20
        if check >= 0 and check <= border:
            chunk_to_use = 3
        else:
            check = player_x+499+x - almighty_list[0][2]*20
            chunk_to_use = 4
            if check_2 and check == 19:
                chunk_to_use = 3
                check = 0
        for block in almighty_list[0][chunk_to_use][check]:
            if block == 1:
                draw_grass(xlocal,counter,almighty_list[1],almighty_list[2],almighty_list[19])
            elif block == 2:
                draw_dirt(xlocal,counter,almighty_list[3],almighty_list[4],almighty_list[19])
            elif block == 3:
                draw_stone(xlocal,counter,almighty_list[5],almighty_list[6],almighty_list[19])
            elif block == 4:
                draw_oak_log(xlocal,counter,almighty_list[7],almighty_list[8],almighty_list[19])
            elif block == 5:
                draw_oak_planks(xlocal,counter,almighty_list[9],almighty_list[10],almighty_list[19])
            elif block == 6:
                draw_oak_leaves(xlocal,counter,almighty_list[11],almighty_list[12],almighty_list[19])
            elif block == 7:
                draw_glass(xlocal,counter,almighty_list[13],almighty_list[14],almighty_list[19])
            elif block == 8:
                draw_sand(xlocal,counter,almighty_list[15],almighty_list[16],almighty_list[19])
            elif block == 9:
                draw_water(xlocal,counter,almighty_list[17],almighty_list[18],almighty_list[19])
            counter += 24


def update_rects(almighty_list, dir):
    border_2 = 19
    border = 19
    player_x = almighty_list[0][0]
    if almighty_list[0][1] == 0:
        border = 18
    elif almighty_list[0][2] == 0:
        border_2 = 18
    for x in range(-6,7):
        use_next = False
        y = 0
        counter = 17
        xlocal = 287+((x*24)-144)
        check = player_x+499+x - almighty_list[0][1]*20
        if check > 0 and check < border:
            chunk_to_use = 3
        elif check == 0 or check == border:
            chunk_to_use = 3
            use_next = True
            use = 4
        else:
            check = player_x+499+x - almighty_list[0][2]*20
            chunk_to_use = 4
            if border_2 < check:
                chunk_to_use = 3
                use_next = True
                use = 4
                check = 0
            elif check == 0 or check == border_2:
                use_next = True
                use = 3
        for block in almighty_list[0][chunk_to_use][check]:
            draw = True
            if not use_next:
                if block == almighty_list[0][chunk_to_use][check+dir][y]:
                    draw = False
            elif check == 0:
                if dir == 1:
                    if block == almighty_list[0][use][1][y]:
                        draw = False
                else:
                    if block == almighty_list[0][use][len(almighty_list[0][use])-1][y]:
                        draw = False
            else:
                if dir == 1:
                    if block == almighty_list[0][use][0][y]:
                        draw = False
                else:
                    if block == almighty_list[0][chunk_to_use][check-1][y]:
                        draw = False    
            if draw:
                if block == 0:
                    ti_draw.set_color(*s)
                    ti_draw.fill_rect(xlocal,counter,25,25)
                elif block == 1:
                    draw_grass(xlocal,counter,almighty_list[1],almighty_list[2],almighty_list[19])
                elif block == 2:
                    draw_dirt(xlocal,counter,almighty_list[3],almighty_list[4],almighty_list[19])
                elif block == 3:
                    draw_stone(xlocal,counter,almighty_list[5],almighty_list[6],almighty_list[19])
                elif block == 4:
                    draw_oak_log(xlocal,counter,almighty_list[7],almighty_list[8],almighty_list[19])
                elif block == 5:
                    draw_oak_planks(xlocal,counter,almighty_list[9],almighty_list[10],almighty_list[19])
                elif block == 6:
                    draw_oak_leaves(xlocal,counter,almighty_list[11],almighty_list[12],almighty_list[19])
                elif block == 7:
                    draw_glass(xlocal,counter,almighty_list[13],almighty_list[14],almighty_list[19])
                elif block == 8:
                    draw_sand(xlocal,counter,almighty_list[15],almighty_list[16],almighty_list[19])
                elif block == 9:
                    draw_water(xlocal,counter,almighty_list[17],almighty_list[18],almighty_list[19])
            counter += 24
            y += 1

def draw_single_block(x,y,block,almighty_list):
    if block == 0:
        ti_draw.set_color(*s)
        ti_draw.fill_rect(x,y,25,25)
    elif block == 1:
        draw_grass(x,y,almighty_list[1],almighty_list[2],almighty_list[19])
    elif block == 2:
        draw_dirt(x,y,almighty_list[3],almighty_list[4],almighty_list[19])
    elif block == 3:
        draw_stone(x,y,almighty_list[5],almighty_list[6],almighty_list[19])
    elif block == 4:
        draw_oak_log(x,y,almighty_list[7],almighty_list[8],almighty_list[19])
    elif block == 5:
        draw_oak_planks(x,y,almighty_list[9],almighty_list[10],almighty_list[19])
    elif block == 6:
        draw_oak_leaves(x,y,almighty_list[11],almighty_list[12],almighty_list[19])
    elif block == 7:
        draw_glass(x,y,almighty_list[13],almighty_list[14],almighty_list[19])
    elif block == 8:
        draw_sand(x,y,almighty_list[15],almighty_list[16],almighty_list[19])
    elif block == 9:
        draw_water(x,y,almighty_list[17],almighty_list[18],almighty_list[19])



def draw_cursor(x,y):
    ti_draw.set_color(*black)
    ti_draw.fill_rect(x,y,10,4)
    ti_draw.fill_rect(x,y+3,4,7)
    ti_draw.fill_rect(x+15,y,10,4)
    ti_draw.fill_rect(x+21,y+3,4,7)
    ti_draw.fill_rect(x,y+21,10,4)
    ti_draw.fill_rect(x,y+15,4,7)
    ti_draw.fill_rect(x+15,y+21,10,4)
    ti_draw.fill_rect(x+21,y+15,4,7)


def update_menu(menu_select, prev):
    ti_draw.set_color(*white)
    if menu_select == 1:
        ti_draw.fill_rect(131,171,58,5)
        ti_draw.fill_rect(184,175,5,20)
        ti_draw.fill_rect(131,194,58,5)
        ti_draw.fill_rect(131,175,5,20)
    elif menu_select == 0:
        ti_draw.fill_rect(16,171,98,5)
        ti_draw.fill_rect(109,175,5,20)
        ti_draw.fill_rect(16,194,98,5)
        ti_draw.fill_rect(16,175,5,20)
    else:
        ti_draw.fill_rect(206,171,98,5)
        ti_draw.fill_rect(299,175,5,20)
        ti_draw.fill_rect(206,194,98,5)
        ti_draw.fill_rect(206,175,5,20)
    ti_draw.set_color(*dark_sky)
    if prev == 1:
        ti_draw.fill_rect(131,171,58,5)
        ti_draw.fill_rect(184,175,5,20)
        ti_draw.fill_rect(131,194,58,5)
        ti_draw.fill_rect(131,175,5,20)
    elif prev == 0:
        ti_draw.fill_rect(16,171,98,5)
        ti_draw.fill_rect(109,175,5,20)
        ti_draw.fill_rect(16,194,98,5)
        ti_draw.fill_rect(16,175,5,20)
    else:
        ti_draw.fill_rect(206,171,98,5)
        ti_draw.fill_rect(299,175,5,20)
        ti_draw.fill_rect(206,194,98,5)
        ti_draw.fill_rect(206,175,5,20)
def tp():
    finished = False
    while not finished:
        try:
            player_x = int(input("Where do you want to go(-490 to 490): "))
            if player_x > -491 and player_x < 491:
                finished = True
            else:
                print("Wrong number")
        except:
            print("Wrong input")
    return player_x
#init/create world
world = can_load_world("MCWD0")
if world is not None:
    print("Loading world...")
    world = trans_for_use()
else:
    print("Creating your world...")
    player_x = 0
    world = [0]
    new_world = True
    for i in range(-499,500):
        chunk = []
        height = change_height(height)
        for air in range(8-height):
            chunk.append(0)
        chunk.append(1)
        if 8-len(chunk) > 2:
            for DIRT in range(2):
                chunk.append(2)
            for STONE in range(8-len(chunk)):
                chunk.append(3)
        else:
            for DIRT in range(8-len(chunk)):
                chunk.append(2)
        world.append(chunk)
    print("Generating trees")
    trees = generate_trees(world)
    world = draw_trees(world, trees)
    print("Saving")
    world = trans_for_save(world)
    print("Doing something")
    for i in range(10):
        saving = "MCWD"
        saving += str(i)
        saved = False
        while not saved:
            saved = save_world(world[i], saving)
            if not saved:
                time.sleep(3)
    print("Saved!!")
    world = trans_for_use()
player_x = world[0]

almighty_list = [world,grass,grass4,dirt,dirt4,stone,stone4,oak_log,oak_log4,oak_planks,oak_planks4,oak_leaves,oak_leaves4,glass,glass4,sand,sand4,water,water4,graphics]

#Start!
while True:
    if draw_menu:
        draw_big_water(-1,-1,water)
        draw_big_water(159,-1,water)
        ti_draw.set_color(*dark_sky)
        ti_draw.fill_rect(-1,159,321,51)
        ti_draw.set_color(*white)
        ti_draw.fill_rect(131,171,58,28)
        ti_draw.set_color(*menu_color)
        ti_draw.fill_rect(20,175,90,20)
        ti_draw.fill_rect(135,175,50,20)
        ti_draw.fill_rect(210,175,90,20)
        ti_draw.set_color(*white)
        ti_draw.draw_text(25,196,"Tutorial")
        ti_draw.draw_text(140,196,"Play")
        ti_draw.draw_text(218,196,"Nothing")
        draw_menu = False
    k = ti_system.get_key(1)
    if k == 45:
        break
    elif k == 105:
        if menu_select == 1:
            game = True
            draw_rects(almighty_list)
            break
        elif menu_select == 0:
            menu_wait = True
            while menu_wait:
                draw_menu = True
                ti_draw.clear()
                ti_draw.draw_text(10,20,"Welcome to Minecraft in TI")
                ti_draw.draw_text(10,40,"Press clear to go back")
                ti_draw.draw_text(10,60,"Use the arrows to move")
                ti_draw.draw_text(10,80,"Toolbox:")
                ti_draw.draw_text(10,100,"0-2, set graphics:")
                ti_draw.draw_text(10,120,"0: one color")
                ti_draw.draw_text(10,140,"1:4x4")
                ti_draw.draw_text(10,160,"2:8x8(takes a long time)")
                ti_draw.draw_text(10,180,"Enter for next page")
                waitkey = ti_system.get_key(1)
                if k == 45:
                    break
                elif k == 105:
                    ti_draw.clear()
                    ti_draw.draw_text(10,20,"3: change time(night/day)")
                    ti_draw.draw_text(10,40,"4: tp(enter coodrinate and press enter")
                    ti_draw.draw_text(10,60, "5: Build:")
                    ti_draw.draw_text(10,80,"Arrows to move")
                    ti_draw.draw_text(10,100,"0-9 to change block")
                    ti_draw.draw_text(10,120,"Enter to build")
                    ti_draw.draw_text(10,140,"Clear to stop")
                    ti_draw.draw_text(10,160,"Press any key to get back")
                    waitkey = ti_system.get_key(1)
                    menu_wait = False
        else:
            ti_draw.clear()
            rand = random.randint(0,9)
            for x in range(-1,320, 24):
                for y in range(-1, 210, 24):
                    if rand == 0:
                        draw_iron(x,y,iron,None,2)
                    elif rand == 1:
                        draw_grass(x,y,grass,None,2)
                    elif rand == 2:
                        draw_dirt(x,y,dirt,None,2)
                    elif rand == 3:
                        draw_stone(x,y,stone,None,2)
                    elif rand == 4:
                        draw_oak_log(x,y,oak_log,None,2)
                    elif rand == 5:
                        draw_oak_planks(x,y,oak_planks,None,2)
                    elif rand == 6:
                        draw_oak_leaves(x,y,oak_leaves,None,2)
                    elif rand == 7:
                        draw_glass(x,y,glass,None,2)
                    elif rand == 8:
                        draw_sand(x,y,sand,None,2)
                    else:
                        draw_water(x,y,water,None,2)
            nothing = ti_system.get_key(1)
            draw_menu = True
            menu_select = 1
            nothing = None
    elif k == 26:
        if menu_select < 2:
            update_menu(menu_select+1,menu_select)
            menu_select += 1
            
    elif k == 24:
        if menu_select > 0:
            update_menu(menu_select-1,menu_select)
            menu_select -= 1


while game:
    k = ti_system.get_key(1)
    if k == 45:
        save_chunk(world[3],world[1])
        save_chunk(world[4],world[2])
        save_player_x(player_x)
        ti_draw.clear()
        game = False
        break
    elif k == 26:
        if player_x != 493:
            player_x += 1
            world[0] = player_x
            if world[1]>world[2]:
                if is_bordering_chunk(player_x, True, world[1]):
                    save_chunk(world[4], world[2])
                    world[2] = world[1]+1
                    world[4] = check_and_load_chunk(world[2])
            else:
                if is_bordering_chunk(player_x, True, world[2]):
                    save_chunk(world[3], world[1])
                    world[1] = world[2]+1
                    world[3] = check_and_load_chunk(world[1])
            almighty_list[0] = world
            update_rects(almighty_list, -1)
            if world_border:
                ti_draw.set_color(*s)
                ti_draw.fill_rect(23,0,280,18)
                world_border = False
        else:
            ti_draw.set_color(0,0,0)
            ti_draw.draw_text(24,20,"You reached the world border")
            world_border = True
    elif k == 24:
        if player_x != -493:
            player_x -= 1
            world[0] = player_x
            if world[1]<world[2]:
                if is_bordering_chunk(player_x, False, world[1]):
                    save_chunk(world[4], world[2])
                    world[2] = world[1]-1
                    world[4] = check_and_load_chunk(world[2])
            else:
                if is_bordering_chunk(player_x, False, world[2]):
                    save_chunk(world[3], world[1])
                    world[1] = world[2]-1
                    world[3] = check_and_load_chunk(world[1])
            almighty_list[0] = world
            update_rects(almighty_list, 1)
            if world_border:
                ti_draw.set_color(*s)
                ti_draw.fill_rect(23,0,280,18)
                world_border = False
        else:
            ti_draw.set_color(0,0,0)
            ti_draw.draw_text(24,20,"You reached the world border")
            world_border = True
    elif k == 83:
        building = True
        xy_list = [7,4]
        xy_list.append(is_in_chunk(player_x+xy_list[0]-7, world[1],world[2]))
        x_draw = (xy_list[0]-1)*24-1
        y_draw = 24*xy_list[1]+17
        while building:
            draw_cursor(x_draw,y_draw)
            k = ti_system.get_key(1)
            if k == 45:
                building = False
                draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]],almighty_list)
            elif k == 26:
                if xy_list[0] != 13:
                    draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]],almighty_list)
                    xy_list[0] += 1
                    xy_list[2] = is_in_chunk(player_x+xy_list[0]-7, world[1],world[2])
                    x_draw += 24
                    draw_cursor(x_draw,y_draw)
            elif k == 24:
                if xy_list[0] != 1:
                    draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]],almighty_list)
                    xy_list[0] -= 1
                    xy_list[2] = is_in_chunk(player_x+xy_list[0]-7, world[1],world[2])
                    x_draw -= 24
                    draw_cursor(x_draw,y_draw)
            elif k == 25:
                if xy_list[1] != 0:
                    draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]],almighty_list)
                    xy_list[1] -= 1
                    y_draw -= 24
                    draw_cursor(x_draw,y_draw)
            elif k == 34:
                if xy_list[1] != 7:
                    draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]],almighty_list)
                    xy_list[1] += 1
                    y_draw += 24
                    draw_cursor(x_draw,y_draw)
            else:
                for key in key_list:
                    if k == key:
                        world[xy_list[2][0]][xy_list[2][1]][xy_list[1]] = key_list.index(key)
                        draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]],almighty_list)
    elif k == 102:
        if graphics != 0:
            graphics = 0
            almighty_list[19] = graphics
            draw_rects(almighty_list)
    elif k == 92:
        if graphics != 1:
            graphics = 1
            almighty_list[19] = graphics
            draw_rects(almighty_list)
    elif k == 93:
        if graphics != 2:
            graphics = 2
            almighty_list[19] = graphics
            draw_rects(almighty_list)
    elif k == 94:
        if s == light_sky:
            s = dark_sky
        else:
            s = light_sky
        draw_rects(almighty_list)
    elif k == 82:
        player_x = tp()
        world = trans_for_use(player_x)
        almighty_list[0] = world
        draw_rects(almighty_list)
print("Console: Info: Program stopped succesfully")