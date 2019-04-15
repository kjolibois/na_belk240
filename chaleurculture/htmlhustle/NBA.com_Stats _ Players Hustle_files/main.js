var tl;
var stopWatch;
var tempHeight = 0;
var dimensions = (function() {
  var str = document
    .querySelectorAll("[name='ad.size']")[0]
    .getAttributeNode("content").value;
  var widthMatch = /width\=(\d+)/.exec(str);
  var heightMatch = /height\=(\d+)/.exec(str);
  return {
    width: parseInt(widthMatch[1]),
    height: parseInt(heightMatch[1])
  };
})();

//INITIALIZE
function init() {
  IDsToVars();

  //set timeline
  tl = new TimelineLite();
  container.style.width = dimensions.width + "px";
  container.style.height = dimensions.height + "px";

  animate();
  addListeners();
}

function addListeners() {
  //replay functionality
  t = new TimelineLite();
  ctaHit.onmouseover = function() {
    t.to(ctaArrow, 0.3333, {
      x: 4,
      repeat: 1,
      yoyo: !0,
      ease: Power2.easeInOut
    }).to(ctaArrow, 0.3333, { x: 0 });
  };
}

//ANIMATE
function animate() {
  //setInterval(checkHeight , 500);
  tl.addLabel("f1")
    .set([txt01A, txt02A, txt03A, txt03B], { x: -350 })
    .set([txt03, txt03A, txt03B, ctaBox, ctaArrow], { alpha: 0 })
    .to(txt01A, 0.5, { alpha: 1, x: 0, ease: Power4.easeOut }, "f1+=.5")
    .to([txt01A], 1, { alpha: 0, ease: Power2.easeIn }, "f1+=4")
    .addLabel("f2")
    .to(txt02A, 0.5, { alpha: 1, x: 0, ease: Power4.easeOut }, "f2+=.5")
    .addLabel("ff")
    .to([txt02A], 1, { alpha: 0, ease: Power2.easeIn }, "ff+=4")
    .addLabel("resolve")

    .staggerTo(
      [txt03A, txt03B],
      1,
      { alpha: 1, x: 0, ease: Power4.easeOut },
      0.1,
      "resolve+=1"
    )
    .to([txt03], 1, { alpha: 1, ease: Power2.easeOut }, "resolve+=1.5")
    .to(
      [ctaBox, ctaArrow],
      1,
      { alpha: 1, ease: Power2.easeOut },
      "resolve+=1.5"
    )
    .to(
      ctaArrow,
      0.3,
      { x: 4, repeat: 1, yoyo: !0, ease: Power2.easeInOut },
      "resolve+=1.9"
    )
    .set(ctaHit, { autoAlpha: 1 }, "resolve+=1.8");

  //timeline animation here
}

function returnTimer() {
  stopWatch = (new Date().getTime() - stopWatch) * 0.001;
  console.log(stopWatch + " seconds");
}

function replay() {
  tl.restart();
}
//SET IDs IN DOM TO GLOBAL VARIABLES
function IDsToVars() {
  var allElements = document.getElementsByTagName("*");

  for (var q = 0; q < allElements.length; q++) {
    var el = allElements[q];
    if (el.id) {
      window[el.id] = document.getElementById(el.id);
    }
  }
}

function showLegal() {
  legalBubble.style.display = "block";
  legalOverlay.style.display = "block";
  TweenLite.to("#legalBubble", 0.5, {
    alpha: 1
  });
  TweenLite.to("#legalOverlay", 0.5, {
    alpha: 0.85
  });
  document.getElementById("legalOverlay").style.display = "block";
  document.getElementById("legalBubble").style.display = "flex";
  document.getElementById("legalBubbleClose").style.display = "block";
  if (legalText.style.offsetHeight > 166) {
    up_arrow.style.display = "block";
    down_arrow.style.display = "block";
    legalText.style.height = "168px";
  }
  //document.getElementById("legalButton2").style.display = "block";
}

function autoshowlegal() {
  showLegal();
  TweenLite.delayedCall(2, hideLegal);
}

function hideLegal() {
  TweenLite.to("#legalBubble", 0.5, {
    alpha: 0
  });
  TweenLite.to("#legalOverlay", 0.5, {
    alpha: 0,
    onComplete: nolegal
  });
  //document.getElementById("legalOverlay").style.display = "none";
  //document.getElementById("legalBubble").style.display = "none";
  document.getElementById("legalBubbleClose").style.display = "none";
  //document.getElementById("legalButton2").style.display = "none";
}

function nolegal() {
  legalBubble.style.display = "none";
  legalOverlay.style.display = "none";
}

function getStyles(selector) {
  return {
    height: parseInt(window.getComputedStyle(selector).height),
    width: parseInt(window.getComputedStyle(selector).width),
    top: parseInt(window.getComputedStyle(selector).top),
    left: parseInt(window.getComputedStyle(selector).left)
  };
}
