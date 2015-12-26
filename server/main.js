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
    var d_json = {
	'd_type'      : 'KNOWLEDGE_INPUT_SAVE',
	'd_title'     : d_title,
	'd_date'      : d_date,
	'd_place'     : d_place,
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
    }
);

$('#dateInput').datepicker({
    format: 'mm/dd/yyyy',
    startDate: '-3d',
    autoclose: 'true'
})

