var $cgj;
function contagiorni_isVisible( elem ) {
    if (!(elem instanceof Element)) throw Error('DomUtil: elem is not an element.');
    const style = getComputedStyle(elem);
    if (style.display === 'none') return false;
    if (style.visibility !== 'visible') return false;
    if (style.opacity < 0.1) return false;
    if (elem.offsetWidth + elem.offsetHeight + elem.getBoundingClientRect().height +
        elem.getBoundingClientRect().width === 0) {
        return false;
    }
    const elemCenter   = {
        x: elem.getBoundingClientRect().left + elem.offsetWidth / 2,
        y: elem.getBoundingClientRect().top + elem.offsetHeight / 2
    };
    if (elemCenter.x < 0) return false;
    if (elemCenter.x > (document.documentElement.clientWidth || window.innerWidth)) return false;
    if (elemCenter.y < 0) return false;
    if (elemCenter.y > (document.documentElement.clientHeight || window.innerHeight)) return false;
    let pointContainer = document.elementFromPoint(elemCenter.x, elemCenter.y);
    do {
        if (pointContainer === elem) return true;
    } while (pointContainer = pointContainer.parentNode);
    return false;
};

function contagiorni_createElementFromHTML(htmlString) {
    var div = document.createElement('div');
    div.innerHTML = htmlString.trim();
  
    // Change this to div.childNodes to support multiple top-level nodes
    return div.firstChild; 
}


  function timeCallback() {
    $cgj = jQuery.noConflict(false);
    loadScript("https://www.contagiorni.it/v1theme/js/timerStyles.js", function() {
        $cgj(".cg_timer").TimeCircles({
            "animation": "smooth",
            "bg_width": 0.2,
            "fg_width": 0.03,
            "circle_bg_color": "#90989F",
            "text_size": 0.09,
            "time": {
                "Days": {
                    "text": "Giorni",
                    "color": "#FFCC66",
                    "show": true
                },
                "Hours": {
                    "text": "Ore",
                    "color": "#99CCFF",
                    "show": true
                },
                "Minutes": {
                    "text": "Minuti",
                    "color": "#BBFFBB",
                    "show": true
                },
                "Seconds": {
                    "text": "Secondi",
                    "color": "#FF9999",
                    "show": true
                }
            }
        });
    
        $cgj(window).resize(function(){
            if($cgj( window ).width() < 1024) {
                $cgj('#cg_seconddiv').show();
                $cgj('#cg_firstdiv').TimeCircles({
                    "time": { "Minutes": { "show": false }, "Seconds": { "show": false }}
                });
            } else {
                $cgj('#cg_seconddiv').hide();
                $cgj('#cg_firstdiv').TimeCircles({
                    "time": { "Minutes": { "show": true }, "Seconds": { "show": true }}
                });
            }
    
            $cgj(".cg_timer").TimeCircles().rebuild();
        }); 
    });
  }

if (contagiorni_conditions()) {
    console.log("[CONTAGIORNI] Funzionante.");
    var currcurr = document.getElementById("contagiorni-309858").innerHTML;
    loadjscssfile("https://www.contagiorni.it/v1theme/css/timerstyles.css", "css");

    loadScript("https://code.jquery.com/jquery-3.5.1.min.js", timeCallback);   

    document.getElementById("contagiorni-309858").innerHTML = `<div class="container_cg">
        <div style="min-height: 170px">
        <div class="cg_timer" id="cg_firstdiv" data-date="2022-06-08 00:00:00" data-options='{"time": { "Minutes": { "show": true }, "Seconds": { "show": true }}, "count_past_zero": false}' style="width: 100%;"></div>
        <div class="cg_timer" id="cg_seconddiv" data-date="2022-06-08 00:00:00" data-options='{"time": { "Days": { "show": false }, "Hours": { "show": false }}, "count_past_zero": false}' style="width: 100%; display: none"></div>
    </div>
    </div>
 
<script>
$cgj(".cg_timer").TimeCircles({
    "animation": "smooth",
    "bg_width": 0.2,
    "fg_width": 0.03,
    "circle_bg_color": "#90989F",
    "text_size": 0.09,
    "time": {
        "Days": {
            "text": "Giorni",
            "color": "#FFCC66",
            "show": true
        },
        "Hours": {
            "text": "Ore",
            "color": "#99CCFF",
            "show": true
        },
        "Minutes": {
            "text": "Minuti",
            "color": "#BBFFBB",
            "show": true
        },
        "Seconds": {
            "text": "Secondi",
            "color": "#FF9999",
            "show": true
        }
    }
});

$cgj(window).resize(function(){
    if($cgj( window ).width() < 1024) {
        $cgj('#cg_seconddiv').show();
        $cgj('#cg_firstdiv').TimeCircles({
            "time": { "Minutes": { "show": false }, "Seconds": { "show": false }}
        });
    } else {
        $cgj('#cg_seconddiv').hide();
        $cgj('#cg_firstdiv').TimeCircles({
            "time": { "Minutes": { "show": true }, "Seconds": { "show": true }}
        });
    }

    $cgj(".cg_timer").TimeCircles().rebuild();
});

</script>
<br>` + currcurr;

    
} else {
    alert("[CONTAGIORNI] Lo script Ã¨ incompleto. Verifica di aver copiato bene.");
}
