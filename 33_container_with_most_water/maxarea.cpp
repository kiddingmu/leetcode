#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        int size = height.size();
        int left = 0;
        int right = size - 1;
        int result = 0;
        while (left < right) {
            int left_val = height[left];
            int right_val = height[right];
            int cur_area = (right - left) * (left_val < right_val ? left_val : right_val);
            if (cur_area > result)
                result = cur_area;
            if (left_val < right_val)
                left += 1;
            else
                right -= 1;
        }
        return result;
    }
};

int main() {
    Solution solution;
    vector<int> height;
    int h_array[] = {2,4,8,4,5};
    for (int i = 0; i < sizeof(h_array)/sizeof(int); i++)
        height.push_back(h_array[i]);
    cout << solution.maxArea(height) << endl;
    return 0;
}
