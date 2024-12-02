#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationTaskReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationTaskReceiveResponse, self).__init__()
        self._point = None
        self._task_id = None

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationTaskReceiveResponse, self).parse_response_content(response_content)
        if 'point' in response:
            self.point = response['point']
        if 'task_id' in response:
            self.task_id = response['task_id']
