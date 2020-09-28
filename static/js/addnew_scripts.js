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
  text = text.replace(/-| /g,'');
  if (text.length > 2) {
    let idlist = $("li.acli")
    for (let i = 0; i < idlist.length; i++) {
      let name = idlist[i].innerText
      name = name.replace(/-| /g,'');
      for (let j = 0; j < name.length; j++) {
        if (name.slice(j, j+text.length).toUpperCase() === text.toUpperCase()) {
          $(idlist[i]).show()
        }
      }
    }
  }
}

function populate(x) {
  let tempvar = $("#li_"+x)
  $("#substance_1").val($(tempvar).html()).addClass("flash");
  $("#substance_1").attr("chemid",x)
  $("#type_1").val($(tempvar).attr('chemtype')).addClass("flash");
  $("#class_1").val($(tempvar).attr('chemclass')).addClass("flash");
  $(".acli").hide()
  $("#qty_1").focus()
}

function clear(x) {
  console.log("polo")
  if (x == 1) {
    document.getElementById("substance_1").value = "";
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
    console.log("false", x)
    return false;
  }
}

function addtoinv(x) {
  substid = $("#substance_"+x).attr("chemid")
  qty = $("#qty_"+x).val()
  newEntryObj = {"id": substid, "qty": qty}
  loading(1)

  $.post("/addtoinv", {
      "newEntry": JSON.stringify(newEntryObj)
    },
    function (data) {
      console.log(data)
      $("#noinv_tr").remove()
      $("#list_div > table").append(data)
      loading(0)
    });

  clear(x)
}