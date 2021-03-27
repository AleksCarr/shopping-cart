
let submitButton = document.querySelector('.submit-button');
let submitMessage = document.querySelector('h2');

const submitted = function(event) {
    alert('Transaction Has been proccessed')
}

submitButton.addEventListener('click', submitted);



