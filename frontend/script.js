const breed = document.getElementById("breed");
const submitButton = document.getElementById("submit");
const resultImage = document.getElementById("image");

submitButton.addEventListener("click", function(){
   const text = breed.value;
   let url = `http://127.0.0.1:8000/breed?breed=${text}`
   if (!text) {
       url = `http://127.0.0.1:8000/random`
       console.log(url)
   }
   fetch(url)
    .then(response => response.json())
    .then(data => {
        resultImage.src = data.message;
    });
});