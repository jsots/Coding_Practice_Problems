function queryParams(str) {
    let ans = {}
    let end = str.length
    let key = ''
    let value = ''
    let questionMarkIndex = str.indexOf("?")
    let fullQueryParam = str.substring(questionMarkIndex+1,end)
    let equalSignIndex = fullQueryParam.indexOf("=")
  
    key = fullQueryParam.substring(0, equalSignIndex)
    let endParam = fullQueryParam.length
  
    let andIndex = fullQueryParam.indexOf("&")
    value = fullQueryParam.substring(equalSignIndex + 1, andIndex)
    let remainingQueryParam = fullQueryParam.substring(andIndex+1, end)
    console.log(remainingQueryParam);
  
  
    // const urlWithMultipleParams = "https://app.coderpad.io/EF37JADM/interview?language=javascript&user=evan"
    
    // &user=evan&blue=blah
    // &blue=blah
    // ''
  
    while (remainingQueryParam) {
      let newAndIndex = remainingQueryParam.indexOf("&")
      let newEqualSignIndex = remainingQueryParam.indexOf("=")
      key = remainingQueryParam.substring(0, newEqualSignIndex)
      if (newAndIndex) {
        value = remainingQueryParam.substring(newEqualSignIndex+1, newAndIndex)
      } else {
        value = remainingQueryParam.substring(newEqualSignIndex+1, remainingQueryParam.length)
      }
      ans[key] = value
      console.log(key)
      console.log(value)
      remainingQueryParam = remainingQueryParam.substring(newAndIndex, end)
    }
  
    return ans
  }