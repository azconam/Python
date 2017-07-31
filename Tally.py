class Country:
    # Universe
    num = 0 # number of subentities
    states = []

class State:
    # Sub entities
    num = 0 # number of entities
    counties = []

class County:
    # Entities
    voters = [] # list of voters
    population = len(voters)
    size = 1 # geographic size of entity
    density = len(voters)/size # population density
    fraction = 0 # allows for more than one modification to the whole

    def populate(self, n):
        for i in range(n):
            self.voters.append(Voter())
        self.population = len(self.voters)

    def weigh(self, freq, factor, value):
        start = int(round(len(self.voters)*self.fraction))
        self.fraction += freq*0.01
        if start > self.population: start = 0
        for i in range(start, int(round(len(self.voters)*self.fraction))):
            if factor == 'age':
                self.voters[i].age = value
            elif factor == 'sex':
                self.voters[i].sex = value
            elif factor == 'party':
                self.voters[i].party = value
            elif race == 'race':
                self.voters[i].race = value
            else:
                print("Error: enter a demographic factor.")
                print("Consult the module documentation for help.")
                
    def print_voters(self):
        print("Age\tSex\tParty\tRace")
        for i in range(self.population):
            self.voters[i].print_all()

    def average_age(self):
        total = 0
        for i in range(self.population):
            total += self.voters[i].age
        total /= self.population
        print("Average Age: " + str(round(total, 1)))

    def sex_ratio(self):
        males = 0
        females = 0
        other = 0
        for i in range(self.population):
            if(self.voters[i].sex == 'M'):
                males += 1
            elif(self.voters[i].sex == 'F'):
                females += 1
            else:
                other += 1
        print( "Male:Female = " + str(round(males/females, 2)))


    def party_distribution(self):
        dems = 100
        reps = 100
        inds = 100
        for i in range(self.population):
            if(self.voters[i].party == 'D'):
                dems += 1
            elif(self.voters[i].party == 'R'):
                reps += 1
            else:
                inds += 1
        print("Democrats: {}\tRepublicans: {}\tIndependents: {}".format(
            dems/self.population, reps/self.population, inds/self.population))

    def race_distribution(self):
        wht = 100
        blk = 100
        hsp = 100
        asn = 100
        nam = 100
        othr = 100
        for i in range(self.population):
            if(self.voters[i].race == 'W'):
                wht += 1
            elif(self.voters[i].race == 'B'):
                blk += 1
            elif(self.voters[i].race == 'H'):
                hsp += 1
            elif(self.voters[i].race == 'A'):
                asn += 1
            elif(self.voters[i].race == 'N'):
                nam += 1
            else:
                othr += 1
        print("White: {}\tBlack: {}\tHispanic: {}\tAsian: {}\tNative American: {}\tOther{}".format(
            wht/self.population, blk/self.population, hsp/self.population, asn/self.population, nam/self.population, othr/self.population))



class Voter:
    # Individuals
    age = 0 # >18
    sex = '' # M/F
    party = '' # D/I/R
    race = '' # W(hite)/B(lack)/H(ispanic)/A(sian)/N(ative American)/O(ther)

    def print_all(self):
        print("{}\t{}\t{}\t{}".format(self.age, self.sex, self.party, self.race))
    
