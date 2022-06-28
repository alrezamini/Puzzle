class Solving_Puzzle():
    def __init__(self,ini_list,tar_list,pz_ln):
        self.ini_list = ini_list
        self.tar_list = tar_list
        self.pz_ln = int(pz_ln)
        self.puzzle_y = int(len(self.ini_list)) // int(self.pz_ln)
        self.temp_list = []
        self.ms_count = -1
        self.saved_nd = []

    def sort(self):
        ln = int(len(self.temp_list))
        for x in range(ln-1):
            for h in range(1,ln):
                if self.temp_list[h]["h"] <= self.temp_list[x]["h"]:
                    tmp = self.temp_list[h]
                    self.temp_list[h] = self.temp_list[x]
                    self.temp_list[x] = tmp
        return self.temp_list[0]

    def position_of_zero(self):
        temp = 0
        for x in range(int(len(self.ini_list))):
            if temp >= self.pz_ln:
                temp = 0
            if self.ini_list[x] == 0:
                return temp , x // self.pz_ln , x
            else:
                temp+=1
                continue

    def find(self,lst):
        flg = False
        for x in self.saved_nd:
            if x == lst:
                flg = True
        return flg


    def check_missing(self,lst):
        missing_count = 0
        cnt = 0
        for x in lst:
            if x != self.tar_list[cnt]:
                missing_count+=1
            cnt+=1
        return missing_count

    def check_condition(self,t1,t2):
        lst = self.ini_list.copy()
        lst[t1] = lst[t2]
        lst[t2] = 0
        if self.find(lst) != True:
            return False , lst
        else:
            return True , lst

    def change_zero_position(self,x,y,t):
        if x+1 < self.pz_ln:
            r = self.check_condition(t,t+1)
            if r[0] != True:
                self.temp_list.append({"lst":r[1],"direction":"R","h":self.check_missing(r[1])})

        if x-1 >= 0:
            r = self.check_condition(t,t-1)
            if r[0] != True:
                self.temp_list.append({"lst":r[1],"direction":"L","h":self.check_missing(r[1])})

        if y+1 < self.puzzle_y:
            r = self.check_condition(t,t+self.pz_ln)
            if r[0] != True:
                self.temp_list.append({"lst":r[1],"direction":"D","h":self.check_missing(r[1])})

        if y-1 >= 0:
            r = self.check_condition(t,t-self.pz_ln)
            if r[0] != True:
                self.temp_list.append({"lst":r[1],"direction":"U","h":self.check_missing(r[1])})

    def solve(self):
        try:
            dirct = ""
            self.saved_nd.append(self.ini_list)
            while self.tar_list != self.ini_list:
                zero_x , zero_y , t = self.position_of_zero()
                self.change_zero_position(zero_x,zero_y,t)
                srt = self.sort()
                self.ms_count = srt["h"]
                self.ini_list = srt["lst"]
                self.saved_nd.append(srt["lst"])
                dirct+="{} ".format(srt["direction"])
                self.temp_list = []
            print(dirct)
        except:
            print("no solution found")


puzzle_length = int(input())
initial_puzzle_list = list(map(int,input().split()))
target_puzzle_list = list(map(int,input().split()))

obj = Solving_Puzzle(initial_puzzle_list,target_puzzle_list,puzzle_length)
obj.solve()