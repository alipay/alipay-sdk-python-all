#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNopenModuleBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNopenModuleBindResponse, self).__init__()
        self._sn = None
        self._trace_id_info = None
        self._url = None

    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def trace_id_info(self):
        return self._trace_id_info

    @trace_id_info.setter
    def trace_id_info(self, value):
        self._trace_id_info = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNopenModuleBindResponse, self).parse_response_content(response_content)
        if 'sn' in response:
            self.sn = response['sn']
        if 'trace_id_info' in response:
            self.trace_id_info = response['trace_id_info']
        if 'url' in response:
            self.url = response['url']
