//
// Button Handlers
//

// Call back function after the server
function buttonSaveCallback(data)
{
    alert(data);
}

// button search success handler
function buttonSearchSuccessHandler(data)
{
    alert("SEARCH SUCCESS");
    alert(data);

    for (var key in data) {
	alert(key + ' : ' + data[key]);
    }
    
    //$('#search-result-jumbotron').append(data);
	    
    $('#search-container').html(data);
}

// Actualy Save handler
function buttonSearchHandler()
{
    d_keyword     = document.getElementById("searchTerms").value
    var d_json = {
	'd_type'      : 'KNOWLEDGE_SEARCH',
	'd_keyword' : d_keyword
    }
    // the path is '/save'
    post_url = window.location.protocol + '//' + window.location.host + '/search';
    
    $.ajax({
	type    : "POST",
	url     : post_url,
	data    : d_json,
	success : function (data) {
	    buttonSearchSuccessHandler(data)
	},
	//	error   : function (data) { alert("ERROR"); alert(JSON.stringify(data)); },
    });

    // dataType: 'json'
    //	contentType: 'application/json; charset=utf-8',

    msg = 'POSTING : ' + JSON.stringify(d_json);
    //    alert(msg);
}
