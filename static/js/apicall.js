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
//    var buy_q = `buy_quant${pro_id}`
//    console.log(">>>>>>>>buy_q", buy_q)
    var buy_quant = $('#buy_quant' + pro_id ).val();
    var avl_quant = $('#avl_quant' + pro_id ).val();
    if (parseInt(buy_quant) > parseInt(avl_quant)){
        alert('Enter less quantity then the available quantity');
        return false;
    }
    var data = {'id':pro_id, 'buy_quant':parseInt(buy_quant)}
    console.log(data)
    $.ajax({
        url:'/webapp/add_to_cart',
        method:'post',
        headers: {'X-CSRFToken': csrftoken},
        data:data,
        success:function(){
            alert("added");
        },
        error:function(result){
            console.log(result['responseText']);
        }
    });
}

