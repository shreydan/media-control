console.log("damn");

function clickTest() {
  fetch(
    "/test?" +
      new URLSearchParams({
        command: "lol",
      })
  )
    .then((response) => response.json())
    .then((data) => console.log(data));
}

// const test_btn = document.getElementById('click');
// test_btn.addEventListener('click', () => {
//   console.log('button was clicked');
//   clickTest();
// })