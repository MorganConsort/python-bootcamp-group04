user_input = input("Please enter a list of numbers seperated by spaces: ")
scores = [float(x) for x in user_input.split()]

set = {
    "min"
    "max"
    "mean"
    "median"
}

def summary(scores):
    Smin, Smax, mean  = 1000, 0, 0
    n = len(scores)//2
    median = (scores[n] + scores[n+1])/2
    for i in scores:
        Smin = min(Smin, i)
        Smax = max(Smax, i)
        mean += i
    mean /= len(scores)
    result = dict(min = Smin, max = Smax, mean = mean, median = median)
    print(result)

if __name__ == "__main__":
    summary(scores)