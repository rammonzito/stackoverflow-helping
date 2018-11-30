using System;
using System.Text;

namespace ConsoleApplication2
{
  class Program
{
        /******************************************************* */
        //O código estava pronto, porém, possui muitas incoerências. 
        //Realizei apenas a implementação da StringBuilder.
        //Alterações marcadas como rammonzito*
        /******************************************************* */
        
    static void Main(string[] args)
    {
        int vAcertos = 0, vErros = 0, x, vTam, i;
        string vPalavra = "";
        char vLetraD;
        bool vAcertou;
        string[] Palavra = new string[8];
        Random aleatory = new Random();
        
        //palavras possíveis
        Palavra[0] = "Batman";
        Palavra[1] = "Coringa";
        Palavra[2] = "Penguim";
        Palavra[3] = "Duas Caras";
        Palavra[4] = "Harleyquinn";
        Palavra[5] = "Morcego Humano";
        Palavra[6] = "Drax";
        Palavra[7] = "Robin";

        //sorteio
        i = aleatory.Next(0, 8);
        vPalavra = Palavra[i];
        vTam = vPalavra.Length;

        //inicialização da StringBuilder
        //rammonzito*
        var PalavraAuxiliar = new StringBuilder(vPalavra);
        
        //rammonzito*
        for (x = 0; x < vTam; x++){
            PalavraAuxiliar.Replace(PalavraAuxiliar[x], '-');
        }

        Console.SetCursorPosition(25, 12);
        Console.Write(PalavraAuxiliar);
        do
        {
            Console.SetCursorPosition(10, 9);
            Console.Write("escreva uma letra: ");
            vLetraD =char.Parse( Console.ReadLine());
            vAcertou = false;
            for (int posicao = 0; posicao < vTam; posicao++)
            {   //rammonzito*
                if(vLetraD == vPalavra[posicao]){
                    PalavraAuxiliar[posicao] = vLetraD;
                    vAcertou = true;
                }
            }
                
            Console.SetCursorPosition(25, 12);
            Console.Write(PalavraAuxiliar);
            if (!vAcertou)
            {
                vErros++;
                MostraCorpo(vErros);
                Console.ReadKey();
            }
            Console.ReadKey();
        } while (vErros != 6 && vAcertos != vTam);


    }
    static void MostraCorpo(int p)
    {
        switch (p)
        {
            case 1:
                Console.SetCursorPosition(13, 7);
                Console.Write("O");
                break;
            case 2:
                Console.SetCursorPosition(13, 8);
                Console.Write(" /|\\ ");
                break;
            case 3:
                Console.SetCursorPosition(13, 7);
                Console.Write(" /\\");
                break;
        }
    }
  }
}