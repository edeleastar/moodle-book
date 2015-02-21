
$(document).ready(function()
{
  $("img").addClass ("img-responsive");

  $(".tab-content img").each(function()
  {
    var title = this.alt;
    $(this).after('<figcaption class="caption"> <em>'+ title +'</em></figcaption>');
  });
})
