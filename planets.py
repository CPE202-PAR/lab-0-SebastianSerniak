# Given earth weight and planet, returns weight on provided planet
# If string does not match a planet, raise ValueError
def weight_on_planets(pounds: float, planet: str) -> float:
   # write your code here
   if planet == 'Mars':
      p = pounds * 0.38
   elif planet == 'Jupiter':
      p = pounds * 2.34
   elif planet == 'Venus':
      p = pounds * 0.91
   else:
      raise ValueError('Oh no!')
   return p

if __name__ == '__main__':    # pragma: no cover
   pounds = float(input("What do you weigh on earth? "))
   print("\nOn Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds." +
          "\nOn Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds." +
         "\nOn Venus you would weigh", weight_on_planets(pounds, 'Venus'), "pounds.")
