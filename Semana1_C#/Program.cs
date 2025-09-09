using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Semana1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer4();
            Console.ReadKey();
         
        }
        static void ejer1()
        {
            string nombre, carrera; //Declarando variables
            Console.WriteLine("Ingrese su nombre: ");
            nombre = Console.ReadLine();
            Console.WriteLine("Ingrese su carrera: ");
            carrera = Console.ReadLine();
            Console.WriteLine($"\n{nombre},\nBienvenido a FA de {carrera}");
        }
        static void ejer2()
        {
            Console.Write("\"Fa\"");
        }
        static void ejer3()
        {
            Console.WriteLine("Ingrese numero x: ");
            int x = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese numero y: ");
            int y = Convert.ToInt32(Console.ReadLine());
            double resu = (double)x / (double)y;
            Console.WriteLine("Suma: " + (x + y));
            Console.WriteLine("Resta: " + (x - y));
            Console.WriteLine("Multiplicacion: " + (x * y));
            Console.WriteLine("Division: " + resu);
        }
        static void ejer4()
        {
            Console.Write("Ingrese un numero decimal: ");
            double num= Convert.ToDouble(Console.ReadLine());

            double raiz2= Math.Sqrt(num);
            int redo=(int)Math.Round(num,0);
            double reduc=Math.Round(num,2);
            double cubo=Math.Pow(num,3);
            double raiz3=Math.Pow(num,1/3d);

            Console.WriteLine("Raiz 2: " + raiz2);
            Console.WriteLine("redondeado: " + redo);
            Console.WriteLine("redondeado con decimales: " + reduc);
            Console.WriteLine("al cubo: " + cubo);
            Console.WriteLine("Raiz 3: " + raiz3);

        }
        static void ejer5()
        {

        }
        static void ejer6()
        {

        }
    }
}
