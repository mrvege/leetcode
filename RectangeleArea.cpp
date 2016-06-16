#include <iostream>
using namespace std;

//problem descripition: https://leetcode.com/problems/rectangle-area/

//思路分析：
// 开始的时候看错了题目。。以为是求覆盖面积， 解到后来发现是求两个长方形的总面积， 那么思路就是分别计算两个矩阵面积， 然后减去overlap
//其中需要判断的是两个矩阵是不是有相交的部分， 这里max和min方法 也可以用math库里的math和min替换掉
class Solution{
public:
  int max(int a, int b){
    return a>b?a:b;
  }
  int min(int a, int b){
    return a<b?a:b;
  }
  int computeArea(int A, int B, int C, int D, int E, int F, int G, int H){
    int lx, ly, rx, ry;
    lx = max(A, E);
    ly = max(B, F);
    rx = min(C, G);
    ry = min(D, H);
    int result = (C-A)*(D-B) +(G-E)*(H-F);
    if(lx >= rx || ly>= ry) return result;
    return result - (rx-lx)*(ry-ly);
    }
};
int main(int argc, char const *argv[]) {
  /* code */
  Solution s1;
  int result = s1.computeArea(-2, -2, 2, 2, -2, -2, 2, 2);
  cout<<result<<endl;
  return 0;
}
