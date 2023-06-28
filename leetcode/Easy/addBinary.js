var addBinary = function(a, b) {
    let ans = [];
    let carry = 0;
    let output = "";
  
    // Pad the shorter binary string with leading zeros
    if (a.length < b.length) {
      a = a.padStart(b.length, "0");
    } else {
      b = b.padStart(a.length, "0");
    }
  
    // Perform binary addition
    for (let i = a.length - 1; i >= 0; i--) {
      let sum = Number(a[i]) + Number(b[i]) + carry;
      ans.push(sum % 2);
      carry = Math.floor(sum / 2);
    }
  
    // If there's still a carry at the end, add it to the result
    if (carry) {
      ans.push(carry);
    }
  
    // Reverse the result array and convert it to a string
    output = ans.reverse().join("");
  
    return output;
  };
  

  // Try comverting the strings into base 10 numbers and then adding them. Then you turn them back into binary.