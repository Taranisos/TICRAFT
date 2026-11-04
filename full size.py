import ti_draw, time, random, ti_system, math, ti_graphics

#varables
height = 4
game = False
building = False
new_world = False
chunk = []
world_border = False
key_list=[102,92,93,94,82,83,84,72,73,74]
menu_select = 1
draw_menu = True



#colors
black=(0,0,0)
menu_color=(111,110,113)
dark_sky=(5,23,52)
light_sky=(130, 172, 255)
s=light_sky #sky
white=(255,255,255)









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
        if player_x -(chunk_to_load*20-499) < 10 or chunk_to_load == 49:
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
    player_x -= (chunk*20)-499
    player_x = str(player_x)
    if chunk == 0:
            return False
    elif dir:
        if player_x == "10":
            return True
    else:
        if player_x == "8":
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








def draw_grass(x,y):
    ti_graphics.drawImage("MCGRS",x,y)

def draw_dirt(x,y):
    ti_graphics.drawImage("MCDRT",x,y)

def draw_stone(x,y):
    ti_graphics.drawImage("MCSTN",x,y)

def draw_oak_log(x,y):
    ti_graphics.drawImage("MCOKL",x,y)

def draw_oak_planks(x,y):
    ti_graphics.drawImage("MCOKP",x,y)

def draw_oak_leaves(x,y):
    ti_draw.set_color(*s)
    ti_draw.fill_rect(x-1,y-31,17,17)
    ti_graphics.drawImage("MCOKV",x,y)

def draw_glass(x,y):
    ti_draw.set_color(*s)
    ti_draw.fill_rect(x-1,y-31,17,17)
    ti_graphics.drawImage("MCGLS",x,y)

def draw_sand(x,y):
    ti_graphics.drawImage("MCSND",x,y)

def draw_water(x,y):
    ti_graphics.drawImage("MCWTR",x,y)




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


def draw_rects(world):
    check_2 = False
    border = 19
    ti_draw.set_color(*s)
    ti_draw.fill_rect(-1,-1,321,211)
    player_x = world[0]
    if world[1] == 0:
        border = 18
    elif world[2] == 0:
        check_2 = True
    for x in range(-9,11):
        counter = 112
        xlocal = 144+(x*16)
        check = player_x+499+x - world[1]*20
        if check >= 0 and check <= border:
            chunk_to_use = 3
        else:
            check = player_x+499+x - world[2]*20
            chunk_to_use = 4
            if check_2 and check == 19:
                chunk_to_use = 3
                check = 0
        for block in world[chunk_to_use][check]:
            draw_single_block(xlocal,counter,block)
            counter += 16


def update_rects(world, dir):
    border_2 = 19
    border = 19
    player_x = world[0]
    if world[1] == 0:
        border = 18
    elif world[2] == 0:
        border_2 = 18
    for x in range(-9,11):
        use_next = False
        y = 0
        counter = 112
        xlocal = 144+(x*16)
        check = player_x+499+x - (world[1]*20)
        if check > 0 and check < border:
            chunk_to_use = 3
        elif check == 0 or check == border:
            chunk_to_use = 3
            use_next = True
            use = 4
        else:
            check = player_x+499+x - (world[2]*20)
            chunk_to_use = 4
            if border_2 < check:
                chunk_to_use = 3
                use_next = True
                use = 4
                check = 0
            elif check == 0 or check == border_2:
                use_next = True
                use = 3
        for block in world[chunk_to_use][check]:
            draw = True
            if not use_next:
                if block == world[chunk_to_use][check+dir][y]:
                    draw = False
            elif check == 0:
                if dir == 1:
                    if block == world[chunk_to_use][1][y]:
                        draw = False
                else:
                    if block == world[use][len(world[use])-1][y]:
                        draw = False
            else:
                if dir == 1:
                    if block == world[use][0][y]:
                        draw = False
                else:
                    if block == world[chunk_to_use][check-1][y]:
                        draw = False
            if draw:
                draw_single_block(xlocal,counter,block)
            counter += 16
            y += 1

def draw_single_block(x,y,block):
    if block == 0:
        ti_draw.set_color(*s)
        ti_draw.fill_rect(x-1,y-31,17,17)
    elif block == 1:
        draw_grass(x,y)
    elif block == 2:
        draw_dirt(x,y)
    elif block == 3:
        draw_stone(x,y)
    elif block == 4:
        draw_oak_log(x,y)
    elif block == 5:
        draw_oak_planks(x,y)
    elif block == 6:
        draw_oak_leaves(x,y)
    elif block == 7:
        draw_glass(x,y)
    elif block == 8:
        draw_sand(x,y)
    elif block == 9:
        draw_water(x,y)



