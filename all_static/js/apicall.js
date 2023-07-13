function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function add_to_cart(pro_id){
    var temp = $('#buy_quant').val();
    var avl_quant = $('#avl_quant').val();
    if (temp > avl_quant){
        alert('Enter less quantity then the available quantity');
        return false;
    }
    $.ajax({
        url:'/webapp/add_to_cart',
        method:'post',
        headers: { 'Authorization': $('#token').val()  },
        data:{id:pro_id}
        success:function(result){
            result = JSON.parse(result)
            alert("added")
        },
        error:function(result){
            console.log(result['responseText']);
        }
    });
}

function save_movies(){
    var data = {
        title: $('#title').val(),
        genres: $('#genres').val(),
        release_date:$('#release_date').val(),
        director:$('#director').val()
    };
    $.ajax({
        url:'/api/movies',
        method:'post',
        headers: {'X-CSRFToken': csrftoken},
        data:data,
        success:function(result){
            alert("Movie added successfully")
        },
        error:function(){
            alert("error while saving movie")
        }
    });
}

function edit_save(id){
    var data = {
        id : $('#id').val(),
        title: $('#e_title').val(),
        genres: $('#e_genres').val(),
        release_date:$('#e_release_date').val(),
        director:$('#e_director').val()
    };
     $.ajax({
        url:'/api/movies',
        method:'patch',
        headers: {'X-CSRFToken': csrftoken},
        data: data,
        success:function(result){
            alert('Updated Successfully');
            movie_list();
        },
        error:function(xyz){
            alert('Failed');
        }
    });
}


function delete_click(id){
    var data = {
        id : id
    }
     $.ajax({
        url:'/api/movies',
        method:'delete',
        headers: {'X-CSRFToken': csrftoken},
        data: data,
        success:function(result){
            alert('Deleted Successfully');
            movie_list()
        },
        error:function(xyz){
            alert('Failed');
        }
    });
}

    function change_val(){
        if ($("#delete_old_data").is(":checked")){
            $("#delete_old_data").val('on');
        }
        else{
            $("#delete_old_data").val('off');
        }
    }