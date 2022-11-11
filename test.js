var x = 'LVIII'

romanValues = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  };

    for (char in x){
        console.log(x[char]);
        console.log(romanValues[char])
    }