import MicroServerAPI

serv = MicroServerAPI.MicroService(url_get='http://localhost:8080/5-semestr/compiler/get-job',
                                   url_post='http://localhost:8080/5-semestr/compiler/post-job',
                                   persistentMode=True)

while True:
    data,addr = serv.GetNextJob(job_type='ArrayConcatenator.A42.ConcatenateStringArrayToString')
    #Begin of data processing area
    
    result_string = ""
    
    for item in data:
        result_string += item
    
    #End of data processing area
    serv.PostFinalResult(content=result_string,
                         result_type='ArrayConcatenator.A42.ConcatenateStringArrayToString.Result',
                         responseAddress=addr)
