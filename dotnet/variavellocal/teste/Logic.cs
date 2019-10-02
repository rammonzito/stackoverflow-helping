using System;

namespace teste
{
    public static class Logic
    {
        public static void VerificaMaisPesado()
        {
            int pos = 2;
            string[] sexo = new string[pos];
            string[] nome = new string[pos];
            decimal[] peso = new decimal[pos];

            decimal pesoMax = 0;
            
            string pessoamaispesada = "";

            for (var i = 0; i < pos; i++)
            {
                Console.Write("Digite o nome da pessoa: ");
                nome[i] = Console.ReadLine();
                Console.Write("Digite o sexo da pessoa {i} (M - masculino | F - feminino): ");
                sexo[i] = Console.ReadLine();
                Console.Write("Digite o peso da pessoa: ");
                peso[i] = decimal.Parse(Console.ReadLine());
            }

            for (int i = 0; i < peso.Length; i++)
            {
                if (peso[i] > pesoMax)
                {
                    pesoMax = peso[i];
                    pessoamaispesada = nome[i];
                }
            }
                       
            Console.Write("A pessoa mais pesada é {0}", pessoamaispesada);

        }
    }
}