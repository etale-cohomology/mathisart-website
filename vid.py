#!/usr/bin/env py
'''
t ffmpeg  -i vid0000_plandemic.mkv  -c:v copy  -c:a libopus -ar 48000 -ac 2  -y vid0000_plandemic.mp4

t ffmpeg  -ss 0 -to 3852  -i vid0002_the_video_for_which_yt_deleted_anthony_patchs_channel.mp4  -c copy  -y vid0002_the_video_for_which_yt_deleted_anthony_patchs_channel_part00.mp4

t convert  alberto1_01.jpg  -sampling-factor 4:2:0 -strip -quality 85 -interlace JPEG -colorspace RGB  alberto1_02.jpg

--------------------------------------------------------------------------------------------------------------------------------
<video id='vid00' controls><source src='vid0000_plandemic.mp4' type='video/mp4'></video>
<div class='video_controls'>
  <button class='mdl-button mdl-js-button mdl-js-ripple-effect mdl-color--blue mdl-color-text--white' title='download'   onclick="window.location.href='vid0000_plandemic.mp4'"><i class='material-icons'>download</i></button>
  <button class='mdl-button mdl-js-button mdl-js-ripple-effect mdl-color--blue mdl-color-text--white' title='0.5x speed' onclick='vid_speed(vid00,0.5)'><i>0.5x</i></button>
  <button class='mdl-button mdl-js-button mdl-js-ripple-effect mdl-color--blue mdl-color-text--white' title='1.0x speed' onclick='vid_speed(vid00,1.0)'><i>1.0x</i></button>
  <button class='mdl-button mdl-js-button mdl-js-ripple-effect mdl-color--blue mdl-color-text--white' title='1.5x speed' onclick='vid_speed(vid00,1.5)'><i>1.5x</i></button>
  <button class='mdl-button mdl-js-button mdl-js-ripple-effect mdl-color--blue mdl-color-text--white' title='2.0x speed' onclick='vid_speed(vid00,2.0)'><i>2.0x</i></button>
  <button class='mdl-button mdl-js-button mdl-js-ripple-effect mdl-color--blue mdl-color-text--white' title='2.5x speed' onclick='vid_speed(vid00,2.5)'><i>2.5x</i></button>
  <button class='mdl-button mdl-js-button mdl-js-ripple-effect mdl-color--blue mdl-color-text--white' title='3.0x speed' onclick='vid_speed(vid00,3.0)'><i>3.0x</i></button>
  <button class='mdl-button mdl-js-button mdl-js-ripple-effect mdl-color--blue mdl-color-text--white' title='4.0x speed' onclick='vid_speed(vid00,4.0)'><i>4.0x</i></button>
  <script>
    var vid00 = document.getElementById('vid00');  // var vid00 = document.querySelector('video');  // document.querySelector('video').playbackRate = 2.0;
    function vid_play( vid)       {  vid.play()   }
    function vid_stop( vid)       {  vid.pause()  }
    function vid_speed(vid, speed){  vid.playbackRate = speed;  }
  </script>
</div>

--------------------------------------------------------------------------------------------------------------------------------
git init
git checkout -b gh-pages  # Create & switch to branch called `gh-pages`!
git remote   add origin https://github.com/etale-cohomology/mathisart-website.git
git add      --all .
git commit   -m "hi"

git push -u origin gh-pages
git push -f origin gh-pages  # to overwrite/clobber destination!
'''
import subprocess
import os

# VSRC   = '/mnt/ssd0/bible/v5f01_er_doctor_explains_2020.mkv'
# VSRC   = '/mnt/ssd0/bible/v0201_plandemic.mkv'
VSRC   = 'patch1a8_False_Report_122920.mp4'
preset = 'veryslow'  # 'slow' 'veryslow'
qp     = 28
fps    = 24
width  = 1920/2
height = 1080/2

vdst     = f'{os.path.splitext(os.path.basename(VSRC))[0]}_01.mp4'
cmd_pack = '-c:v libx264 -preset {preset}  -profile:v main -pix_fmt yuv420p -qp {qp} -r {fps}'
cmd_size = '-filter:v "scale=w={width}:h={height}:force_original_aspect_ratio=1:flags=bilinear, pad={width}:{height}:(ow-iw)/2:(oh-ih)/2"'
cmd      = f"t ffmpeg  -i {VSRC}  {cmd_pack.format(preset=preset,qp=qp,fps=fps)}  {cmd_size.format(width=width,height=height)}  -c:a libopus -ar 48000 -ac 2  -y {vdst}"
# subprocess.run(cmd, shell=True)
