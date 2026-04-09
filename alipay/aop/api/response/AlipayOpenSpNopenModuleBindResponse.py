#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNopenModuleBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNopenModuleBindResponse, self).__init__()
        self._trace_id_info = None

    @property
    def trace_id_info(self):
        return self._trace_id_info

    @trace_id_info.setter
    def trace_id_info(self, value):
        self._trace_id_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNopenModuleBindResponse, self).parse_response_content(response_content)
        if 'trace_id_info' in response:
            self.trace_id_info = response['trace_id_info']
