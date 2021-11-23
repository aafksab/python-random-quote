import random
import argparse

parser = argparse.ArgumentParser(description='Number of quotes to return')
parser.add_argument('--number', dest='number', type=int, help='Number of quotes to return')
args = parser.parse_args()
number = args.number

def primary(number):
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) -1

  for n in range(number):
    rnd = random.randint(0,last)
    print(quotes[rnd], end="")

if __name__== "__main__":
  primary(number)
