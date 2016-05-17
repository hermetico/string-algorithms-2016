#include<iostream>
#include <ctime>

int main(int argc, const char* argv[]) {

  std::string str = argv[1];
  std::string pat = argv[2];
  int count =0;

  clock_t start = clock();
  for (int i=0; i<str.length()-(pat.length()-1); i++){
    for(int j=0; j<pat.length();j++){
      if (str[i+j] != pat[j]){
	count--;
	break;
      }
    }
    count++;
  }
  clock_t end = clock();
  std::cout <<"Result: " << count<< "\nTime: " << end-start << std::endl;
}
