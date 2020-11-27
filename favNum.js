// https://remeeting.com/quiz/python_script.cgi
// https://remeeting.com/quiz/
// user: remeeting
// pw: ****

let requestOptions = {
  method: 'GET',
  redirect: 'follow'
};


// initial guess = 109
function guessFavNumber(guess=109) {
  
  let URL = `https://remeeting.com/quiz/python_script.cgi?number=${guess}`;

  // Make GET request to the URL endpoint above passing in guess as query param
  fetch(URL, requestOptions)
  
    // when promise is fulfilled, do code below
    .then(response => {
      
      // convert response obj to promise
      responsePromise = response.text();
      // console.log(responsePromise);
  
      // when promise is fulfilled, check if number is correct
      responsePromise.then(textResult => {
        // console.log(textResult);
        
        // if html text contains the word "Sorry", number is incorrect
        let isIncorrect = textResult.includes("Sorry");

        if (isIncorrect) {
          console.log(guess + " is incorrect!");

          // recursively/continuously make fetches until we get correct number
          // wait 10 seconds before making next call (incase there's rate limiting in place)
          setTimeout(guessFavNumber(guess + 1), 10000);

        } else {
          console.log(guess + " is CORRECT!!!!");
        }

        if (guess === 1000) return;   // exit if we hit 1000
      });
    })
    .catch(error => console.log('error', error));
}

guessFavNumber();


