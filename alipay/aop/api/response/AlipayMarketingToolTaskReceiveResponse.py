#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingToolTaskReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolTaskReceiveResponse, self).__init__()
        self._stage_code = None
        self._task_id = None

    @property
    def stage_code(self):
        return self._stage_code

    @stage_code.setter
    def stage_code(self, value):
        self._stage_code = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolTaskReceiveResponse, self).parse_response_content(response_content)
        if 'stage_code' in response:
            self.stage_code = response['stage_code']
        if 'task_id' in response:
            self.task_id = response['task_id']
