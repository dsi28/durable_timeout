# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blueprint) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints

import logging
import azure.functions as func


blueprint = func.Blueprint()


@blueprint.service_bus_queue_trigger(arg_name="azservicebus", queue_name="mysbqueue",
                               connection="AzureWebJobsStorage") 
def servicebus_trigger(azservicebus: func.ServiceBusMessage):
    logging.info('Python ServiceBus Queue trigger processed a message: %s',
                azservicebus.get_body().decode('utf-8'))
