#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskHunterReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskHunterReceiveResponse, self).__init__()
        self._task_instance_id = None

    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskHunterReceiveResponse, self).parse_response_content(response_content)
        if 'task_instance_id' in response:
            self.task_instance_id = response['task_instance_id']
