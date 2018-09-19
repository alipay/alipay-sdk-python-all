#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpEntityMonitorUploadResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpEntityMonitorUploadResponse, self).__init__()
        self._biz_success = None
        self._solution_id = None

    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpEntityMonitorUploadResponse, self).parse_response_content(response_content)
        if 'biz_success' in response:
            self.biz_success = response['biz_success']
        if 'solution_id' in response:
            self.solution_id = response['solution_id']
