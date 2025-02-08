#Rule: if a number is divisibe by 9 then, sum of its digits is also divisible by 9, and vice versa.
def RepAddDigits(n):
  if n == 0: #if input is 0 return 0
    return 0

if n % 9 == 0: #in case remainder comes 9 only, then return 9
  return 9

return n % 9 #returns sum of sum of digits (shall be single digit)
