def app(env, start_response):                                                   
    start_response('200 OK', [('Content-Type', 'text/plain')])                  
    return  [x + "\n\r" for x in env["QUERY_STRING"].split("&")]                

