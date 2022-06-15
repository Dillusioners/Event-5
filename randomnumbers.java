public class randomnumbers 
{
    static void check(int a, int b, int c, int d, int e)
    {
        int w = a;
        int x = b;
        int y = c;
        int z = d;
        int f = e;

        int m = 0;
        int n = 0;
        int o = 0;
        int p = 0;
        int q = 0;

        while (w != 0)
        {
            int k = w % 10;
            w = w/10;
            m = m + k;
        }
        while (x != 0)
        {
            int l = x % 10;
            x = x/10;
            n = n + x;
        }
        while (y != 0)
        {
            int g = y % 10;
            y = y / 10;
            o = o + g;
        }
        while (z != 0)
        {
            int u = z % 10;
            z = z / 10;
            p = p + u;
        }
        while (f != 0)
        {
            int i = f % 10;
            f = f / 10;
            q = q + i;
        }
        
        int j = m + n + o + p + q;
        System.out.print("The random number is: "+j);
    }
}
