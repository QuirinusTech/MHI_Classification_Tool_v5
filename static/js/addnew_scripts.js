/** function to hide the "AddNew" dialog box */
function hideaddnew() {
  document.getElementById('button_addnew').style.display = 'block'
  document.getElementById('addnewbox').style.display = 'none'
}


function UpdateSearchType(x) {
  $(".error").hide()
  $(".error").removeClass("flash")
  $("#addinfo_row").hide()

  clear()
  RemoveEmptyAcli()
  if (typeof x === 'undefined') {
    x = $("#searchtype").val()
  } else {
    $("#searchtype").val(x)
  }
  x = parseInt(x)
  console.log(x)
  
  switch (x) {
    case 0:
      $("#userinputfield").html("CAS Number:")
      show("addnew--usertextinput")
      hide("addnew--classselect")
      $("#listedSubstancesInfoRow").hide()
      break;
    case 1:
      $("#userinputfield").html("Substance name:")
      show("addnew--usertextinput")
      hide("addnew--classselect")
      break;
    case 2:
      $("#userinputfield").html("UN Number:")
      show("addnew--usertextinput")
      hide("addnew--classselect")
      break;
    case 3:
      hide("addnew--usertextinput")
      show("addnew--classselect")
      $("#hiddenInputs--chemtype").val("listed")
      break;
    default:
      console.log("case default")
      break;
    }
}

function GetSearchTypeName() {
  switch ($("#searchtype").val()) {
    case "0":
      return "CAS"
      break;
    case "1":
      return "name"
      break;
    case "2":
      return "UN"
      break;
    case "3":
      return "category"
      break;
    default:
      break;
  }
}

// autocomplete suggestions for named substances
function AutusCumpletus() {

  RemoveEmptyAcli()
  $(".error").hide()
  $(".error").removeClass("flash")
  $("#addinfo_row").hide()

  let text = $("#substance").val()
  text = text.replace(/[\s\,\-]+/g, '');

  if (text.length < 2) {
    // if user enters less than three characters
    show("threeCharsMin")
  }
  
  if ($("#searchtype").val() == 1 && text.length > 2) {
    // title
    let idlist = $("li.acli_1")
    for (let i = 0; i < idlist.length; i++) {
      let name = idlist[i].innerText
      name = name.replace(/[\s\,\-]+/g, '');
      for (let j = 0; j < name.length; j++) {
        if (name.slice(j, j + text.length).toUpperCase() === text.toUpperCase()) {
          $(idlist[i]).show()
        }
      }
      if ($(idlist[i]).attr("title")) {
        let title = $(idlist[i]).attr("title")
      
        for (let j = 0; j < title.length; j++) {
          if (title.slice(j, j + text.length).toUpperCase() === text.toUpperCase()) {
            $(idlist[i]).show()
          }
        }
      }
    }

  } else if (($("#searchtype").val() == 0 && text.length > 1)) {
    // CAS
    let idlist = $("li.acli_0")
    for (let i = 0; i < idlist.length; i++) {
      let name = idlist[i].innerText
      name = name.replace(/[\s\,\-]+/g, '');
      for (let j = 0; j < name.length; j++) {
        if (name.slice(j, j + text.length).toUpperCase() === text.toUpperCase()) {
          $(idlist[i]).show()
        }
      }
    }
  } else if (($("#searchtype").val() == 2 && text.length > 1)) {
    // CAS
    let idlist = $("li.acli_2")
    for (let i = 0; i < idlist.length; i++) {
      let name = idlist[i].innerText
      name = name.replace(/[\s\,\-]+/g, '');
      for (let j = 0; j < name.length; j++) {
        if (name.slice(j, j + text.length).toUpperCase() === text.toUpperCase()) {
          $(idlist[i]).show()
        }
      }
    }
  }

  // if no records are found
  if (!$(".acli").is(":visible") && text.length > 2) {
    show("NoRecords")
    $("#NoRecords").addClass("norecords")
  }

}

