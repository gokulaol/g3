
// Set some global variables for ease
button_save     = document.getElementById("buttonSave")
button_harden   = document.getElementById("buttonHarden")
button_retrieve = document.getElementById("buttonRetrieve")
button_next     = document.getElementById("buttonNext")

// Onload handler called when the page gets loaded
function onLoadHandler()
{    
    button_save.disabled = true
    button_harden.disabled = true
    button_retrieve.disabled = true
    button_next.disabled = true
}

window.onload = onLoadHandler

//
// Button Handlers
//

// Call back function after the server
function buttonSaveCallback(data)
{
    alert(data);
}
// Actualy Save handler
function buttonSaveHandler()
{    
    d_title     = document.getElementById("titleInput").value
    d_date      = document.getElementById("dateInput").value
    d_place     = document.getElementById("placeInput").value
    d_knowledge = document.getElementById("knowledgeInput").value
    d_series    = document.getElementById("seriesChoice").value
    d_sheetid   = document.getElementById("sheetIdInput").value
    d_sheetno   = String(document.getElementById("sheetNoInput").value)
    // special case: trim the "An Intimate Note..." name to
    //               handle efficiently at the server
    if (d_series == "An Intimate Note to a Sincere Seeker") {
	d_series = "An Intimate Note";
    }
    var d_json = {
	'd_type'      : 'KNOWLEDGE_INPUT_SAVE',
	'd_title'     : d_title,
	'd_date'      : d_date,
	'd_place'     : d_place,
	'd_series'    : d_series,
	'd_sheetid'   : d_sheetid,
	'd_sheetno'   : d_sheetno,	
	'd_knowledge' : d_knowledge
    }
    // the path is '/save'
    post_url = window.location.protocol + '//' + window.location.host + '/save';
    
    $.ajax({
	type    : "POST",
	url     : post_url,
	data    : d_json,
	success : function (data) { alert("SUCCESS"); alert(data); },
	//	error   : function (data) { alert("ERROR"); alert(JSON.stringify(data)); },
    });

    // dataType: 'json'
    //	contentType: 'application/json; charset=utf-8',

    msg = 'POSTING : ' + JSON.stringify(d_json);
    alert(msg);
}

function buttonHardenHandler()
{
    alert("botton harden gokul! ");
}
function buttonRetrieveHandler()
{
    alert("botton save gokul! ");
}
function buttonNextHandler()
{
    alert("botton save gokul! ");
}

$('#inputSelected').click(
    function() {
	action_box = document.getElementById("inputAction")
	action_box.value = "Input Knowledge"
	action_box.disabled = true

	document.getElementById("sheetIdInput").disabled = true
	document.getElementById("titleInput").disabled = false
    }
);
$('#retrieveSelected').click(
    function() {
	action_box = document.getElementById("inputAction")
	action_box.value = "Retrieve Knowledge"
	action_box.disabled = true

	document.getElementById("titleInput").disabled = true
	document.getElementById("sheetIdInput").disabled = false	
    }
);


$('#intimateNote').click(
    function() {
	action_box = document.getElementById("seriesChoice")
	action_box.value = "An Intimate Note to a Sincere Seeker"
	action_box.disabled = true
    }
);

$('#satsangKnowledge').click(
    function() {
	action_box = document.getElementById("seriesChoice")
	action_box.value = "Satsang Knowledge"
	action_box.disabled = true
    }
);

$('#bhaktiSutras').click(
    function() {
	action_box = document.getElementById("seriesChoice")
	action_box.value = "Bhakti Sutras"
	action_box.disabled = true
    }
);

$('#yogaSutras').click(
    function() {
	action_box = document.getElementById("seriesChoice")
	action_box.value = "Patanjali Yoga Sutras"
	action_box.disabled = true
    }
);

$('#ashtavakraGita').click(
    function() {
	action_box = document.getElementById("seriesChoice")
	action_box.value = "Ashtavakra Gita"
	action_box.disabled = true
    }
);

$('#shivaSutras').click(
    function() {
	action_box = document.getElementById("seriesChoice")
	action_box.value = "Shiva Sutras"
	action_box.disabled = true
    }
);

$('#kenopanishad').click(
    function() {
	action_box = document.getElementById("seriesChoice")
	action_box.value = "Kena Upanishad"
	action_box.disabled = true
    }
);

$('#kathopanishad').click(
    function() {
	action_box = document.getElementById("seriesChoice")
	action_box.value = "Katha Upanishad"
	action_box.disabled = true
    }
);

$('#knowledgeInput').keyup(function(event) {
    var k_len = document.getElementById("knowledgeInput").value.length
    var k_val = document.getElementById("knowledgeInput").value
    // may not be the most efficient way to do this test
    if (k_len > 0) {
	if (/[a-zA-Z]/.test(k_val)) {	
	    button_save.disabled = false
	    return
	}
    }
    // else
    button_save.disabled = true
})

$('#dateInput').datepicker({
    format: 'mm-dd-yyyy',
    startDate: '05-13-1956',
    autoclose: 'true'
})

