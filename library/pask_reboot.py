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

name = 'reboot'


class PaskReboot(PaskModule):
    def __init__(self, name, module_args):
        super(PaskReboot, self).__init__(name, module_args)

    @try_except
    def run(self):
        if self.module.params['verify'] == "yes":
            data = dict()
            self.resp = self.post(self.url, data)


def main():
    reboot = PaskReboot(name, module_args)
    reboot.set_param()
    reboot.run()
    reboot.set_result()

if __name__ == '__main__':
    main()