function RemoveEmptyAcli() {
  $("#NoRecords").removeClass("norecords")
  $(".acli").hide()
}

/** when clicking on a list item, populate the input field with the relevant info */
function populate(x) {
  
  let tempvar = $("#li_" + x)
  let text = $(tempvar).html()
  while (text[0] === " ") {
    text = text.slice(1)
  }

  if ($(tempvar).attr("chemtype")=="named") {
    $("#hiddenInputs--chemtype").val("named")
    $("#substance").attr("chemtype", "named")
  }
  $("#substance").val(text);
  $("#substance").addClass("flash")  

  console.log("tempvar = ")
  console.log(tempvar)
  console.log("text = " + text)


  $("#hiddenInputs--Category").val($(tempvar).attr("chemclass"))
  
  if (x.slice(0,4) == "cas_") {
    $("#substance").attr("chemid", x.slice(4))
    $("#hiddenInputs--chemid").val(x.slice(4))
  } else if (x.slice(0,3) == "UN_") {
    $("#substance").attr("chemid", x.slice(3))
    $("#hiddenInputs--chemid").val(x.slice(3))
  } else {
    $("#substance").attr("chemid", x)
    $("#hiddenInputs--chemid").val(x)
  }
  if ($(tempvar).attr("flammable")=="True") {
    $("#flammableLiquidWarning").show()
    $("#flammableLiquidWarning").addClass("flash")
  }

  let title = $(tempvar).attr("title")
  console.log(title)
  let y = $("#hiddenInputs--chemid").val()
  if (y == "390010208290") {
    show('note7table')
    $("#addinfo_row").hide()
  } else if (title !== undefined) {
    $("#addinfo_row").show()
    $("#hiddenInputs--additionalInfo").html(title)
  } else if (title === undefined) {
    $("#addinfo_row").hide()
  } else {
    $("#addinfo_row").hide()
  }

  $(".acli").hide()
  $("#qty").focus()
}

/** when clicking on a list item, populate the input field with the relevant info */
function populateListed(x) {
  UpdateSearchType(1)
  $("#substance").attr("chemtype", "listed")
  $("#substance").attr("chemid", x["chemid"])
  $("#listedSubstancesInfoRow").show()
  $("#hiddenInputs--chemid").val(x["chemid"])
  $("#hiddenInputs--chemtype").val("listed")
  $("#hiddenInputs--Category").val(x["category"])
  let hphrasesstring = ""
  x["hazardPhrases"].forEach(element => {
    hphrasesstring = hphrasesstring + element + ", "
  });
  hphrasesstring = hphrasesstring.slice(0, -2)
  $("#hiddenInputs--hphrases").val(hphrasesstring)
  $("#substance").val(x["recordTitle"])
  $("#substance").addClass("flash")
  $(".acli").hide()
  loading(0)
  if ($("#qty").val() === "") {
    $("#qty").focus()
  } else {
    $("#addtoinv_btn".focus())
  }
}

function ShowAddInfo() {
  chemid = $("#category").val()
  categories = Array.from($(".categoryType"))
  let title = null

  categories.forEach(category => {
    if ($(category).attr('chemid') == chemid) {
      title = $(category).attr("title")
    }
  })

      let y = $("#hiddenInputs--chemid").val()
      if (title !== undefined && title !== null) {
        $("#addinfo_row").show()
        $("#hiddenInputs--additionalInfo").html(title)
      } else {
        $("#addinfo_row").hide()
      }
}

