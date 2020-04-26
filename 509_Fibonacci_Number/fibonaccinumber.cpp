class Solution {
    public:
        int fib(int N) {
            return memorize(N);
        }

        int memorize(int N) {
            if (N <= 1)
                return N;
            std::vector<int> nums(N+1);

            nums[1] = 1;
            for (int i = 2 ; i < N+1 ; i++)
            {
                nums[i] =   nums[i - 1] +  nums[i - 2];
            }
            return nums[N];
        }
};
