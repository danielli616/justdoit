// The API isBadVersion is defined for you.
// bool isBadVersion(int version);


class Solution
{
  public:
    int firstBadVersion(int n)
    {
      long start = 1;
      long end = n;
      long mid = (start + end) / 2;

      while (start != mid)
      {
        !isBadVersion(mid) ? (start = mid) : (end = mid);
        mid = (start + end) / 2;
      }

      return isBadVersion(start) ? start : end;
    }
};
