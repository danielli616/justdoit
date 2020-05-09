class Solution
{
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        vector<char> v;

        for (char c : magazine)
        {
            v.push_back(c);
        }

        for (char s : ransomNote)
        {
            auto it = std::find(v.begin(), v.end(), s);
            if (it != v.end())
                v.erase(it);
            else
                return false;
        }

        return true;
    }
};