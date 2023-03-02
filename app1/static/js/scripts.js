
function fnDel(id,url) {
  swal({
      title: "Está seguro de eliminar?",
      text: "Una vez eliminado, no podrá recuperar este archivo !",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete)  => {
      if (willDelete) {
        
        swal("Usuario! Su archivo se ha eliminado exitosamente!", {
          icon: "success",
          
        });
        let index= document.getElementsByTagName("td");
        let  a = document.getElementById(id);
        a.setAttribute("href", url+String(index[0].innerHTML));
        
        document.getElementById(id).click();
        

      } else {
        swal("Su archivo se salvo de ser eliminado !");
      }
    });
};


function validate() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('pass').value;
    
    if (username === "" || username === null) {
      intensify($('#userLabel'));
          return false;
    }
    
    if (password === "" || password === null) {
         intensify($('#passLabel'));
          return false;
    }
  }
  
  function intensify(intense) {
    intense.addClass('animated shakeit').delay(6000).queue(function(){
            intense.removeClass('animated shakeit').dequeue();
          });
  }
  
  function clicked() {
    $('button').addClass('clicked').delay(200).queue(function(){
      $('button').removeClass('clicked').dequeue();
    });
  }
  
  var submit = document.getElementById('submit');
  submit.addEventListener('click', clicked);
  submit.addEventListener('click', validate);
