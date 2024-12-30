import random

class Gym:
    def __init__(self):
        self.dumbbells = [i for i in range(10,39) if i%2 == 0]
        self.dumbbell_rack = {}
        self.restart_the_day()

    def restart_the_day(self):
        self.dumbbell_rack = {i:i for i in self.dumbbells}

    def list_dumbbells(self):
        return [i for i in self.dumbbell_rack.values() if i != 0]

    def list_empty_slots(self):
        return [i for i, j in self.dumbbell_rack.items() if j == 0]

    def get_dumbbell(self, dumbbell):
        dumbbell_position = list(i for i in self.dumbbell_rack.values()).index(dumbbell)
        dumbell_key = list(i for i in self.dumbbell_rack.keys())[dumbbell_position]
        self.dumbbell_rack[dumbell_key] = 0
        return dumbbell

    def return_dumbbell(self, position, dumbbell):
        self.dumbbell_rack[position] = dumbbell

    def measure_chaos(self):
        chaotic_positions = 0
        for i,j in self.dumbbell_rack.items():
            if i != j:
                chaotic_positions += 1
        return chaotic_positions / len(self.dumbbell_rack)

class User:
    def __init__(self, type, gym):
        self.type = type   #[1] Normal / [2] Caótico
        self.gym = gym
        self.dumbbell = 0

    def start_workout(self):
        list_dumbbells = self.gym.list_dumbbells()
        self.dumbbell = random.choice(list_dumbbells)
        self.gym.get_dumbbell(self.dumbbell)

    def finish_workout(self):
        empty_slots = self.gym.list_empty_slots()

        if self.type == 1:
            if self.dumbbell in empty_slots:
                self.gym.return_dumbbell(self.dumbbell, self.dumbbell)
            else:
                position = random.choice(empty_slots)
                self.gym.return_dumbbell(position, self.dumbbell)

        if self.type == 2:
            position = random.choice(empty_slots)
            self.gym.return_dumbbell(position, self.dumbbell)

        self.dumbbell = 0

gym = Gym()
users = [User(1, gym) for i in range(9)] # Total de usuários normais
users += [User(2, gym) for i in range(1)] # Total de usuários caóticos

gym.restart_the_day()
for i in range(10): # Total de treino
    random.shuffle(users)
    for user in users:
        user.start_workout()
    for user in users:
        user.finish_workout()

print(f'{round(gym.measure_chaos()*100,2)} %')