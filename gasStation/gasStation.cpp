/**
 * 首先确认gas总和大于cost，因此判断能够绕圈。接下来寻找起始位置，我们可以借鉴归并排序的思路，如果某一段路gas>cost，则这段路剩余的油量可以支撑其他路段。因此问题变化为找到某个节点，在它之前的路段剩余油量为负，而从它开始到整个队列结束剩余油量为正（正油量可以不足前面路段的不足油量）。时间可以在O（n）完成。
 * 
 * */
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        vector<int> remainder;
        int sum =0;
        for(int i = 0; i < gas.size(); i++)
        {
            remainder.push_back(gas[i]-cost[i]);
            sum += gas[i]-cost[i];
        }
        if(sum < 0)
        {
            return -1;
        }
        else
        {
            int start;
            int cur = 0;
            do
            {
                start = cur;
                int tmp = remainder[cur++];
                while(tmp >= 0 && cur<gas.size())
                {
                    tmp += remainder[cur++];
                    if(tmp < 0)
                    {
                        break;
                    }
                }
                if(tmp >= 0 && cur == gas.size())
                {
                    return start;
                }
            }while(cur<gas.size());
            return -1;
        }
    }
};
