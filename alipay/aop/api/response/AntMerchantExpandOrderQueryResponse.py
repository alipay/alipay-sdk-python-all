#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandOrderQueryResponse, self).__init__()
        self._apply_time = None
        self._ext_info = None
        self._ip_role_id = None
        self._merchant_name = None
        self._status = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        if isinstance(value, list):
            self._ip_role_id = list()
            for i in value:
                self._ip_role_id.append(i)
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandOrderQueryResponse, self).parse_response_content(response_content)
        if 'apply_time' in response:
            self.apply_time = response['apply_time']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'status' in response:
            self.status = response['status']
