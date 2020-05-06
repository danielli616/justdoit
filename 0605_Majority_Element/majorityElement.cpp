class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        vector<int>::iterator ptr;
        unordered_map<int, int> mymap;
        int len = nums.size();

        for (ptr = nums.begin(); ptr < nums.end(); ptr++)
        {
            auto ret = mymap.insert(std::pair<int, int>(*ptr, 1));

            if (ret.second == false)
            {
                ret.first->second++;

                if (ret.first->second > len / 2)
                {
                    return *ptr;
                }
            }
        }
        
        return 0;
    }
};