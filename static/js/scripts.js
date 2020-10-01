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