def draw_cursor(x,y):
    ti_draw.set_color(*black)
    ti_draw.fill_rect(x,y,7,3)
    ti_draw.fill_rect(x,y+2,3,5)
    ti_draw.fill_rect(x+10,y,7,3)
    ti_draw.fill_rect(x+14,y+2,3,5)
    ti_draw.fill_rect(x,y+14,7,3)
    ti_draw.fill_rect(x,y+10,3,5)
    ti_draw.fill_rect(x+10,y+14,5,3)
    ti_draw.fill_rect(x+14,y+10,3,7)


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
            player_x = int(input("Where do you want to go(-485 to 485): "))
            if player_x > -486 and player_x < 486:
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


#Start!
while True:
    if draw_menu:
        #draw_big_water(-1,-1,water)
        #draw_big_water(159,-1,water)
        ti_draw.set_color(*dark_sky)
        ti_draw.fill_rect(-1,158,321,52)
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
            draw_rects(world)
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
                ti_draw.draw_text(10,100,"0: tp(enter coodrinate and press enter")
                ti_draw.draw_text(10,120,"2: change time(night/day)")
                ti_draw.draw_text(10,140,"Enter for next page")
                waitkey = ti_system.get_key(1)
                if k == 45:
                    break
                elif k == 105:
                    ti_draw.clear()
                    ti_draw.draw_text(10,20,"5: Build:")
                    ti_draw.draw_text(10,40,"Arrows to move")
                    ti_draw.draw_text(10,60, "0-9 to change block")
                    ti_draw.draw_text(10,80,"Enter to build")
                    ti_draw.draw_text(10,100,"Clear to stop")
                    ti_draw.draw_text(10,120,"Press any key to get back")
                    waitkey = ti_system.get_key(1)
                    menu_wait = False
                    menu_select = 1
        else:
            ti_draw.clear()
            rand = random.randint(0,8)
            for x in range(0,320, 16):
                for y in range(30, 240, 16):
                    if rand == 0:
                        draw_sand(x,y)
                    elif rand == 1:
                        draw_grass(x,y)
                    elif rand == 2:
                        draw_dirt(x,y)
                    elif rand == 3:
                        draw_stone(x,y)
                    elif rand == 4:
                        draw_oak_log(x,y)
                    elif rand == 5:
                        draw_oak_planks(x,y)
                    elif rand == 6:
                        draw_oak_leaves(x,y)
                    elif rand == 7:
                        draw_glass(x,y)
                    else:
                        draw_water(x,y)
            nothing = ti_system.get_key(1)
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
        if player_x != 489:
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
            world = world
            update_rects(world, -1)
            if world_border:
                ti_draw.set_color(*s)
                ti_draw.fill_rect(23,0,280,18)
                world_border = False
        else:
            ti_draw.set_color(0,0,0)
            ti_draw.draw_text(24,20,"You reached the world border")
            world_border = True
    elif k == 24:
        if player_x != -488:
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
            world = world
            update_rects(world, 1)
            if world_border:
                ti_draw.set_color(*s)
                ti_draw.fill_rect(23,0,280,18)
                world_border = False
        else:
            ti_draw.set_color(0,0,0)
            ti_draw.draw_text(24,20,"You reached the world border")
            world_border = True
    elif k == 92:
        building = True
        xy_list = [9,4]
        xy_list.append(is_in_chunk(player_x+xy_list[0]-9, world[1],world[2]))
        x_draw = 144
        y_draw = 176
        while building:
            draw_cursor(x_draw-1,y_draw-31)
            k = ti_system.get_key(1)
            if k == 45:
                building = False
                draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]])
            elif k == 26:
                if xy_list[0] != 19:
                    draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]])
                    xy_list[0] += 1
                    xy_list[2] = is_in_chunk(player_x+xy_list[0]-9, world[1],world[2])
                    x_draw += 16
                    draw_cursor(x_draw-1,y_draw-31)
            elif k == 24:
                if xy_list[0] != 0:
                    draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]])
                    xy_list[0] -= 1
                    xy_list[2] = is_in_chunk(player_x+xy_list[0]-9, world[1],world[2])
                    x_draw -= 16
                    draw_cursor(x_draw-1,y_draw-31)
            elif k == 25:
                if xy_list[1] != 0:
                    draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]])
                    xy_list[1] -= 1
                    y_draw -= 16
                    draw_cursor(x_draw-1,y_draw-31)
            elif k == 34:
                if xy_list[1] != 7:
                    draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]])
                    xy_list[1] += 1
                    y_draw += 16
                    draw_cursor(x_draw-1,y_draw-31)
            else:
                for key in key_list:
                    if k == key:
                        world[xy_list[2][0]][xy_list[2][1]][xy_list[1]] = key_list.index(key)
                        draw_single_block(x_draw,y_draw,world[xy_list[2][0]][xy_list[2][1]][xy_list[1]])
    elif k == 102:
        player_x = tp()
        world = trans_for_use(player_x)
        world = world
        draw_rects(world) 
    elif k == 93:
        if s == light_sky:
            s = dark_sky
        else:
            s = light_sky
        draw_rects(world)
print("Console: Info: Program stopped succesfully")