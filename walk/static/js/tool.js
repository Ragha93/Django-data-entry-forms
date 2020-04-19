function opentool(evt, toolName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(toolName).style.display = "block";
  evt.currentTarget.className += " active";
}




// To Enable or Disable textbox Image******************************
$('[name="asinmainimage"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment8"]').show();
}
else {
  $('[name="comment8"]').hide();
}
})

$('[name="asinmainimagewhitebg"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment9"]').show();
}
else {
  $('[name="comment9"]').hide();
}
})

$('[name="asinimageborderwatermanrtextcheck"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment10"]').show();
}
else {
  $('[name="comment10"]').hide();
}
})



$('[name="asinimagematchtitle"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment11"]').show();
}
else {
  $('[name="comment11"]').hide();
}
})


$('[name="asinimagematchcolorsize"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment12"]').show();
}
else {
  $('[name="comment12"]').hide();
}
})


$('[name="asinimageplaceholdercheck"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment13"]').show();
}
else {
  $('[name="comment13"]').hide();
}
})


$('[name="asinimagegraphratings"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment14"]').show();
}
else {
  $('[name="comment14"]').hide();
}
})


$('[name="asinimagepromotextcheck"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment15"]').show();
}
else {
  $('[name="comment15"]').hide();
}
})


$('[name="asinimagecustomerdepict"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment16"]').show();
}
else {
  $('[name="comment16"]').hide();
}
})
// To Enable or Disable textboxImage******************************
// To Enable or Disable title*************************************
$('[name="asinreflectproduct"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment5"]').show();
}
else {
  $('[name="comment5"]').hide();
}
})


$('[name="asinnomismatchbtwnattributes"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment6"]').show();
}
else {
  $('[name="comment6"]').hide();
}
})


$('[name="asintitleguideline"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment7"]').show();
}
else {
  $('[name="comment7"]').hide();
}
})
// To Enable or Disable title*************************************

// To Enable or Disable bullet*************************************
$('[name="asinbulltpointrelevant"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment19"]').show();
}
else {
  $('[name="comment19"]').hide();
}
})

$('[name="asinbulletwarrantyinfo"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment20"]').show();
}
else {
  $('[name="comment20"]').hide();
}
})

$('[name="asinbulletshort"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment21"]').show();
}
else {
  $('[name="comment21"]').hide();
}
})

$('[name="asinbulletnumerals"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment22"]').show();
}
else {
  $('[name="comment22"]').hide();
}
})
// To Enable or Disable bullet*************************************

// To Enable or Disable category***********************************
$('[name="asincorrectcategory"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment4"]').show();
}
else {
  $('[name="comment4"]').hide();
}
})
// To Enable or Disable category***********************************

// To Enable or Disable brandname***********************************
$('[name="asinbrandnamecorrect"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment17"]').show();
}
else {
  $('[name="comment17"]').hide();
}
})

$('[name="asinbrandhyperlink"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment18"]').show();
}
else {
  $('[name="comment18"]').hide();
}
})
// To Enable or Disable brandname***********************************

// To Enable or Disable release*************************************
$('[name="asinreleasedate1"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment23"]').show();
}
else {
  $('[name="comment23"]').hide();
}
})
// To Enable or Disable release*************************************

// To Enable or Disable A+******************************************
$('[name="asinsiteadescstatus"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment29"]').show();
}
else {
  $('[name="comment29"]').hide();
}
})

$('[name="asinapluscontent"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment30"]').show();
}
else {
  $('[name="comment30"]').hide();
}
})

$('[name="asinrelevantproduct"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment31"]').show();
}
else {
  $('[name="comment31"]').hide();
}
})
// To Enable or Disable A+******************************************

// To Enable or Disable variation***********************************
$('[name="asinvariationcheck"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment24"]').show();
}
else {
  $('[name="comment24"]').hide();
}
})

$('[name="asincolorname"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment25"]').show();
}
else {
  $('[name="comment25"]').hide();
}
})

$('[name="asinsizecheck"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment27"]').show();
}
else {
  $('[name="comment27"]').hide();
}
})

$('[name="asinvariationword"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment34"]').show();
}
else {
  $('[name="comment34"]').hide();
}
})

// To Enable or Disable variation***********************************

// To Enable or Disable keywords************************************

$('[name="asinsearchable"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment1"]').show();
}
else {
  $('[name="comment1"]').hide();
}
})
$('[name="asinretailcontribution"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment2"]').show();
}
else {
  $('[name="comment2"]').hide();
}
})
$('[name="asinobsolete"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment3"]').show();
}
else {
  $('[name="comment3"]').hide();
}
})
$('[name="asinkeyword"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment33"]').show();
}
else {
  $('[name="comment33"]').hide();
}
})
$('[name="asinleafnode"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment35"]').show();
}
else {
  $('[name="comment35"]').hide();
}
})
// To Enable or Disable keywords************************************

// To Enable or Disable orphan tab**********************************
$('[name="asinappropriate"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment32"]').show();
}
else {
  $('[name="comment32"]').hide();
}
})
$('[name="asinnotorphan"]').change(function () {
var end = this.value;
if (end == 'Error'){
  $('[name="comment28"]').show();
}
else {
  $('[name="comment28"]').hide();
}
})
// To Enable or Disable orphan tab**********************************

// To Disable fields****************************************
// $(document).ready(function(){
//     $("#id_asin").hover(function(){
//         myFunction();
//     });
// });
// function myFunction() {
//   document.getElementById("id_asin").disabled = true;
// }
// To Disable fields*****************************************
// <!-- <a class="btn btn-outline-warning" href="{% url 'detail' update.id %}">Currently Viewing {{update.id}} : {{update.asin}}</a>
// <a class="btn btn-outline-warning" href="{% url 'walkapp:registerinfo' %}" id="allocatedto"> Allocated To: {{update.allocatedto}}</a>
// <a class="btn btn-outline-warning" href="{% url 'listasins' %}" id="allocatedon">Allocated on: {{update.allocationdate}}</a></li> -->
//   <!-- No property in CSS to leave space, if found please replace here between first and second anchor tag -->
// <!-- <a class="btn btn-outline-warning" href="" target="_blank">Currently Viewing ASIN ({{form.asin.id}} out of 100) : {{form.asin}}</a> -->
