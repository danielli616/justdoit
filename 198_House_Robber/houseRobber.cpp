class Solution
{
public:
    int rob(vector<int> &nums)
    {

        int len = nums.size();

        // Padding
        vector<int> re(len + 2, 0);

        // 自底向上
        for (int i = len - 1; i >= 0; i--)
        {
            re[i] = std::max(re[i + 1], nums[i] + re[i + 2]);
        }

        return re[0];
    }
};