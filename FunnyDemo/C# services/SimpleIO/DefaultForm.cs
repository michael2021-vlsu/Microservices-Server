using System;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Linq;
using System.Runtime.InteropServices;
using System.Threading;

namespace SimpleIO {
    public partial class DefaultForm : Form {
        public DefaultForm() {
            InitializeComponent();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e) {
            var psinfo = new ProcessStartInfo {
                UseShellExecute = true,
                FileName = "https://docs.microsoft.com/ru-ru/dotnet/csharp/tour-of-csharp/"
            };
            Process.Start(psinfo);
        }

        private void button1_Click(object sender, EventArgs e) {
            Close();
        }

        private void button2_Click(object sender, EventArgs e) {
            string[] tbtext = tbInput.Lines;
            button2.Enabled = false;
            button2.Text = "Ждите результат...";
            tbOutput.Text = "";

            //All magic here!!!
            var serv = new MicroServerAPI.MicroService("http://localhost:8080/5-semestr/compiler/get-job", "http://localhost:8080/5-semestr/compiler/post-job");

            object[] result = null;

            Task.Run(() => {
                //ProcessAsFunction is blocking function, however, we have a GUI, that mut not to be blocked
                //We need to rub ProcessAsFunction as a background task
                //Task.Run do that
                result = serv.ProcessAsFunction<object[], string[]>("Demo.Backend.MutliExpressionCalculator.EffectiveManager", 
                    tbtext, 
                    "Demo.Backend.MutliExpressionCalculator.EffectiveManager.Merit");

            }).ContinueWith((task) => {
                //We need to fill textbox or to display error after the processing by ProcessAsFunction
                //ContinueWith allows to simply execute needed work in a GUI thread
                if (task.IsCompletedSuccessfully) {
                    tbOutput.Lines = result.Select(x => x.ToString()).ToArray(); //Converting object array to the string array
                } else {
                    MessageBox.Show("Произошла ошибка: " + task.Exception.Message + "\nУчтите, persistentMode (persistentConnections) неактивен: возможно, система ещё запускается, подождите и попробуйте снова позже.", "Ошибка подключения к серверу", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                button2.Enabled = true;
                button2.Text = "Вычислить";
            }, TaskScheduler.FromCurrentSynchronizationContext()); //FromCurrentSynchronizationContext tells ContinueWith to execute work in a GUI thread
            //End of magic
        }

        private void DefaultForm_FormClosing(object sender, FormClosingEventArgs e) {
            if (!button2.Enabled) {
                var result = MessageBox.Show("А вот этого делать не рекомендуется во время ожидания результата!\nЕсли вы выйдете сейчас, результат текущих вычислений будет занимать место на сервере, но получить его данная программа не сможет!\nВы согласны ещё подождать?", "Предупреждение", MessageBoxButtons.YesNo, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1);
                if (result == DialogResult.Yes)
                    e.Cancel = true;
            }
        }

        [DllImport("user32.dll")]
        [return: MarshalAs(UnmanagedType.Bool)]
        private static extern bool FlashWindow(IntPtr pwfi, bool bInvert);

        private void timer1_Tick(object sender, EventArgs e) {
            if (ActiveForm != this) {
                bool fls = FlashWindow(Handle, true);
                if (!fls) {
                    Activate();
                }
            }
            
        }
    }
}
