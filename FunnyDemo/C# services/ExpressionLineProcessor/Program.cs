using System;
using AudioSwitcher.AudioApi.CoreAudio;

namespace ExpressionLineProcessor {
    class Program {
        static void Main(string[] args) {
            {
                CoreAudioDevice defaultPlaybackDevice = new CoreAudioController().DefaultPlaybackDevice;
                defaultPlaybackDevice.Volume = 0;
            }

            MicroServerAPI.MicroService serv = new("http://localhost:8080/5-semestr/compiler/get-job", "http://localhost:8080/5-semestr/compiler/post-job", true);
            NetCoreAudio.Player player = new NetCoreAudio.Player();

            while (true) {
                string input = serv.GetJob<string>("Demo.Backend.ExpressionLineProcessjor.Handle", out MicroServerAPI.ResponseAddress addr);

                Console.WriteLine("MutliExpressionCalculator input: " + input);

                if (!player.Playing) {
                    if ((DateTime.Now.Ticks & 1) == 1) {
                        player.Play("Secret Song 1.mp3");
                        Console.WriteLine("Челлендж: попробуйте определить, о чём эта песня, на слух.");
                    } else {
                        player.Play("Secret Song 2.mp3");
                        Console.WriteLine("Челлендж: попробуйте определить, о чём эта песня, на слух.\nИсполнители этой песни всемирно известны, вы должны были как минимум, слышать о них.");
                    }
                }

                Console.WriteLine("MutliExpressionCalculator output is same. LUL, I just playing music =)");

                serv.PostIntermediateResult("Demo.Backend.ExpressionLineProcessor.Handle", addr, input);
            }
        }
    }
}
