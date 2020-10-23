/** function to hide the "AddNew" dialog box */
function hideaddnew() {
  document.getElementById('button_addnew').style.display = 'block'
  document.getElementById('addnewbox').style.display = 'none'
  // $("#addnewbox").fadeOut()
}

/** used to switch between named and listed substance tabs  */
function tabtoggle(int) {
  switch (int) {
    case 1:
      $("#tab_2_row_1").hide()
      $("#tab_2_row_2").hide()
      $("#tab_1_row_1").show()
      $("#tab_1_row_2").show()
      $("#tab_2").removeClass("active_tab")
      $("#tab_1").addClass("active_tab")
      break;
    case 2:
      $("#tab_1_row_1").hide()
      $("#tab_1_row_2").hide()
      $("#tab_2_row_1").show()
      $("#tab_2_row_2").show()
      $("#tab_1").removeClass("active_tab")
      $("#tab_2").addClass("active_tab")
      break;
  }
}

// autocomplete suggestions for named substances
function AutusCumpletus() {
  $(".acli").hide()
  let text = $("#substance_1").val()
  text = text.replace(/-| /g, '');
  if (text.length > 2) {
    let idlist = $("li.acli")
    for (let i = 0; i < idlist.length; i++) {
      let name = idlist[i].innerText
      name = name.replace(/-| /g, '');
      for (let j = 0; j < name.length; j++) {
        if (name.slice(j, j + text.length).toUpperCase() === text.toUpperCase()) {
          $(idlist[i]).show()
        }
      }
    }
  }
}

/** when clicking on a list item, populate the input field with the relevant info */
function populate(x) {
  let tempvar = $("#li_" + x)
  $("#substance_1").val($(tempvar).html()).addClass("flash");
  $("#substance_1").attr("chemid", x)
  $("#type_1").val($(tempvar).attr('chemtype')).addClass("flash");
  $("#class_1").val($(tempvar).attr('chemclass')).addClass("flash");
  $(".acli").hide()
  $("#qty_1").focus()
}

/** uses regex to validate the user input where x is the current tab */
function enable_add_button(x) {
  var letterNumberDashSpace = /^[0-9a-zA-Z\-\s\/\\\(\)]+$/;
  var numbers = /^[0-9]+$/

  if (x == 1) {
    let substance_1 = $("#substance_1").val()
    let qty_1 = $("#qty_1").val()
    if (substance_1.length > 5 && qty_1>0) {
      if (new RegExp(letterNumberDashSpace).test(substance_1) && new RegExp(numbers).test(qty_1)) {
        document.getElementById("addtoinv_1").addEventListener("click", function () {
          addtoinv(1)
        })
        $("#addtoinv_1").removeClass("button--disabled")
      }
    } else {
      $("#addtoinv_1").addClass("button--disabled")
      document.getElementById("addtoinv_1").removeEventListener("click", function () {
        addtoinv(1)
      })
    }
  } else if (x == 2) {
    let substance_2 = $("#substance_2").val()
    if (substance_2.length > 5) {
      test_2_1 = new RegExp(letterNumberDashSpace).test($("#substance_2").val()) ? true : false
      test_2_2 = $("#class_2").val() !== "" ? true : false
      test_2_3 = new RegExp(numbers).test($("#qty_2").val()) ? true : false
      if (test_2_1 === true && test_2_2 === true && test_2_3 === true) {
        $("#addtoinv_2").removeClass("button--disabled")
        document.getElementById("addtoinv_2").addEventListener("click", function () {
          addtoinv(2)
        })
      } else {
        $("#addtoinv_2").addClass("button--disabled")
        document.getElementById("addtoinv_2").removeEventListener("click", function () {
          addtoinv(2)
        })
      }
    }
  }
}

/** clears the input fields where x is the tab number */
function clear(x) {
  console.log(`clear(${x})`)
  switch (x) {
    case 1:
      document.getElementById("substance_1").value = "";
      $("#substance_1").val("")
      $("#qty_1").val("")
      $("#class_1").val("")
      $("#type_1").val("")
      break;
    case 2:
      $("#substance_2").val("")
      $("#qty_2").val("")
      $("#class_2").val("")
      $("#type_2").val("")
      break;
    default:
      console.log("false", x)
      return false;
  }
  $("#addtoinv_1").addClass("button--disabled")
  $("#addtoinv_2").addClass("button--disabled")
  $(".flash").removeClass("flash")
}

