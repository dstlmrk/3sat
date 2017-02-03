class Sat(object):

    def __init__(self, file):
        """Read DIMACS CNF format"""
        self.clauses = []
        for line in file:
            if line.startswith('c'):
                continue
            elif line.startswith('p'):
                meta_data = line.split()
                self.variables_count = int(meta_data[2])
                self.clauses_count = int(meta_data[3])
            elif line.startswith('w'):
                self.weights = []
                self.total_weight = 0
                for var in line.split()[1:]:
                    self.total_weight += int(var)
                    self.weights.append(int(var))
            else:
                clause = []
                for var in line.split()[:-1]:
                    clause.append(int(var))
                # because of invalid row
                if len(clause) == 3:
                    self.clauses.append(clause)

    def get_ratios(self, configuration):
        satisfied_count = 0
        for clause in self.clauses:
            # print(Sat.is_satisfied(clause, configuration))
            if Sat.is_satisfied(clause, configuration):
                satisfied_count += 1

        c = float(satisfied_count) / self.clauses_count
        w = float(self.get_weight(configuration)) / self.total_weight
        return c, w

    @staticmethod
    def is_satisfied(clause, configuration):
        for x in clause:
            if (x > 0 and configuration[abs(x)-1]) or (x < 0 and not configuration[abs(x)-1]):
                return True
        return False

    def get_weight(self, configuration):
        weight_usage = 0
        for idx, val in enumerate(configuration):
            if val:
                weight_usage += self.weights[idx]
        return weight_usage
