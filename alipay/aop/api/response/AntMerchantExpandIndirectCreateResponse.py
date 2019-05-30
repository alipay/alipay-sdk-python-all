#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectCreateResponse, self).__init__()
        self._service_codes = None
        self._service_fail_reason = None
        self._sub_merchant_id = None

    @property
    def service_codes(self):
        return self._service_codes

    @service_codes.setter
    def service_codes(self, value):
        if isinstance(value, list):
            self._service_codes = list()
            for i in value:
                self._service_codes.append(i)
    @property
    def service_fail_reason(self):
        return self._service_fail_reason

    @service_fail_reason.setter
    def service_fail_reason(self, value):
        self._service_fail_reason = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectCreateResponse, self).parse_response_content(response_content)
        if 'service_codes' in response:
            self.service_codes = response['service_codes']
        if 'service_fail_reason' in response:
            self.service_fail_reason = response['service_fail_reason']
        if 'sub_merchant_id' in response:
            self.sub_merchant_id = response['sub_merchant_id']
