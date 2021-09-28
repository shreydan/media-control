console.log("remote is active on network");
console.log('Issues/Help: https://github.com/shreydan/media-control');

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



const control_buttons = [
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


// remote mode
var mode = 'YOUTUBE' // YOUTUBE, NORMAL
const youtube_controls = document.getElementById('youtube-mode-active');


function toggle_remote_mode() {

  // switch betwen normal and youtube control mode + required CSS changes

  if (mode === 'YOUTUBE') {
    mode = 'NORMAL';
    youtube_controls.style.visibility = 'hidden';
    mode_change_button.style.backgroundColor = '#82B9EB';
    mode_change_button.innerText = 'Universal';
    play_pause.style.backgroundColor = '#82B9EB';
  }
  else if (mode === 'NORMAL') {
    mode = 'YOUTUBE';
    youtube_controls.style.visibility = 'visible';
    mode_change_button.style.backgroundColor = '#EB8282';
    mode_change_button.innerText = 'Youtube';
    play_pause.style.backgroundColor = '#EB8282';
  }
}

// event listener to toggle control mode 
mode_change_button.addEventListener('click', () => {
  toggle_remote_mode();
})



// add event listener to each control button
control_buttons.forEach((button) => {
  button.addEventListener('click', () => {
    console.log(button);
    send_remote_button(button)
  });
})


function send_remote_button(button) {

  // do a POST request when button is pressed to /control endpoint
  
  const data = {
    button_id: button.id,
    mode: mode
  };

  fetch("/control/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
}
