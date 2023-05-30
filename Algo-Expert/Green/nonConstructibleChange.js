function nonConstructibleChange(coins) {
    // Write your code here.
    let constructibleChange = 0
    coins.sort(function(a, b){return a - b})
    for (let i = 0; i<coins.length; i++) {
      if (coins[i] > constructibleChange+1) {
        return constructibleChange+1
      } else {
        constructibleChange += coins[i]
      }
    }
    return constructibleChange+1;
}