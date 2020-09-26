function hideaddnew() {
  $("#addnewbox").fadeOut()
}

function tabtoggle(int) {
  switch (int) {
    case 1:
      $("#tab_2_row_1").hide()
      $("#tab_1_row_1").show()
      $("#tab_1_row_2").show()
      $("#tab_2").removeClass("active_tab")
      $("#tab_1").addClass("active_tab")
      break;
    case 2:
      $("#tab_1_row_1").hide()
      $("#tab_1_row_2").hide()
      $("#tab_2_row_1").show()
      $("#tab_1").removeClass("active_tab")
      $("#tab_2").addClass("active_tab")
      break;
  }
}

// QUackk quack
function AutusCumpletus() {
  $(".acli").hide()
  let text = $("#substance_1").val()
  if (text.length > 3) {
      let idlist = $("li.acli")
      for (let i = 0; i < idlist.length; i++) {
          if (idlist[i].innerText.slice(0,text.length).toUpperCase()===text.toUpperCase()) {
              $(idlist[i]).show()
          }
      }
  }
}

function populate(x) {
  $("#substance_1").val(x).addClass("flash");
  $("#type_1").val("testtype"+x).addClass("flash");
  $("#class_1").val("testclass"+x).addClass("flash");
  $(".acli").hide()
  $("#qty_1").focus()
}

function clear(x) {
  if (x == 1) {
    $("#substance_1").val("")
    $("#qty_1").val("")
    $("#class_1").val("")
    $("#type_1").val("")
  } else if (x == 2){
    $("#substance_2").val("")
    $("#qty_2").val("")
    $("#class_2").val("")
    $("#type_2").val("")
  } else {
    return false;
  }
}