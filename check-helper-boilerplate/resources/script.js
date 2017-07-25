
// This is the HTML that displays one item in the form. We use this template
// to add more.
new_item_html = '<div class="item">' +
                '<input type="text" class="item_name" name="item_name"></input>\n' +
                '<input type="text" class="item_price" name="item_price"></input>' +
                '</div>';

// Function that creates the various handlers that we'll need.
function associate_events() {
$('#remove_item').on('click', remove_last_item);
$('#add_item').on('click', add_item);
$('#submit_btn').click(send_check_and_print_result);
}

// Call the function associate_events only after the document is ready, so that
// all HTML objects exist in the DOM.
$(document).ready(
   associate_events
   //once its loaded the fcn above will appear
);

// Adds a new line for one item in the page.
function add_item(event) {
  $('#items').append(new_item_html);

  console.log("Press the + button");
}

// Removes the last line in the items list.
function remove_last_item(event) {
  $('.item').eq(-1).remove();
  //$("#items .item").last().remove() is also the same as above
  console.log("Press the - button");
}

// Prepares and sends the POST request, without reloading the page.
function send_check_and_print_result(event) {
  // We can use this function to validate the input before sending it.
  // Everything is validated, return true, and the browser will send the request
  // if we return false instead, the form will not be sent.
  if (!$('#tax_rate').val()){
    window.alert('we need a tax rate');
return false;
}
for (i=0;i<$('.item_price').length;i++){
  if (!$('.item_price').eq(i).val()){
    window.alert("you are missing the price for a item " + (i + 1));
    return false;
  }
}
  return true;
}
