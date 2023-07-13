function create_account(){
    var data={
        user_name:$('#user_name').val(),
        first_name:$('#first_name').val(),
        last_name:$('#last_name').val(),
        password:$('#password').val()
    };
    $.ajax({
        url:'/create_user',
        data:data,
        method:'POST',
        success:function(result){
            alert('Created Successfully')
            window.location.replace('/');
        },
        error:function(result){
            alert('in error')
        }
    })
}



function login_ajax(){
    var data={
        username:$('#username').val(),
        password:$('#password').val()
    };
    $.ajax({
        url:'/user_authenticate',
        data:data,
        method:'post',
        success:function(result){
          window.location.replace('/webapp/home_page');
        },
        error:function(result){
            alert("user/password wrong");
        }
    });
}

function passfunc(){
    var x = document.getElementById("password");
    var eye = document.getElementById("togglePassword");
    if (x.type === "password") {
        x.type = "text";
        $( "#togglePassword" ).removeClass( "far fa-eye-slash" )
        $( "#togglePassword" ).addClass( "far fa-eye" )
    } else {
        x.type = "password";
        $( "#togglePassword" ).removeClass( "far fa-eye" )
        $( "#togglePassword" ).addClass( "far fa-eye-slash" )
    }
}
