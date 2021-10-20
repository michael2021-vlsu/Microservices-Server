import MicroServerAPI

serv = MicroServerAPI.MicroService(url_get='http://localhost:8080/5-semestr/compiler/get-job',
                                   url_post='http://localhost:8080/5-semestr/compiler/post-job',
                                   persistentMode=True)

while True:
    data,addr = serv.GetNextJob(job_type='Demo.Backend.MutliExpressionCalculator.LinesProcessor')
    #Begin of data processing area

    print("LinesProcessor task: " + str(data))
    
    for i in range(0, len(data)):
        data[i] = serv.ProcessAsFunction(content=data[i],
                           requested_function='Demo.Backend.ExpressionLineProcessjor.Handle',
                           target_content_type='Demo.Backend.ExpressionLineProcessor.Output')

    print("LinesProcessor completed: " + str(data))
    print()
    
    #End of data processing area
    serv.PostFinalResult(content=data,
                         result_type='Demo.Backend.MutliExpressionCalculator.ResultingLines',
                         responseAddress=addr)
