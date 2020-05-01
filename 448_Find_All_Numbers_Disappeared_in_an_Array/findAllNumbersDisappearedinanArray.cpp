class Solution
{
public:
    vector<int> findDisappearedNumbers(vector<int> &D)
    {

        vector<int> re;

        int len = D.size();
        bool ismember = false;

        for (unsigned i = 1; i < len + 1; i++)
        {
            ismember = false;
            for (unsigned j = 0; j < D.size(); j++)
            {

                if (D.at(j) == i)
                {
                    D.erase(D.begin() + j);
                    ismember = true;
                }
            }
            if (!ismember)
            {
                re.push_back(i);
            }
        }

        return re;
    }
};