var arr = [220, 63, 25, 8, 5, 7, 295, 589];

for (var i = 0; i < arr.length; i++) {

 for (var j = 0; j < (arr.length - i - 1); j++) {

  if (arr[j] > arr[j + 1]) {

  var temp = arr[j]

 
  arr[j] = arr[j + 1]

  arr[j + 1] = temp;

  }}}

  console.log(arr);