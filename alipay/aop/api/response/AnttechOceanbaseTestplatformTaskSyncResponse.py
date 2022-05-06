#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseTestplatformTaskSyncResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseTestplatformTaskSyncResponse, self).__init__()
        self._task_id = None
        self._task_info = None

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_info(self):
        return self._task_info

    @task_info.setter
    def task_info(self, value):
        self._task_info = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseTestplatformTaskSyncResponse, self).parse_response_content(response_content)
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'task_info' in response:
            self.task_info = response['task_info']
