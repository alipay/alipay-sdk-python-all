#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceXlightTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceXlightTaskQueryResponse, self).__init__()
        self._finish_time = None
        self._status = None
        self._task_reward_amount = None

    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_reward_amount(self):
        return self._task_reward_amount

    @task_reward_amount.setter
    def task_reward_amount(self, value):
        self._task_reward_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceXlightTaskQueryResponse, self).parse_response_content(response_content)
        if 'finish_time' in response:
            self.finish_time = response['finish_time']
        if 'status' in response:
            self.status = response['status']
        if 'task_reward_amount' in response:
            self.task_reward_amount = response['task_reward_amount']
