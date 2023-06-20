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


  const parseQueryParams = (url) => {
    if (!url.includes('?')) {
      return {}
    }
    const ans = {}
    const paramString = url.split('?')[1]
    const entries = paramString.split('&');
    entries.forEach((entry) => {
      // the following line of code is equivalent to: 
      // key = entry.split('=')[0]; 
      // value = entry.split('=')[1];
      // it assumes there will be 2 values in the array.
      const [key, value] = entry.split('=');
      if (key in ans) {
          const currentEntry = ans[key]
  
          if (typeof currentEntry === 'string') {
            // just a string; make new array
            ans[key] = [currentEntry]
          }
  
          ans[key].push(value);
      } else {
        ans[key] = value;
      }
    });
  
    return ans;
  }

  const urlPlain = "https://app.coderpad.io/EF37JADM/interview"
const urlWithParam = "https://app.coderpad.io/EF37JADM/interview?language=javascript"
const urlWithMultipleParams = "https://app.coderpad.io/EF37JADM/interview?language=javascript&language=python&user=evan&language=english"
const malformedUrl = "https://app.coderpad.io/EF37JADM/interview?language==&&blah"