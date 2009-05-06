
var init = function() {

    $('[title]').tooltip({
        track: true,
        delay: 50,
        showURL: false,
        showBody: " - ",
        opacity: 0.85
    });

}

$(document).ready(init);



