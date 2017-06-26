var total  = parseInt($(".pagination").attr("child")) + 1
var index = 1
var color = "#03a9f4 light-blue"
$(".pagination > .waves-effect#1").attr("class", "active " + color)


$(".pagination >.waves-effect").click(function(){
    if($(this).attr("id") != "0" && $(this).attr("id") != "-1" ){
      $(".pagination >.active").attr("class", "waves-effect");
      $(this).attr("class", "active " + color);
      index = parseInt($(this).attr("id"))
    };
});


$(".pagination >.active").click('click',function(){
  var text_value = $(this).text();
  text_value = text_value.toString().trim()
  if($(this).attr("id") != "0" && $(this).attr("id") != "-1") {
    $(".pagination >.active").attr("class", "waves-effect");
    $(this).attr("class", "active " + color);
    index = parseInt($(this).attr("id"))
  };
});


$(".pagination >.waves-effect#-1").click('click',function(){
  $(".pagination >.active").attr("class", "waves-effect");
  index  = (index + 1) % total;
  if(index==0) index = 1;
  $(".pagination >.waves-effect#"+index).attr("class", "active " + color);
});

$(".pagination >.waves-effect#0").click('click',function(){
  $(".pagination >.active").attr("class", "waves-effect");
  index  = (index - 1);
  if(index==0) index = parseInt(total) - 1;
  $(".pagination >.waves-effect#"+index).attr("class", "active " + color);
});
