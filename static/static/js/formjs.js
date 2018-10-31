function changeBorder(){
  var getForm = document.getElementById('clientForm');
  var el = getForm.getElementsByTagName('select');
  for (var i = 0; i < el.length; i++) {
    console.log(i);
    if (el[i].selectedIndex == 0) {
      console.log(el[i]);
      el[i][0].setAttribute('disabled','disabled');
    }
  }
}
