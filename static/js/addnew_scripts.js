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

  if (x == 1) {
    let substance_1 = $("#substance_1").val()
    let qty_1 = $("#qty_1").val()
    if (substance_1.length > 5 && qty_1 > 0) {
      if (new RegExp(letterNumberDashSpace).test(substance_1) && new RegExp(numbers).test(qty_1)) {
        return true
      }
    } else {
      return false
    }
  } else if (x == 2) {
    let substance_2 = $("#substance_2").val()
    if (substance_2.length > 4) {
      test_2_1 = new RegExp(letterNumberDashSpace).test($("#substance_2").val()) ? true : false
      test_2_2 = $("#class_2").val() !== "" ? true : false
      test_2_3 = new RegExp(numbers).test($("#qty_2").val()) ? true : false
      if (test_2_1 === true && test_2_2 === true && test_2_3 === true) {
        return true
      }
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
          "qty": qty,
          "chemid": chemid,
          "type": "listed"
        }
        UpdateHPhrasesController(newEntryObj)
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
  console.log(Obj)
  jsonstring = JSON.stringify(Obj)
  $.post("/update", {
      "update": jsonstring
    },
    function (data) {
        console.log(data)
        loading(0)
        location.reload()
    });
}

/** submits a post request to add a substance to the inventory */
function addtoinvPOST(newEntryObj) {
  console.log(newEntryObj)
  newEntry = JSON.stringify(newEntryObj)
  $.post("/addtoinv", {
      "newEntry": newEntry
    },
    function (data) {
        console.log(data)
        $("#noinv_tr").remove()
        $("#list_div > table").append(data)
        inventoryexists = true
        $("#calc_button").removeClass('disabled_button')
        loading(0)
      clear()
    });
}
function UpdateHPhrasesController(newEntryObj) {

  // init with temporary var

  // Shaun - the variable below is being declaired in the global scope which is to be avoided since it can easily be overwritten if another variable called x is decalred in the global scope
  // Shaun - A better way to copy objects are with the spread operator "...", what you are doing below is assigning the var x to the same object in memory, so when you change a value oon  it will be changed on newEntryObj

  // x = newEntryObj
  // x["hphrases"] = "";
  // x["cid"] = "";

  // Shaun - Below creates a local object with the keys and values spread into x
  const x = {...newEntryObj}
  x["hphrases"] = "";
  x["cid"] = "";

  // Shaun - Did the same here just in case havent seen what your doing with it yet but usually doesnt do any harm

  // let readyObj = newEntryObj

  let readyObj = {...newEntryObj}
  let error = false
  let done = false
  var validcasregex = /^[\d]{1,4}\-[\d]{1,4}\-[\d]{1,4}$/;

  if (new RegExp(validcasregex).test(x["CAS"])) {
    x["searchtype"] = "CAS";
    barwidth(5)
  } else {
    x["searchtype"] = "name";
    barwidth(45)
  }

  // first call

  // Shaun - Global var to be avoided
  // After commenting everything out except 'results = updateh(x)' it returned undefined, then i noticed you werent returning anything in the updateh function, when you say var name = function, the function has to return something to assign to the variable
  // results = updateh(x)

  updateh(x).then((results) => {
    console.log(results)
    if (results["found"] == true && results["foundresult"] == "named") {
      readyObj["hphrases"] = results["hphrases"]
      if (readyObj["name"] != results["recordTitle"]) {
        readyObj["name"] = newEntryObj["name"] + " (" + results["recordTitle"] + ")"
      }
      readyObj["hphrases"] = results["hphrases"]
      addtoinvPOST(readyObj)
    }
    if (results["found"] === false && results["retry"] == true) {
      // Coudn´t find a substance with the CAS number, retry with substance name
      barwidth(25)
      x["searchtype"] = "name";
      results = updateh(x)
    }
    if (results["found"] === false && results["retry"] == false) {
      // no results for name or cas number
      error = true
      errorMsg = 'We were unable to find any information for this substance name or CAS number. Please see error code "Galapagos" on the FAQ page.'
    }
    if (results["found"] === true) {
      // found either cid or h-phrases
      if (results["foundresult"] == "cid" && results["cid"].length() > 1) {
        barwidth(50)
        x["cid"] = results["cid"]
        x["searchtype"] = "cid";
        // final call with cid to get h-phrases
        results = updateh(x)
      }
      else if (results["foundresult"] == "final") {
        // search complete, h-phrases found
        barwidth(90)
        x["hphrases"] = results["hphrases"]
        x["name"] = x["name"] + " (" + results["recordTitle"] + ")"
        done = True
      }
    }
    }
  )
  














//   for (let index = 0; index < 15; index++) {
//     setTimeout(() => {
//       if (results != null) {
//         index = 15
//       }
//       else if (results === null && index == 14) {
//         fail = true
//       }
//     }, 1000);
//   }
  
// while (done === false) {
//   if (!fail) {
//     if (results["found"] == true && results["foundresult"] == "named") {
//       readyObj["hphrases"] = results["hphrases"]
//       if (readyObj["name"] != results["recordTitle"]) {
//         readyObj["name"] = newEntryObj["name"] + " (" + results["recordTitle"] + ")"
//       }
//       readyObj["hphrases"] = results["hphrases"]
//       addtoinvPOST(readyObj)
//     }
//     if (results["found"] === false && results["retry"] == true) {
//       // Coudn´t find a substance with the CAS number, retry with substance name
//       barwidth(25)
//       x["searchtype"] = "name";
//       results = updateh(x)
//     }
//     if (results["found"] === false && results["retry"] == false) {
//       // no results for name or cas number
//       error = true
//       errorMsg = 'We were unable to find any information for this substance name or CAS number. Please see error code "Galapagos" on the FAQ page.'
//     }
//     if (results["found"] === true) {
//       // found either cid or h-phrases
//       if (results["foundresult"] == "cid" && results["cid"].length() > 1) {
//         barwidth(50)
//         x["cid"] = results["cid"]
//         x["searchtype"] = "cid";
//         // final call with cid to get h-phrases
//         results = updateh(x)
//       }
//       else if (results["foundresult"] == "final") {
//         // search complete, h-phrases found
//         barwidth(90)
//         x["hphrases"] = results["hphrases"]
//         x["name"] = x["name"] + " (" + results["recordTitle"] + ")"
//         done = True
//       }
//     }
//   } else {
//     done = true
//     error = true
//     errorMsg = "Failure to obtain information from server"
//   }
// }

    

//   if (done === true && error === false) {
//     let readyObj = newEntryObj
//     readyObj["id"] = x["id"];
//     readyObj["name"] = x["name"]
//     readyObj["hphrases"] = x["hphrases"]
//     addtoinvPOST(readyObj)
//   }
//   else if (done === true && error === true) {
//     alert(errorMsg)
//     addtoinvPOST(readyObj)
//   }
}

/** object must include either a "CAS" key or a "name" key */

// Shaun - redid this part to test but rememeber to return something always

// function updateh(x) {
//   console.log(x)
//   $.post("/updatehphrases", {
//       "substance": JSON.stringify(x)
//     },
//     function(data) {
//       console.log('Response from server: ')
//       console.log(data)
//       updateHPhrasesControllerresultsvariable = data
//     });
// }

async function updateh(x) { 
  const data = await $.post("/updatehphrases", {
             "substance": JSON.stringify(x)
           })
  updateHPhrasesControllerresultsvariable = data
  return data
}

function barwidth(param) {
  console.log("Barwidth = " + param)
  $("#pre_loader").val(param)
}