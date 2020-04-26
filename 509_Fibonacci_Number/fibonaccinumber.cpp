class Solution {
public:
	int fib(int N) {

		if (N <= 1) {
			return N;
		}
		return memoize(N);
	}
	int memoize(int N) {
		std::vector<int> nums(N);

		for (int i = 0; i < N; i++)
		{
			if (i == 0)
			{
				nums.at(i) = 0;
			}
			else if (i == 1)
			{
				nums.at(i) = 1;
			}
			else
			{
				nums.at(i) = nums.at(i - 1) + nums.at(i - 2);
			}
		}
		return  nums.at(N - 1) + nums.at(N - 2);
	}
};