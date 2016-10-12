$(document).ready(function(){
    //Convert address tags to google map links - Michael Jasper 2012
    $('address').each(function () {
        var link = "<a href='http://maps.google.com/maps?q=" + encodeURIComponent( $(this).text() ) + "' target='_blank'>" + $(this).text() + "</a>";
        $(this).replaceWith(link);
    });
    
    $("map-address").each(function(){                         
        var embed ="<iframe width='425' height='350' frameborder='0' scrolling='no'  marginheight='0' marginwidth='0' src='https://maps.google.com/maps?&amp;q="+ encodeURIComponent( $(this).text() ) +"&amp;output=embed'></iframe>";
        $(this).html(embed);             
    });
    
    // Name can't be blank
    $('#contact_name').on('input', function() {
        var input=$(this);
        var is_name=input.val();
        if(is_name){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });

    // Subject line can't be blank
    $('#contact_subject').on('input', function() {
        var input=$(this);
        var is_name=input.val();
        if(is_name){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });

    // Email must be an email
    $('#contact_email').on('input', function() {
        var input=$(this);
        var re = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        var is_email=re.test(input.val());
        if(is_email){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });

    // Website must be a website
    $('#contact_website').on('input', function() {
        var input=$(this);
        if (input.val().substring(0,4)=='www.'){input.val('http://www.'+input.val().substring(4));}
        var re = /(http|ftp|https):\/\/[\w-]+(\.[\w-]+)+([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?/;
        var is_url=re.test(input.val());
        if(is_url){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}
    });

    // Message can't be blank
    $('#contact_message').keyup(function(event) {
        var input=$(this);
        var message=$(this).val();
        console.log(message);
        if(message){input.removeClass("invalid").addClass("valid");}
        else{input.removeClass("valid").addClass("invalid");}   
    });

    // After Form Submitted Validation
    $("#contact_submit button").click(function(event){
        var form_data=$("#contact").serializeArray();
        var error_free=true;
        for (var input in form_data){
            var element=$("#contact_"+form_data[input]['name']);
            var valid=element.hasClass("valid");
            var error_element=$("span", element.parent());
            if (!valid){error_element.removeClass("error").addClass("error_show"); error_free=false;}
            else{error_element.removeClass("error_show").addClass("error");}
        }
        if (!error_free){
            event.preventDefault();                    
        }
        else{                    
            // alert('No errors: Form will be submitted');
        }
    });
});