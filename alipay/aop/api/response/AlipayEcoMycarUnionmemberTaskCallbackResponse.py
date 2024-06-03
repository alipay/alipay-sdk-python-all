#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarUnionmemberTaskCallbackResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarUnionmemberTaskCallbackResponse, self).__init__()
        self._award_status = None
        self._task_status = None

    @property
    def award_status(self):
        return self._award_status

    @award_status.setter
    def award_status(self, value):
        self._award_status = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarUnionmemberTaskCallbackResponse, self).parse_response_content(response_content)
        if 'award_status' in response:
            self.award_status = response['award_status']
        if 'task_status' in response:
            self.task_status = response['task_status']
