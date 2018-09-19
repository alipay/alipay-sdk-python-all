#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPromorulecenterRuleAnalyzeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPromorulecenterRuleAnalyzeResponse, self).__init__()
        self._fail_condition_msg = None
        self._fail_condition_name = None
        self._result_code = None
        self._success = None
        self._triggered = None

    @property
    def fail_condition_msg(self):
        return self._fail_condition_msg

    @fail_condition_msg.setter
    def fail_condition_msg(self, value):
        self._fail_condition_msg = value
    @property
    def fail_condition_name(self):
        return self._fail_condition_name

    @fail_condition_name.setter
    def fail_condition_name(self, value):
        self._fail_condition_name = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def triggered(self):
        return self._triggered

    @triggered.setter
    def triggered(self, value):
        self._triggered = value

    def parse_response_content(self, response_content):
        response = super(AlipayPromorulecenterRuleAnalyzeResponse, self).parse_response_content(response_content)
        if 'fail_condition_msg' in response:
            self.fail_condition_msg = response['fail_condition_msg']
        if 'fail_condition_name' in response:
            self.fail_condition_name = response['fail_condition_name']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'success' in response:
            self.success = response['success']
        if 'triggered' in response:
            self.triggered = response['triggered']
