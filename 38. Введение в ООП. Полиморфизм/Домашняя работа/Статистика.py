class MinStat:    def __init__(self):        self.min_list = []    def add_number(self, num):        self.min_list.append(num)    def result(self):        if len(self.min_list) != 0:            return(min(self.min_list))        else:            return Noneclass MaxStat:    def __init__(self):        self.max_list = []    def add_number(self, num):        self.max_list.append(num)    def result(self):        if self.max_list != []:            return(max(self.max_list))        else:            return Noneclass AverageStat:    def __init__(self):        self.average_list = []    def add_number(self, num):        self.average_list.append(num)    def result(self):        if len(self.average_list) != 0:            return(sum(self.average_list) / len(self.average_list))        else:            return None