int[] one_d = {1,2,3};
int[,]two_d_ex1 = new int [3,4];



int[,] two_d_ex2 = new int [,]
{
    {1,2,3},
    {4,5,6},
    {7,8,9},
    {10,11,12},
    {13,14,15}

};

Console.WriteLine(two_d_ex2[3,0]);



int rows = 3; // 3แถว
int cols = 4; // 4คอลัมน์


int[,] two_d_ex3 = new int [rows,cols];

//รับค่า
for (int i = 0; i < rows; i++)
{
    for (int j = 0; j < cols; j++)
    {
        Console.Write(
            $"Enter value for Two array two_d_ex3 [{i},{j}]: "
            );
        string input = Console.ReadLine();
        if(int.TryParse(input, out int value))
    {
         two_d_ex3[i,j] = value;
    }
    else
        {
        Console.WriteLine("Invalid number, set to 0");
        two_d_ex3[i,j] = 0;
        }
    }
}