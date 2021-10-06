import MicroServerAPI

serv = MicroServerAPI.MicroService('http://localhost:8080/5-semestr/compiler/get-job','http://localhost:8080/5-semestr/compiler/post-job')

while True:
    data,addr = serv.GetNextJob(job_type='PyTest.01')

    print(data)

    serv.PostFinalResult(content='ok',job_type='PyTest.01.Result',responseAddress=addr)
