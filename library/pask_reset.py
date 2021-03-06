#!/usr/bin/python

import os
import logging
import requests
import copy
import ast
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.pask_prestapi import PrestApi,\
    OP_DELETE, OP_GET, OP_POST, OP_PUT
from ansible.module_utils.pask_module import PaskModule,\
    make_module_args, try_except


module_args = dict(
    verify=dict(type="str", required=True)
)

name = 'reset'


class PaskReset(PaskModule):
    def __init__(self, name, module_args):
        super(PaskReset, self).__init__(name, module_args)

    @try_except
    def run(self):
        if self.module.params['verify'] == "yes":
            data = dict()
            self.resp = self.post(self.url, data)


def main():
    reset = PaskReset(name, module_args)
    reset.set_param()
    reset.run()
    reset.set_result()

if __name__ == '__main__':
    main()