/** add or remove red borders on fields with invalid values when trying to add a substance to the inv */
function pre_add_check(x) {
  if (x == 1) {
    if (!$("#addtoinv_1").hasClass("button--disabled")) {
      $("input.invalid_input").removeClass("invalid_input")
      return true;
    } else {
      $("#substance_1").addClass("invalid_input")
      $("#qty_1").addClass("invalid_input")
    }
  } else if (x == 2) {
    if (!$("#addtoinv_2").hasClass("button--disabled")) {
      $("input.invalid_input").removeClass("invalid_input")
      return true;
    } else {
      $("#substance_2").addClass("invalid_input")
      $("#type_2").addClass("invalid_input")
      $("#class_2").addClass("invalid_input")
      $("#qty_2").addClass("invalid_input")
    }
  }
  return false
}

/** using the input fields, adds a substance to the inventory */
function addtoinv(x) {
  // var preCheck = pre_add_check(x)
  // if (pre_add_check(x) === false) {
  //   alert("Please check that you've entered valid information into the fields above.")
  // } else {
    if (x==2) {
      chemid = $("#class_2").val()
      d = new Date()
      substid = "custom_" + d.getDate().toString() + d.getHours() + d.getMinutes() + d.getSeconds()
      qty = $("#qty_2").val()
      substname = $("#substance_2").val()
      cas = $("#cas_2").val()
      newEntryObj = {
        "id": substid,
        "name": substname,
        "CAS": cas,
        "qty": qty,
        "chemid": chemid,
        "type": "listed"
      }
      loading(1)
      addtoinvPOST(newEntryObj, x)
    } else if (x==1) {
      id = $("#substance_1").attr("chemid")
      qty = $("#qty_1").val()
      newEntryObj = {
        "id": id,
        "qty": qty,
        "type": "named"
      }
      loading(1)
      addtoinvPOST(newEntryObj, x)
    }
  // }
}

function toggleEditMode (e, x){
  const target = e.target
  const classes = target.classList
  const cell = document.getElementById(x + "_qty_td")
  const inEditMode = cell.getAttribute('EditMode')
  if (inEditMode === 'false') {
    cell.setAttribute('EditMode', true)
    target.classList.remove('button_icon--edit')
    target.classList.add('button_icon--check')
    edit(x, cell)
  } else {
    cell.setAttribute('EditMode', false)
    target.classList.add('button_icon--edit')
    target.classList.remove('button_icon--check')
    update(x, cell)
  }
}


/** provides the interface for the user to update the qty of an item in already in the inv */
function edit(x, cell) {
  const qty = cell.getAttribute('value')
  const input = document.createElement('input')
  input.setAttribute('type', 'number')
  input.setAttribute('min', "1")
  input.setAttribute('max', "9999")
  input.setAttribute('id', 'newqty_'+x)
  input.value = qty
  const div = document.createElement("div")
  div.classList.add('editfield')
  div.appendChild(input)
  $("#"+x+"_qty_td").html(div)
}

/** submits a post request updating the qty of an item already in the inv */
function update(x, cell) {
  let newval = $("#newqty_"+x).val()
  const prevQty = cell.getAttribute('value')
  if (prevQty === newval) {
    const p = document.createElement("p")
    p.innerHTML = prevQty
    $("#"+x+"_qty_td").html(p)
  } else {
    newEntryObj = {
      "id": x,
      "qty": newval
    }
    loading(1)
    addtoinvPOST(newEntryObj)
  }
}

/** deletes an item from the inv */
function del(x) {
  newEntryObj = {
    "id": x,
    "qty": 0
  }
  loading(1)
  addtoinvPOST(newEntryObj)
}

/** submits a post request to add a substance to the inventory */
function addtoinvPOST(newEntryObj, x) {
  console.log(newEntryObj)
  $.post("/addtoinv", {
    "newEntry": JSON.stringify(newEntryObj)
  },
  function (data) {
    if (data !== "updated") {
      console.log(data)
      $("#noinv_tr").remove()
      $("#list_div > table").append(data)
      inventoryexists=true
      $("#navbar_process").removeClass('disabled_link')
      $("#calc_button").removeClass('button--disabled')
      loading(0)
    } else if (data === "updated") {
      location.reload()
    }
  });
clear(x)
}