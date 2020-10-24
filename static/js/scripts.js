// On page load run the init function
window.addEventListener('load', function() {
  init();
})

// Add event listners etc
function init (){
  var burger = document.querySelector('.sidenav_burger');
  var addNewButton = document.getElementById('button_addnew');
  var main = document.querySelector('.main');
  burger && burger.addEventListener('click', ()=>{toggleMenuHandler()});
  addNewButton && addNewButton.addEventListener('click', ()=>{showAddNewHandler()})
  main && main.addEventListener('click', () =>{toggleClickAwayHandler()})

  // addtoinv() and clear() buttons
  var btnclear = document.getElementById("clear_btn")
  btnclear && btnclear.addEventListener("click", ()=>{clear()})

  // set tab 1 to active
  tabtoggle(1)
  loading(0)
}

function toggleMenuHandler(){
  var burger = document.querySelector('.sidenav_burger');
  var sideBar = burger.parentElement 
  sideBar.classList.toggle('isOpen');
  main.classList.toggle('isOpen');
}

function toggleClickAwayHandler(e) {
  var main = document.querySelector('.main');
  if (main.classList.contains('isOpen')) {
    var burger = document.querySelector('.sidenav_burger');
    var sideBar = burger.parentElement
    sideBar.classList.remove('isOpen');
    main.classList.remove('isOpen');
  }
}

function showAddNewHandler () {
  document.getElementById('button_addnew').style.display = 'none'
  document.getElementById('addnewbox').style.display = 'flex'
}

function loading(x, t=1500) {
  if (x==1) {
    $("#main").hide()
    $("#pre_loader").show()
    $(".meter > span").each(function() {
      $(this)
        .data("origWidth", $(this).width())
        .width(0)
        .animate({
          width: $(this).data("origWidth") // or + "%" if fluid
        }, t);
    });
  } else {
    $("#pre_loader").hide()
    $("#main").show()
  }
}

/** activatees loading screen and redirect.
 * arg1=href (e.g. '/about')  */
function Redirect(arg) {
  loading(1)
  window.location.href = arg;
}

function show(x) {
  $("#"+x).show()
}

function hide(x) {
  $("#"+x).hide()
}

/** assess the risk associated with the current inventory */
function Process() {
  if (inventoryexists===true) {
    $(".current_page").removeClass('current_page')
    $("#navbar_process").addClass("current_page")
    hide("list_div")
    hide("addnewbox")
    loading(1,5000)
    window.setTimeout(function() {
      Redirect('/results')
    }, 2000);
  } else {
    return false;
  }
}

function NewStart() {
  loading(1,500)
  $.post("/clearinv", {"clearinv": true}, function (data) {
    if (data == "Cleared") {
      Redirect('/')
    }
  })
}