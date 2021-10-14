using System;


namespace APIdev {
    class Program {

        static void Main(string[] args) {
            MicroServerAPI.MicroService mserv = new("http://localhost:8080/5-semestr/compiler/get-job", "http://localhost:8080/5-semestr/compiler/post-job", false);
            
            System.Diagnostics.Stopwatch stw = new();
            Console.WriteLine("Started");
            stw.Start();
            string result = mserv.ProcessAsFunction<string, bool>("PyTest.01", true);
            stw.Stop();
            Console.WriteLine(result);
            Console.WriteLine(stw.ElapsedMilliseconds / 1000.0);
        }
    }
}
