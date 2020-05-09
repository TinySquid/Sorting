//* Selection Sort
function selection_sort(arr) {
  let smallest_index;
  let temp;

  for (let i = 0; i < arr.length - 1; i++) {
    smallest_index = i;
    temp = arr[i]; // For swapping

    for (let cur_index = smallest_index + 1; cur_index < arr.length; cur_index++) {
      if (arr[smallest_index] > arr[cur_index]) {
        smallest_index = cur_index;
      }
    }

    //Swap elements
    arr[i] = arr[smallest_index];
    arr[smallest_index] = temp;
  }

  return arr;
}

console.log("Selection Sort : ", selection_sort([6, 1, 4, 5, 3, 0, 2]));

//* Bubble Sort
function bubble_sort(arr) {
  let didSwap = true;
  let temp;

  while (didSwap) {
    didSwap = false;
    for (let i = 0; i < arr.length - 1; i++) {
      temp = arr[i];
      if (arr[i] > arr[i + 1]) {
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        didSwap = true;
      }
    }
  }

  return arr;
}

console.log("Bubble Sort: ", bubble_sort([6, 1, 4, 5, 3, 0, 2]));
