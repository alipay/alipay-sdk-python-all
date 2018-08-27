#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdSeAppletQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdSeAppletQueryResponse, self).__init__()
        self._apdu_commands = None
        self._opt_type = None
        self._result_code = None
        self._step = None
        self._step_code = None
        self._sub_opt_type = None
        self._total_step = None

    @property
    def apdu_commands(self):
        return self._apdu_commands

    @apdu_commands.setter
    def apdu_commands(self, value):
        self._apdu_commands = value
    @property
    def opt_type(self):
        return self._opt_type

    @opt_type.setter
    def opt_type(self, value):
        self._opt_type = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value
    @property
    def step_code(self):
        return self._step_code

    @step_code.setter
    def step_code(self, value):
        self._step_code = value
    @property
    def sub_opt_type(self):
        return self._sub_opt_type

    @sub_opt_type.setter
    def sub_opt_type(self, value):
        self._sub_opt_type = value
    @property
    def total_step(self):
        return self._total_step

    @total_step.setter
    def total_step(self, value):
        self._total_step = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdSeAppletQueryResponse, self).parse_response_content(response_content)
        if 'apdu_commands' in response:
            self.apdu_commands = response['apdu_commands']
        if 'opt_type' in response:
            self.opt_type = response['opt_type']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'step' in response:
            self.step = response['step']
        if 'step_code' in response:
            self.step_code = response['step_code']
        if 'sub_opt_type' in response:
            self.sub_opt_type = response['sub_opt_type']
        if 'total_step' in response:
            self.total_step = response['total_step']
