#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseDataserviceInsighttaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseDataserviceInsighttaskQueryResponse, self).__init__()
        self._biz_no = None
        self._task_status = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseDataserviceInsighttaskQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'task_status' in response:
            self.task_status = response['task_status']
