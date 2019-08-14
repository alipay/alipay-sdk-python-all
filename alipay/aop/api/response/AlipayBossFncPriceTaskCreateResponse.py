#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncPriceTaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncPriceTaskCreateResponse, self).__init__()
        self._result_code = None
        self._result_msg = None
        self._task_detail = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def task_detail(self):
        return self._task_detail

    @task_detail.setter
    def task_detail(self, value):
        self._task_detail = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncPriceTaskCreateResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'task_detail' in response:
            self.task_detail = response['task_detail']