/** uses regex to validate the user input where x is the current tab */
function checkinputs() {

  let qtyTest = false
  let substanceTest = false

  let substance = $("#substance").val()

  switch ($("#searchtype").val()) {
    case "0":
      var validcasregex = /^[\d]{1,5}\-[\d]{1,5}\-[\d]{1,5}$/;
      if (substance.length > 4 && new RegExp(validcasregex).test(substance)) {
        substanceTest = true
      } else {
        $("#substance").addClass("invalid_input");
      }
      break;

    case "1":
      // test substance
      var letterNumberDashSpace = /^[0-9a-zA-Z,\-\s\/\\\(\)]+$/;
      if (substance.length > 2 && new RegExp(letterNumberDashSpace).test(substance)) {
        substanceTest = true
      } else {
        $("#substance").addClass("invalid_input");
      }
      break;
    case "2":
      case "0":
        var unNumberRegex = /^[\d]{4}$/;
        if (substance.length == 4 && new RegExp(unNumberRegex).test(substance)) {
          substanceTest = true
        } else {
          $("#substance").addClass("invalid_input");
        }
        break;

    case "3":
      if ($("#class").val() !== "") {
        substanceTest = true
      } else {
        $("#class").addClass("invalid_input");
      }
      break;
  }

  // test qty
  let qty = $("#qty").val()
  var numbers = /^[0-9\.\,]+$/
  if (qty > 0 && new RegExp(numbers).test(qty)) {
      qtyTest = true
  } else {
      $("#qty").addClass("invalid_input");
  }
    
  // final check
  if (!substanceTest || !qtyTest) {
    return false
  } else if(substanceTest === true && qtyTest === true) {
    return true
  }
}

/** clears the input fields */
function clear() {
  $("#listedSubstancesInfoRow").hide()
  $(".acli").hide()
  $("#substance").val("");
  $("#qty").val("")
  $("#class").val("")
  $("#type").val("")
  $(".flash").removeClass("flash")
}



/** using the input fields, adds a substance to the inventory */
function addtoinv() {
  if (checkinputs() === false) {
    popUp("Please check that you've entered valid information into the fields above.", "Error")
  } else {
    $(".error").hide()
    $(".error").removeClass("flash")
    $("#addinfo_row").hide()
    loading(1)

    var d = new Date()
    var substid = "substid_" + d.getDate().toString() + d.getHours() + d.getMinutes() + d.getSeconds()
    
    var chemid, name;
    if ($("#searchtype").val() == "3") {
      chemid = $("#category").val()
      name = chemid
    } else {
      chemid = $("#hiddenInputs--chemid").val()   
      name = $("#substance").val()
    }

    var chemtype = $("#hiddenInputs--chemtype").val();
    var hphrases = "";
    if (chemtype === "listed") {
      hphrases = $("#hiddenInputs--hphrases").val()
    }

    field = GetSearchTypeName()

    newEntryObj = {
      "id": substid,
      "chemid": chemid,
      "chemtype": chemtype,
      "qty": $("#qty").val(),
      "hazardPhrases": hphrases,
      "name": name,
      "field": field
    }
    $("#listedSubstancesInfoRow").hide()
    
    addtoinvPOST(newEntryObj)
  }
}

function ListedSubstanceSearch() {
  substanceFieldInputValue = $("#substance").val()
  popUp("Searching for \""+substanceFieldInputValue+"\".", "info")
  field = GetSearchTypeName()
  updateh(field, substanceFieldInputValue)
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
  input.setAttribute('min', "0")
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
        if (data.substr(0,6) == "Error:") {
          heading = "An Error has occurred: "
          string = data.substr(6)
          popUp(string, data)
          loading(0)
        } else {
          $("#noinv_tr").remove()
          $("#list_div > table").append(data)
          inventoryexists = true
          $("#calc_button").removeClass('disabled_button')
          loading(0)
        }
      clear()
    });
}

/** searchtype = CAS/name/UN,  */
async function updateh(searchtype,subst) {
  loading(1)
  var x = {"searchtype": searchtype, "field": subst}

  $.post("/updatehphrases", {
      "substance": JSON.stringify(x)
    }, function(data) {
      //data = JSON.parse(data)
      if (data["found"] === true && data["foundresult"] === "final") {
        populateListed(data)
      } else {
        // couldn't find anything with the given info
        UpdateSearchType(3)
        loading(0)
        $("#galapagosMessage").slideDown()
        $("#galapagosMessage").addClass('flash')
      }
    });
}
