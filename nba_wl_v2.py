#entirely based on user input ----> v3 will have data scraping from league sites/internet

class Sport:
    def __init__(self,w,l):
        self.w = w
        self.l = l
        self.games = 0
        self.d = 0  #for leagues with draws that are important to standings
    def on_pace(self):
        total = self.w + self.l
        if not(total>=0 and total<=self.games):
            print("The record input is not a possible record")
            return
        win_per = self.w/total
        
        wins = round(win_per * self.games)
        loss = round((1-win_per)*self.games)
        
        return print("On pace for" , wins, "wins\nOn pace for", loss, "losses")
    
class Goal(Sport): #could be more complex with draw and non-draw goal based sports, but only want to work with 1 level of inheritance for simplicity
    def __init__(self,w,l,g):
        super().__init__(w, l)
        self.g = g
        self.p_w = 0
        self.p_d = 0                #most attributes used to determine the points system in leagues that have goals
        self.p_lot = 0 #points_lossOT
        self.otl = 0
    def on_pace_goals(self): 
        Sport.on_pace(self)
        goals = round((self.g/(self.w+self.l)) * self.games)
        points = round(((self.p_w*self.w + self.p_lot*self.otl + self.p_d*self.d)/(self.w+self.l+self.d))*self.games)
        return print("And on pace for", goals, "goals", "for a total of", points, "points")
        
class NBA(Sport):
    def __init__(self, w,l):
        super().__init__(w,l)
        self.games = 82


class MLB(Sport):
    def __init__(self,w,l):
        super().__init__(w,l)
        self.games = 162

class NFL(Sport):
    def __init__(self,w,l):
        super().__init__(w,l)
        self.games = 17

class NHL(Goal): #2 points win, one point OT loss 
    def __init__(self,w,l,otl, g): 
        super().__init__(w,l,g)
        self.games = 82
        self.otl = otl
        self.p_w = 2
        self.p_lot = 1
        

class MLS(Goal): #3 points for win, 1 point tie
    def __init__(self,w,l,d,g): 
        super().__init__(w, l, g)
        self.games = 34
        self.d = d
        self.p_w = 3
        self.p_d = 1
    def draw_pace(self):  #find another way to implement if there is another league that relies on draws
        total = self.w + self.l + self.d
        if not(total>=0 and total<=self.games):
            print("The record input is not a possible record")
            return
        win_per = self.w/total
        
        wins = round(win_per * self.games)
        
        loss = round((self.l/total)*self.games)
        draws = round((self.d/total)*self.games)
        
        goals = round((self.g/(self.w+self.l)) * self.games)
        points = round(((self.p_w*self.w + self.p_lot*self.otl + self.p_d*self.d)/(self.w+self.l+self.d))*self.games)
        return print("On pace for" , wins, "wins\nOn pace for", loss, "losses\nOn pace for",draws,
                     "draws\nAnd on pace for", goals, "goals", "for a total of", points, "points")

league = input("Enter the league: ")    #can make entire section less verbose function calls
league = league.upper()
if league == "NBA":
    wins = int(input("Enter the number of wins: "))
    losses = int(input("Enter the number of losses: "))  
    nba = NBA(wins,losses)
    nba.on_pace()
elif league == "MLB":
    wins = int(input("Enter the number of wins: "))
    losses = int(input("Enter the number of losses: "))  
    mlb = MLB(wins,losses)
    mlb.on_pace()
elif league == "NFL":
    wins = int(input("Enter the number of wins: "))
    losses = int(input("Enter the number of losses: "))  
    nfl = NFL(wins,losses)
    nfl.on_pace()
elif league == "NHL":
    wins = int(input("Enter the number of wins: "))
    losses = int(input("Enter the number of losses: "))  
    otl = int(input("Enter the number of OT losses: "))
    goals = int(input("Enter the number of goals: "))
    nhl = NHL(wins,losses,otl,goals)
    nhl.on_pace_goals()
elif league == "MLS":
    wins = int(input("Enter the number of wins: "))
    losses = int(input("Enter the number of losses: "))  
    draws = int(input("Enter the number of draws: "))  
    goals = int(input("Enter the number of goals: "))
    mls = MLS(wins,losses,draws,goals)
    mls.draw_pace()
else:
    print("This is not a valid league.")
