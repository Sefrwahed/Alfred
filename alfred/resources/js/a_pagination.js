var total  = parseInt($(".pagination").attr("child")) + 1
var index = 1
var color = "#03a9f4 light-blue"
$(".waves-effect#1").attr("class", "active " + color)


$(".waves-effect").click(function(){
    if($(this).attr("id") != "0" && $(this).attr("id") != "-1" ){
      $(".active").attr("class", "waves-effect");
      $(this).attr("class", "active " + color);
      index = parseInt($(this).attr("id"))
    };
});


$(".active").click('click',function(){
  var text_value = $(this).text();
  text_value = text_value.toString().trim()
  if($(this).attr("id") != "0" && $(this).attr("id") != "-1") {
    $(".active").attr("class", "waves-effect");
    $(this).attr("class", "active " + color);
    index = parseInt($(this).attr("id"))
  };
});


$(".waves-effect#-1").click('click',function(){
  $(".active").attr("class", "waves-effect");
  index  = (index + 1) % total;
  if(index==0) index = 1;
  $(".waves-effect#"+index).attr("class", "active " + color);
});

$(".waves-effect#0").click('click',function(){
  $(".active").attr("class", "waves-effect");
  index  = (index - 1);
  if(index==0) index = parseInt(total) - 1;
  $(".waves-effect#"+index).attr("class", "active " + color);
});
