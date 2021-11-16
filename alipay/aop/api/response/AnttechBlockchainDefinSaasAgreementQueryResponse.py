#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinSaasAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinSaasAgreementQueryResponse, self).__init__()
        self._active_flag = None
        self._end_time = None
        self._out_member_id = None
        self._platform_member_id = None
        self._product_code = None
        self._product_name = None
        self._product_type = None
        self._signing_time = None

    @property
    def active_flag(self):
        return self._active_flag

    @active_flag.setter
    def active_flag(self, value):
        self._active_flag = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        self._out_member_id = value
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def signing_time(self):
        return self._signing_time

    @signing_time.setter
    def signing_time(self, value):
        self._signing_time = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinSaasAgreementQueryResponse, self).parse_response_content(response_content)
        if 'active_flag' in response:
            self.active_flag = response['active_flag']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'out_member_id' in response:
            self.out_member_id = response['out_member_id']
        if 'platform_member_id' in response:
            self.platform_member_id = response['platform_member_id']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'product_name' in response:
            self.product_name = response['product_name']
        if 'product_type' in response:
            self.product_type = response['product_type']
        if 'signing_time' in response:
            self.signing_time = response['signing_time']
