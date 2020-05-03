class Solution
{
public:
    int numJewelsInStones(string J, string S)
    {
        int cout = 0;
        std::set<char> my_set;

        for (char s : J)
        {
            my_set.insert(s);
        }

        for (char h : S)
        {
            auto res = my_set.insert(h);

            if (res.second)
            {
                my_set.erase(h);
            }
            else
            {
                cout++;
            }
        }

        return cout;
    }
};