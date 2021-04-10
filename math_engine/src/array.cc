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
std::vector<int>& get_data(){
    return &data;
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
    return sum() / shape;
}

// Define a custom output stream return string.
std::ostream& array::operator<<(std::ostream &out, array const& data) {
    out << "array([" << ':';
    std::vector<int>& vec = data.get_data();
    for(int i = 0; i < shape; i++){
        out << &vec[i];
        if(i < shape) out << '\t';
    }
    out << ")]" << std::endl;
    return out;
}


int main(){
    std::vector<int> myVec = {1, 2, 3, 4}
    array obj = new array(myVec);
    std::cout << obj;
    return 0;
}