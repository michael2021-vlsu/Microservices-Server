import MicroServerAPI

serv = MicroServerAPI.MicroService(url_get='http://localhost:8080/5-semestr/compiler/get-job',
                                   url_post='http://localhost:8080/5-semestr/compiler/post-job',
                                   persistentMode=True)

while True:
    first_data,addr = serv.GetNextJob(job_type='Demo.Backend.MutliExpressionCalculator.EffectiveManager')
    #Begin of data processing area

    print("Manager task: " + str(first_data))
    
    second_data = serv.ProcessAsFunction(content=first_data,
                           requested_function='Demo.Backend.LineTrimmer')

    third_data = serv.ProcessAsFunction(content=second_data,
                           requested_function='Demo.Backend.MutliExpressionCalculator.LinesProcessor')

    print("Manager completed: " + str(third_data))
    print()
    
    #End of data processing area
    serv.PostFinalResult(content=third_data,
                         result_type='Demo.Backend.MutliExpressionCalculator.EffectiveManager.Merit',
                         responseAddress=addr)
