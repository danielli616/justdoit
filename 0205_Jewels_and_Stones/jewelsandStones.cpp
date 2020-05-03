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
            if (my_set.count(h) != 0)
                cout++;
        }
        
        return cout;
    }
};