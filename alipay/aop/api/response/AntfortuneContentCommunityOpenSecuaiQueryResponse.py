#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneContentCommunityOpenSecuaiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneContentCommunityOpenSecuaiQueryResponse, self).__init__()
        self._secuai_open_result = None
        self._trace_id = None

    @property
    def secuai_open_result(self):
        return self._secuai_open_result

    @secuai_open_result.setter
    def secuai_open_result(self, value):
        self._secuai_open_result = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneContentCommunityOpenSecuaiQueryResponse, self).parse_response_content(response_content)
        if 'secuai_open_result' in response:
            self.secuai_open_result = response['secuai_open_result']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
