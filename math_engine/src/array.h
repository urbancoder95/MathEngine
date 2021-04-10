#include <vector>

class array{
    public:
        array(std::vector<int> vec);
        ~array();
        int shape;
        float mean();
        int sum();
        std::vector<int>& get_data();
        friend std::ostream& operator<<(std::ostream &out, const array& data);
    private:
        std::vector<int> data;
};

// array::sum(){
//     return 1;
// }
