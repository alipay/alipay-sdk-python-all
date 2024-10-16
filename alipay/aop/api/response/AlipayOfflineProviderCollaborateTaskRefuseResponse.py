#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderCollaborateTaskRefuseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateTaskRefuseResponse, self).__init__()
        self._task_no = None

    @property
    def task_no(self):
        return self._task_no

    @task_no.setter
    def task_no(self, value):
        self._task_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateTaskRefuseResponse, self).parse_response_content(response_content)
        if 'task_no' in response:
            self.task_no = response['task_no']
