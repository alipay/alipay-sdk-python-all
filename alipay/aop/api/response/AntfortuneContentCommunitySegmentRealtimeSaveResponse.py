#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneContentCommunitySegmentRealtimeSaveResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneContentCommunitySegmentRealtimeSaveResponse, self).__init__()
        self._result = None
        self._trace_id = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneContentCommunitySegmentRealtimeSaveResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
