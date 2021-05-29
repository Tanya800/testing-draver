int add(int a, int b)
{
    return a + b;
}

int sub(int a, int b)
{
    return a - b;
}
int theBiggest(int a,int b ,int c){
    if(a>=c) return a > b ? a : b ;
    else return c > b ? c : b;
}
_Bool isPolindrom(int number){
    int n = 0;

    while (number)
    {
        n = 10 * n + number % 10;
        number /= 10;
    }
 
    return n == number;
}
_Bool checkDel(int a,int b){
    if ((a % b )== 0 ) return 1;
    else return 0;
}