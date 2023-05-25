function tournamentWinner (competitions, results) {
    let max
    let winners = {}
    let twinner
    for (let i=0; i<competitions.length; i++){
      if (results[i] === 0) {
         winners[competitions[i][1]] = (winners[competitions[i][1]] || 0) + 3;
      } else {
         winners[competitions[i][0]] = (winners[competitions[i][0]] || 0) + 3;
      }
    }
      max = Math.max(...Object.values(winners));
      twinner = Object.keys(winners).find(twinner => winners[twinner] === max)
    return twinner
  }
  
  comp = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
  res = [0, 0, 1]
  console.log(tournamentWinner(comp, res))