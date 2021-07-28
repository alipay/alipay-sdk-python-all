#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OfflinepayBaseRPCResponseInfo import OfflinepayBaseRPCResponseInfo


class AlipayCommerceTransportWorldCardscriptQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportWorldCardscriptQueryResponse, self).__init__()
        self._current_time = None
        self._offlinepay_base_rpc_response_info = None
        self._script_code = None
        self._script_mac = None

    @property
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, value):
        self._current_time = value
    @property
    def offlinepay_base_rpc_response_info(self):
        return self._offlinepay_base_rpc_response_info

    @offlinepay_base_rpc_response_info.setter
    def offlinepay_base_rpc_response_info(self, value):
        if isinstance(value, OfflinepayBaseRPCResponseInfo):
            self._offlinepay_base_rpc_response_info = value
        else:
            self._offlinepay_base_rpc_response_info = OfflinepayBaseRPCResponseInfo.from_alipay_dict(value)
    @property
    def script_code(self):
        return self._script_code

    @script_code.setter
    def script_code(self, value):
        self._script_code = value
    @property
    def script_mac(self):
        return self._script_mac

    @script_mac.setter
    def script_mac(self, value):
        self._script_mac = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportWorldCardscriptQueryResponse, self).parse_response_content(response_content)
        if 'current_time' in response:
            self.current_time = response['current_time']
        if 'offlinepay_base_rpc_response_info' in response:
            self.offlinepay_base_rpc_response_info = response['offlinepay_base_rpc_response_info']
        if 'script_code' in response:
            self.script_code = response['script_code']
        if 'script_mac' in response:
            self.script_mac = response['script_mac']
