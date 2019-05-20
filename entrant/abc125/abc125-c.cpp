#include <iostream>
#include <vector>

int gcd(int a,int b){
  int tmp;
  while(b!=0){
    tmp=a%b;
    a=b;
    b=tmp;
  }
  return a;
}

int max(int g[],int n){
  int max=g[0];
  for(int i=1;i<n;i++){
    if(g[i]>max) max=g[i];
  }
  return max;
}

int main(){
  int n;
  std::cin>>n;
  // int tmp,a[n];
  // for(int i=0;i<n;i++){
  //   std::cin>>tmp;
  //   a[i]=tmp;
  // }
  std::vector<int> a(n);
  for(int i=0;i<n;i++) std::cin>>a[i];
  int g[n];
  // std::vector<int> g(n);
  for(int i=0;i<n;i++){
    int isFirst=1;
    for(int j=0;j<i;j++){
      if(isFirst){
        g[i]=a[j];
        isFirst=0;
      }
      else g[i]=gcd(g[i],a[j]);
    }
    for(int j=i+1;j<n;j++){
      if(isFirst){
        g[i]=a[j];
        isFirst=0;
      }
      else g[i]=gcd(g[i],a[j]);
    }
    // std::cout<<g[i]<<std::endl;
  }
  std::cout<<max(g,n)<<std::endl;
  return 0;
}
