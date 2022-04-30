
# Online Python - IDE, Editor, Compiler, Interpreter
import random
import math

    
class LinearCongruentialGenerator:
    def __init__(self, a, c, mod):
        self.multiplier = a
        self.increment = c
        self.modulus = mod
        self.seed = 1
    
    def updateSeed(self):
        self.seed = int((self.multiplier * 1 * self.seed + self.increment) % self.modulus)
        
    def set_seed(self, seed):
        self.seed = seed
    
    def nextNumber(self):
        self.updateSeed()
        return float(self.seed / self.modulus)

class LeggedFibonacciGenerator:
    def updateSeed(self):
        self.a = 106
        self.c = 1283
        temp = LinearCongruentialGenerator(self.a, self.c, self.modulus)
        temp.set_seed(self.seed)
        for i in range(self.k):
            self.f.append(temp.nextNumber() * self.modulus)
            
    def __init__(self, j, k, mod, seed = 3):
        self.j = j
        self.k = k
        self.modulus = mod
        self.seed = seed
        self.count = 1
        self.f = []
        
        self.a = 106
        self.c = 1283
        temp = LinearCongruentialGenerator(self.a, self.c, self.modulus)
        temp.set_seed(self.seed)
        for i in range(self.k):
            self.f.append(temp.nextNumber() * self.modulus)
        
    def set_seed(self, seed):
        self.seed = seed
        self.count = 1
        updateSeed()
    
    def next_number(self):
        if self.count < k:
            res = float(self.f[self.count] / self.modulus)
            self.count += 1
            return res
        
        self.f[self.count % k] = (self.f[(self.count - self.j + self.k) % self.k] + self.f[(self.count) % self.k]) % self.modulus
        ans = self.f[self.count % self.k]
        self.count += 1
        return float(ans / self.modulus)
            
        
class ChiSquareTest:
    def __init__(self, n):
        self.n = n
    
    def result(self, sequence):
        freqeuncy = {}
        for i in sequence:
            if i * self.n not in freqeuncy.keys():
                freqeuncy[i * self.n] = 1
            else:
                freqeuncy[i * self.n] += 1
        ans = 0
        expected = float(len(sequence) / self.n)
        for i in range(self.n):
            if i not in freqeuncy.keys():
                freqeuncy[i] = 0
            ans += ((freqeuncy[i] - expected) * (freqeuncy[i] - expected)) / expected
        return ans

class KolmogorovSmirnovTest:
    def __init__(self, n):
        self.n = n
    M = 10
    def result(self, sequence):
        sequence.sort()
        for i in range(len(sequence)):
            sequence[i] *= self.n
        maxDeviation = float(0)
        minDeviation = float(0)
        
        for i in range(len(sequence)):
            if i != len(sequence) - 1 and sequence[i + 1] == sequence[i]:
                continue
            fn = float((i + 1) / len(sequence))
            fx = float((sequence[i] + 1) / self.n)
            pos_div = math.sqrt(self.n) * (fn - fx)
            neg_div = math.sqrt(self.n) * (fx - fn)
            
            maxDeviation = max(maxDeviation, pos_div)
            minDeviation = max(minDeviation, neg_div)
        maxDeviation /= self.M
        minDeviation /= 10 * self.M
        return [maxDeviation, minDeviation]

a = 106
c = 1283
mod1 = 6075
mod2 = 241
N = 1000

generatorLinear = LinearCongruentialGenerator(a, c, mod1)

j = 7
k = 10
generatorLegged = LeggedFibonacciGenerator(j, k, mod2)

linear_gen_output = []
legged_gen_output = []
for i in range(N):
    linear_gen_output.append(generatorLinear.nextNumber())
    legged_gen_output.append(generatorLegged.next_number())

chi_square_tester_linear = ChiSquareTest(mod1)
print("Chisqare test result for LinearCongruentialGenerator:", chi_square_tester_linear.result(linear_gen_output))

chi_square_tester_legged = ChiSquareTest(mod2)
print("Chisqare test result for LeggedFibonacciGenerator:", chi_square_tester_legged.result(legged_gen_output))

kolmogorov_tester_linear = KolmogorovSmirnovTest(mod1)
kolmogorov_tester_legged = KolmogorovSmirnovTest(mod2)
liner_kolmogorov_tester_result = kolmogorov_tester_linear.result(linear_gen_output)
print("KolmogorovSmirnovTest result for LinearCongruentialGenerator: k+=", liner_kolmogorov_tester_result[0]," and k-=", liner_kolmogorov_tester_result[1])

legged_kolmogorov_tester_result = kolmogorov_tester_legged.result(legged_gen_output)
print("KolmogorovSmirnovTest result for LeggedFibonacciGenerator: k+=", legged_kolmogorov_tester_result[0]," and k-=", legged_kolmogorov_tester_result[1])



		

    
    
    
    
    
    
    
    
    
    


