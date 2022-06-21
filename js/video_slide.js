var boolrewind = false;
var intervalRewind =false;
var fastmode = false;
var automode = false;

Reveal.addKeyBinding( { keyCode: 67, key: 'C', description: 'Fast mode' }, () => {
    fastmode=fastmode ? false : true;
    console.log("c, fastmode=",fastmode)
} )

Reveal.addKeyBinding( { keyCode: 65, key: 'A', description: 'Autoplay' }, () => {
    automode=automode ? false : true;
    console.log("a, automode=",fastmode)
    Reveal.next()
} )


// video slide handling fns
Reveal.addEventListener( 'fragmentshown', function( event ) {
  // event.fragment = the fragment DOM element
  if(event.fragment.getAttribute('type')=='video'){
      console.log("shown");
      boolrewind=false;
      var time_start = event.fragment.getAttribute('time_start');
      var time_end = event.fragment.getAttribute('time_end');

      cslide=Reveal.getCurrentSlide();
      vidobj=cslide.slideBackgroundElement.getElementsByTagName('video')[0]
      vidobj.ontimeupdate = function(){}
      vidobj.playbackRate = 1.0
      vidobj.currentTime = time_start
      vidobj.play()
      vidobj.ontimeupdate = function(){

            if(fastmode || vidobj.currentTime-time_end>0){
              console.log(vidobj.currentTime-time_end)
              vidobj.pause();
              vidobj.currentTime = time_end;
              vidobj.ontimeupdate = function(){};
              if(automode) Reveal.next()
            }
          }

      console.log(time_start+"->"+time_end);
  }

} );
Reveal.addEventListener( 'fragmenthidden', function( event ) {
  if(event.fragment.getAttribute('type')=='video'){
      console.log("hidden");
      var time_start = event.fragment.getAttribute('time_start');
      var time_end = event.fragment.getAttribute('time_end');

      cslide=Reveal.getCurrentSlide();
      vidobj=cslide.slideBackgroundElement.getElementsByTagName('video')[0]

      vidobj.ontimeupdate = function(){}

      console.log(time_start+"<-"+time_end);

      vidobj.pause()
      vidobj.currentTime = time_start
  }

} );


Reveal.addEventListener( 'slidechanged', function( event ) {
      if(event.currentSlide.getAttribute("type") == "videoslide"){
        console.log("videoslide");
        vidobj=event.currentSlide.slideBackgroundContentElement.getElementsByTagName('video')[0]

        console.log(event)

        if(automode) Reveal.next()
      }
} );
