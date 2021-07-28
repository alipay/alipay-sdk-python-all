#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportIntelligentizeDataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIntelligentizeDataSyncResponse, self).__init__()
        self._data_id = None
        self._ext_info = None
        self._result_code = None
        self._result_msg = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIntelligentizeDataSyncResponse, self).parse_response_content(response_content)
        if 'data_id' in response:
            self.data_id = response['data_id']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
