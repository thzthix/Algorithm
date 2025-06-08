/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/


import java.io.*;
import java.util.*;
//int 숫자의 개수 nums을 받는다
// int 숫자 N을 받는다
//숫자들을 받는다 StringTokenizer가 나을수도 (숫자가 15000개 옆으로 들어온다)
// int[] numbers  = new int [nums];

//count 0초기화, sum(int), startIndex, endIndex 0 초기화
//배열에 넣는다. 
//while(numbers[startIndex]!= numbers의 마지막)
//{
//     sum= numbers[startIndex] + numbers[endIndex];
//    if(sum == N) startIdex ++, endindex = startIndex+1; count++;
//    else endIndex++;
        
//}
//count 출력
public class Main {
  public static void main(String args[]) throws IOException{
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
    int nums = Integer.parseInt(stringTokenizer.nextToken());
    stringTokenizer = new StringTokenizer(bufferedReader.readLine());
    int N = Integer.parseInt(stringTokenizer.nextToken());
    stringTokenizer = new StringTokenizer(bufferedReader.readLine());
    int[] numbers =  new int[nums];
    for(int i = 0; i< nums; i++){
        numbers[i] = Integer.parseInt(stringTokenizer.nextToken());
    }
    int count = 0;
    int sum = 0;
    int startIndex = 0;
    int endIndex = 1;
    while(startIndex <= nums-2){
        sum = numbers[startIndex] + numbers[endIndex];
        if(sum == N){
            count++;
        }
        if(endIndex == nums-1)
        {
            startIndex++;
            endIndex = startIndex+1;
        }else{
            endIndex++;
        }
        
        
    }
    System.out.println(count);
    
}

}