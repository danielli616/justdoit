// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution
{
public:
    int firstBadVersion(int n)
    {
        long start = 1;
        long end = n;
        long mid = 0;

        while (start != mid)
        {
            {
                if (!middle(start, end))
                {
                    start = (start + end) / 2;
                }
                else
                {
                    end = (start + end) / 2;
                }

                mid = (start + end) / 2;
            }
        }

        if (isBadVersion(start))
        {
            return start;
        }
        else
        {
            return end;
        }
    }

    bool middle(long start, long end)
    {
        return isBadVersion((start + end) / 2);
    }
};