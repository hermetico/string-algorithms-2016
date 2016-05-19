#include <iostream>
#include <ctime>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, const char* argv[]) {

  //std::string str = argv[1];
 // std::string pat = argv[2];
 string str;
 string pat;
  int count =0;

  ifstream infile;
  infile.open("args");
  infile >> str >> pat;
  time_t start = time(0);
  for (int i=0; i<str.length()-(pat.length()-1); i++){
    for(int j=0; j<pat.length();j++){
      if (str[i+j] != pat[j]){
	count--;
	break;
      }
    }
    count++;
  }
  time_t end = time(0);
  int elapsed_time =(end-start);
  
  
  //std::cout << end << "  " << start << "  "  << elapsed_time << std::endl;
  //std::cout <<"Result: " << count<< "\nTime: " << end-start << std::endl;
  //std::cout << str.length() << "\t" << 1000000.0*(end-start)/CLOCKS_PER_SEC << std::endl;
  cout << str.length() << "\t" << elapsed_time << endl;
}
