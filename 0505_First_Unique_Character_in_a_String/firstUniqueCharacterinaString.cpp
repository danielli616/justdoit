class Solution
{
public:
    int firstUniqChar(string s)
    {
        unordered_map<char, int> mymap;
        int i = 0;
        int res = -1;

        for (char c : s)
        {
            auto ret = mymap.insert(std::make_pair(c, i));
            i++;

            if (ret.second == false)
            {
                ret.first->second = -1;
            }
        }

        int temp = s.size();

        for (const auto &n : mymap)
        {
            if (n.second >= 0 && n.second < temp)
            {
                res = n.second;
                temp = n.second;
            }
        }

        return res;
    }
};