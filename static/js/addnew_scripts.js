/** Global variable */
let updateHPhrasesControllerresultsvariable = ""

/** function to hide the "AddNew" dialog box */
function hideaddnew() {
  document.getElementById('button_addnew').style.display = 'block'
  document.getElementById('addnewbox').style.display = 'none'
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
  text = text.replace(/[\s\,\-]+/g, '');
  if (text.length > 2) {
    let idlist = $("li.acli")
    for (let i = 0; i < idlist.length; i++) {
      let name = idlist[i].innerText
      let title = $(idlist[i]).attr("title")
      name = name.replace(/[\s\,\-]+/g, '');
      title = title.replace(/[\s\,\-]+/g, '');
      for (let j = 0; j < name.length; j++) {
        if (name.slice(j, j + text.length).toUpperCase() === text.toUpperCase()) {
          $(idlist[i]).show()
        }
      }
      for (let k = 0; k < title.length; k++) {
        if (title.slice(k, k + text.length).toUpperCase() === text.toUpperCase()) {
          $(idlist[i]).show()
        }
      }
    }
    // if no records are found
    if (!$(".acli").is(":visible")) {
      show("NoRecords")
    }
  } else {
    // if user enters less than three characters
    show("threeCharsMin")
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
function checkinputs(x) {
  var letterNumberDashSpace = /^[0-9a-zA-Z\-\s\/\\\(\)]+$/;
  var numbers = /^[0-9]+$/

  // named substance
  if (x == 1) {
    let substance_1 = $("#substance_1").val()
    let qty_1 = Math.floor($("#qty_1").val())
    if (substance_1.length > 5 && qty_1 > 0) {
      if (new RegExp(letterNumberDashSpace).test(substance_1) && new RegExp(numbers).test(qty_1)) {
        return true
      } else {
        $("#substance_1").addClass("invalid_input");
      }
    } else {
      return false
    }
    // listed substance
  } else if (x == 2) {
    let substance_2 = $("#substance_2").val()

    // test substance 2 name
    if (new RegExp(letterNumberDashSpace).test(substance_2)) {
      test_2_1 = true
    } else {
      $("#substance_2").addClass("invalid_input");

      // if the substance fails validation, also test the CAS
      var validcasregex = /^[\d]{1,5}\-[\d]{1,5}\-[\d]{1,5}$/;
      if (new RegExp(validcasregex).test($("#cas_2").val())) {
        test_2_1 = true;
      } else {
        $("#cas_2").addClass("invalid_input");
      }
    }
    
    // check that the user selected a class
    if ($("#class_2").val() === ""){
      test_2_2 = false
      $("#class_2").addClass("invalid_input");
    } else {
      test_2_2 = true
    }

    // check that the user entered a value
    if (new RegExp(numbers).test($("#qty_2").val())){
      test_2_3 = true
    } else {
      test_2_3 = false
      $("#qty_2").addClass("invalid_input");
    }

    // summary test to check all values entered
    if (test_2_1 === true && test_2_2 === true && test_2_3 === true) {
      $(".invalid_input").removeClass("invalid_input")  
      return true
    } else {
      return false
    }
  }
  return false
}

/** clears the input fields */
function clear() {
  $("#substance_1").val("");
  $("#qty_1").val("")
  $("#class_1").val("")
  $("#type_1").val("")
  $("#substance_2").val("")
  $("#qty_2").val("")
  $("#class_2").val("")
  $("#type_2").val("")
  $(".flash").removeClass("flash")
}



/** using the input fields, adds a substance to the inventory */
function addtoinv() {
  let x = $("div.active_tab").attr("value")

  if (checkinputs(x) === false) {
    alert("Please check that you've entered valid information into the fields above.")
  } else {
    loading(1)
    d = new Date()
    substid = "custom_" + d.getDate().toString() + d.getHours() + d.getMinutes() + d.getSeconds()
    if (x == 2) {
      if (confirm("Finding information for a custom substance can take up to 45 seconds in some cases. Continue?")) {
        chemid = $("#class_2").val()
        qty = $("#qty_2").val()
        substname = $("#substance_2").val()
        cas = $("#cas_2").val()

        newEntryObj = {
          "id": substid,
          "name": substname,
          "CAS": cas,
          "qty": Math.floor(qty),
          "chemid": chemid,
          "type": "listed"
        }
        updateh(newEntryObj)
      } else {
        return false
      }
    } else if (x==1) {
      id = $("#substance_1").attr("chemid")
      qty = $("#qty_1").val()
      newEntryObj = {
        "id": substid,
        "chemid": $("#substance_1").attr("chemid"),
        "qty": qty,
        "type": "named"
      }
      addtoinvPOST(newEntryObj)
    }
  }
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
    x = Math.floor(x)
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
    updatePost(newEntryObj)
  }
}

/** deletes an item from the inv */
function del(x) {
  delObj = {
    "id": x,
    "qty": 0
  }
  loading(1)
  updatePost(delObj)
}

function updatePost(Obj) {
  jsonstring = JSON.stringify(Obj)
  $.post("/update", {
      "update": jsonstring
    },
    function () {
        loading(0)
        location.reload()
    });
}

/** submits a post request to add a substance to the inventory */
function addtoinvPOST(newEntryObj) {
  newEntry = JSON.stringify(newEntryObj)
  $.post("/addtoinv", {
      "newEntry": newEntry
    },
    function (data) {
        $("#noinv_tr").remove()
        $("#list_div > table").append(data)
        inventoryexists = true
        $("#calc_button").removeClass('disabled_button')
        loading(0)
      clear()
    });
}

/** object must include either a "CAS" key or a "name" key */
async function updateh(x) {
  const readyObj = {...x}
  var validcasregex = /^[\d]{1,5}\-[\d]{1,5}\-[\d]{1,5}$/;
  if (new RegExp(validcasregex).test(x["CAS"])) {
    x["searchtype"] = "CAS";
  } else {
    x["searchtype"] = "name";
  }

  $.post("/updatehphrases", {
      "substance": JSON.stringify(x)
    }, function(data) {
      data = JSON.parse(data)
      if (data["foundresult"] == "named") {
        readyObj["hphrases"] = data["hphrases"]
        if (data["recordTitle"] && readyObj["name"].toUpperCase() != data["recordTitle"].toUpperCase()) {
          readyObj["name"] = newEntryObj["name"] + " (" + data["recordTitle"] + ")"
        }
        readyObj["hphrases"] = data["hphrases"]
        $("#status_message").html("Substance found under named substances.")
        addtoinvPOST(readyObj)
      }
      // successful information retrieval
      else if (data["found"] === true && data["foundresult"] !== "named") {
        // search complete, h-phrases found
          readyObj["hphrases"] = data["hphrases"]
          if (data["recordTitle"] && readyObj["name"].toUpperCase() != data["recordTitle"].toUpperCase()) {
            readyObj["name"] = newEntryObj["name"] + " (" + data["recordTitle"] + ")"
          }
          addtoinvPOST(readyObj)
        }
      // couldn't find anything with the given info
      else {
        errorMsg = 'We were unable to corroborate the given information. Please see error code "Galapagos" on our FAQ page for more info.'
        alert(errorMsg)
        addtoinvPOST(readyObj)
      }
    });
}

