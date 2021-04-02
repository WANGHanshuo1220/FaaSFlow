import gevent
import repository
import function_proxy
import sys
sys.path.append('../function_manager')
from function_manager import FunctionManager


class WorkflowManager:
    def __init__(self, request_id):
        self.request_id = request_id
        self.function_info = dict()
        self.file_exist = set()

    def get_function_info(self, function_name):
        if function_name not in self.function_info:
            self.function_info[function_name] = repository.get_function_info(function_name)
        return self.function_info[function_name]

    def run_function(self, function_name):
        # prepare params
        function_info = self.get_function_info(function_name)
        param = {'function_name': function_info['function_name'], 'request_id': self.request_id,
                 'runtime': function_info['runtime'], 'input': function_info['input'],
                 'output': function_info['output']}
        # run function
        function_proxy.run(param)
        # save each function's file location
        for output_file_name in function_info['output']:
            self.file_exist.add(output_file_name)
        # check if any function has enough input to be able to fire
        for name in function_info['next']:
            next_function_info = self.get_function_info(name)
            file_name_list = next_function_info['input'].keys()
            file_satisfied = True
            for file_name in file_name_list:
                if file_name not in self.file_exist:
                    file_satisfied = False
                    break
            if file_satisfied:
                gevent.spawn(self.run_function(name))

    def prepare_basic_input(self):
        basic_input = repository.get_basic_input()
        file_list = list()
        for doc in basic_input:
            file_list.append({'request_id': self.request_id, 'file_name': doc['file_name'], 'value': '0'})
            self.file_exist.add(doc['file_name'])
        repository.prepare_basic_file(file_list)

    def run_workflow(self):
        self.prepare_basic_input()
        gevent.spawn(self.run_function('start_node'))


# workflow = WorkflowManager('1')
# workflow.run_workflow()
# db[request_id + "_" + function + "_" + file_name] = {"key" : "file1", "value" : "****"}
# without function, just filename