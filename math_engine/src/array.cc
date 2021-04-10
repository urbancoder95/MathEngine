/*
Definitions for array class. For now we create the methods for mean and sum. 
*/

#include <iostream>
#include <cmath>
#include "array.h"

// Constructor definition. 
array::array(std::vector<int> vec){
    data = vec;
    shape = vec.size();
}

// Destructor definition. Allocate null and clear shape. 
array::~array(){
    data = {};
    shape = 0;
}

// Define a getter method to get the vector data
std::vector<int>& array::get_data(){
    return data;
}

// Sum of all elements
int array::sum(){
    int s = 0;
    for(int i : get_data()){
        s += i;
    }
    return s;
}

// Mean/average of all elements in the array
float array::mean(){
    return sum() / (float)shape;
}

// Define a custom output stream return string.
std::ostream& operator<<(std::ostream &out, const array& data) {
    array& ref = const_cast<array&>(data);
    out << "array([";
    std::vector<int>& vec = ref.get_data();
    for(int i = 0; i < ref.shape; i++){
        out << vec[i];
        if(i < ref.shape - 1) out << '\t';
    }
    out << ")]" << std::endl;
    return out;
}
