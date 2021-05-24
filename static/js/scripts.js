// On page load run the init function
window.addEventListener('load', function() {
  init();
})

// Add event listeners etc
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
  var addtoinv_btn = document.getElementById('addtoinv_btn')
  addtoinv_btn && addtoinv_btn.addEventListener('click', ()=> {addtoinv()})
  var hide_addnew_form_btn = document.getElementById("hide_addnew_form_btn")
  hide_addnew_form_btn && hide_addnew_form_btn.addEventListener('click', ()=> {hideaddnew()})

  // remove loader
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
  $("#loader_width_adjustable").attr("style", "width: 100%")
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

// adjusts loader width. if m = true: message will display.
function barwidth(int,m=false) {
  $("#loader_width_adjustable").animate({"width" : int.toString() + "%"})

  if (m) {
    switch(int) {
      case 0:
        $("#status_message").html("establishing connection")
        break
      case 10:
        $("#status_message").html("checking CAS number validity")
        break
      case 20:
        $("#status_message").html("searching by CAS")
        break
      case 30:
        $("#status_message").html("cross-referencing with external database")
        break
      case 40:
        $("#status_message").html("parsing first response")
        break
      case 45:
        $("#status_message").html("invalid CAS. Searching by substance name")
        break
      case 50:
        $("#status_message").html("verifying matches")
        break
      case 60:
        $("#status_message").html("parsing second response")
        break
      case 70:
        $("#status_message").html("obtaining classification")
        break
      case 80:
        $("#status_message").html("parsing GHS statements")
        break
      case 90:
        $("#status_message").html("calculating tier thresholds")
        break
      case 100:
        $("#status_message").html("complete!")
        break
    }
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

