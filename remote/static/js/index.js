console.log("damn");

// definition of all buttons of the remote control
const mode_change_button = document.getElementById("mode_change_button");

const volume_down = document.getElementById("volume_down");
const play_pause = document.getElementById("play_pause");
const volume_up = document.getElementById("volume_up");

const playlist_previous = document.getElementById("playlist_previous");
const playlist_next = document.getElementById("playlist_next");

const yt_fullscreen = document.getElementById("yt_fullscreen");
const yt_captions = document.getElementById("yt_captions");
const yt_rewind = document.getElementById("yt_rewind");
const yt_forward = document.getElementById("yt_forward");



const buttons = [
  mode_change_button,
  volume_down,
  play_pause,
  volume_up,
  playlist_previous,
  playlist_next,
  yt_fullscreen,
  yt_captions,
  yt_rewind,
  yt_forward
];


// add event listener to each button

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    console.log(button);
    send_remote_button(button)
  });
})

function send_remote_button(button) {

  // do a POST request when button is pressed to /control endpoint
  
  const data = {
    button_id: button.id,
  };

  fetch("/control/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
}
