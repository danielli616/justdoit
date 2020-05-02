class Solution
{
public:
    vector<int> findDisappearedNumbers(vector<int> &nums)
    {
        vector<int> res;
        int temp = 0;

        for (int i = 0; i < nums.size(); i++)
        {

            if (nums[i] != i + 1)
            {
                temp = nums[i];

                nums[i] = nums[temp - 1];

                nums[temp - 1] = temp;
            }
        }

        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != i + 1)
                res.push_back(i + 1);
        }

        return res;
    }
};