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
            ejer2();
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
            Console.WriteLine("Ingrese numero x: ");
            int x = int.Parse( Console.ReadLine());
            Console.WriteLine("Ingrese numero y: ");
            int y = Convert.ToInt32( Console.ReadLine());
            double resu = (double)x / (double)y;
            Console.WriteLine("Suma: " + (x + y));
            Console.WriteLine("Resta: " + (x - y));
            Console.WriteLine("Multiplicacion: " + (x * y));
            Console.WriteLine("Division: " + resu);
        }
        static void ejer3()
        {

        }
        static void ejer4()
        {

        }
        static void ejer5()
        {

        }
        static void ejer6()
        {

        }
    }
}
