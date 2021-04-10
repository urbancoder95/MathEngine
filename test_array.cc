#include <iostream>
#include "math_engine/src/array.h"

void print_vector(std::vector<int>& ref){
    for(int i : ref){
        std::cout << i << '\t';
    }
    std::cout << std::endl;
}

int main(){
    std::vector<int> myVec = {1, 2, 3, 4};
    std::cout << "Defined a vector viz.:- " << std::endl;
    print_vector(myVec);

    std::cout << std::endl;

    // Create array object
    array my_obj(myVec);
    std::cout << "Array object visualization:- " << std::endl;
    std::cout << my_obj << std::endl << std::endl;

    std::cout << "Sum of all elements in the array is " << my_obj.sum() << "." << std::endl;

    std::cout << "Mean of all elements in the array is " << my_obj.mean() << "." << std::endl;

    return 0;
}
