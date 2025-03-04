/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return left;    
};

console.log( 'Answer1 :' , checkAns1 = searchInsert( nums = [ 1, 3, 5, 6 ], target = 5 ) )
console.log( 'Answer2 :' , checkAns2 = searchInsert( nums = [ 1, 3, 5, 6 ], target = 2 ) )
console.log( 'Answer3 :' , checkAns3 = searchInsert( nums = [ 1, 3, 5, 6 ], target = 7 ) )
console.log( 'Answer4 :' , checkAns4 = searchInsert( nums = [ 1, 3, 5, 6 ], target = 0 ) )
console.log( 'Answer5 :' , checkAns5 = searchInsert( nums = [ ], target = 0 ) )
console.log( 'Answer6 :', checkAns6 = searchInsert( nums = [ 1 ], target = 1 ) )
console.log( 'Answer7 :', checkAns7 = searchInsert( nums = [ 1 ], target = 2 ) )
console.log( 'Answer8 :', checkAns8 = searchInsert( nums = [ 1, 3 ], target = 1 ) )



// var searchInsert = function(nums, target) {
//     // check if there are none target element 
//     if( nums.length == 0 || target == 0 ){
//         return 0
//     }

//     // check if there are one element
//     if( nums.length == 1 ){
//         if( target <= nums[ 0 ] ){
//             return 0
//         }
//         else if( target > nums[ 0 ] ){
//             return 1
//         }
//     }

//     // check if there are more than one elemnet
//     let stockValue = 0;
//     for( const element in nums ){
//         if( nums[ element ] >= target ){
//             if( nums[ element ] == target ){
//                 return parseInt( stockValue );
//             }
//             else if( nums[ element ] > target ){
//                 return parseInt( stockValue ) + 1;
//             }
            
//         }
//         else if( target > nums[ nums.length - 1 ] ){
//             return nums.length 
//         }
//         else{
//             stockValue = element;
//         }
//     }
// };