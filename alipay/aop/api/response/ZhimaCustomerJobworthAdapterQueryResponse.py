#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerJobworthAdapterQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthAdapterQueryResponse, self).__init__()
        self._adapter_score = None
        self._sub_code = None
        self._sub_msg = None
        self._url = None

    @property
    def adapter_score(self):
        return self._adapter_score

    @adapter_score.setter
    def adapter_score(self, value):
        self._adapter_score = value
    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value
    @property
    def sub_msg(self):
        return self._sub_msg

    @sub_msg.setter
    def sub_msg(self, value):
        self._sub_msg = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthAdapterQueryResponse, self).parse_response_content(response_content)
        if 'adapter_score' in response:
            self.adapter_score = response['adapter_score']
        if 'sub_code' in response:
            self.sub_code = response['sub_code']
        if 'sub_msg' in response:
            self.sub_msg = response['sub_msg']
        if 'url' in response:
            self.url = response['url']
