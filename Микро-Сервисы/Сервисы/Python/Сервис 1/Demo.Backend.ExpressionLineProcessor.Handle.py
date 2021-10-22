import MicroServerAPI

serv = MicroServerAPI.MicroService(url_get='http://localhost:8080/5-semestr/compiler/get-job',
                                   url_post='http://localhost:8080/5-semestr/compiler/post-job',
                                   persistentMode=True)

while True:
    data,addr = serv.GetNextJob(job_type='Demo.Backend.ExpressionLineProcessor.Handle')
    #Begin of data processing area

    print("ExpressionLineProcessor task: " + str(data))
    
    try:
        data = eval(data)
    except:
        data = f"Выражение '{str(data)}' некорректно"
    
    print("ExpressionLineProcessor completed: " + str(data))
    print()
    
    #End of data processing area
    serv.PostFinalResult(content=data,
                         result_type='Demo.Backend.ExpressionLineProcessor.Output',
                         responseAddress=addr)
