#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseDataserviceInsighttaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseDataserviceInsighttaskCreateResponse, self).__init__()
        self._biz_no = None
        self._task_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseDataserviceInsighttaskCreateResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'task_id' in response:
            self.task_id = response['task_id']
