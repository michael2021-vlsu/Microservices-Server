import MicroServerAPI

serv = MicroServerAPI.MicroService(url_get='http://localhost:8080/5-semestr/compiler/get-job',
                                   url_post='http://localhost:8080/5-semestr/compiler/post-job',
                                   persistentMode=True)

while True:
    data,addr = serv.GetNextJob(job_type='Demo.Backend.LineTrimmer')
    #Begin of data processing area

    print("LineTrimmer task: " + str(data))
    
    lines = [w.strip() for w in data]
    data = [w for w in lines if w]

    print("LineTrimmer completed: " + str(data))
    print()
    
    #End of data processing area
    serv.PostFinalResult(content=data,
                         result_type='Demo.Backend.LineTrimmer.Result',
                         responseAddress=addr)
