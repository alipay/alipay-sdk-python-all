#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectPromotaskTakeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectPromotaskTakeResponse, self).__init__()
        self._task_id = None
        self._task_state = None

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_state(self):
        return self._task_state

    @task_state.setter
    def task_state(self, value):
        self._task_state = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectPromotaskTakeResponse, self).parse_response_content(response_content)
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'task_state' in response:
            self.task_state = response['task_state']
