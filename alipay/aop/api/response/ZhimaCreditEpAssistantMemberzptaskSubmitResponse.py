#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAssistantMemberzptaskSubmitResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAssistantMemberzptaskSubmitResponse, self).__init__()
        self._jump_url = None
        self._task_id = None

    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAssistantMemberzptaskSubmitResponse, self).parse_response_content(response_content)
        if 'jump_url' in response:
            self.jump_url = response['jump_url']
        if 'task_id' in response:
            self.task_id = response['task_id']
