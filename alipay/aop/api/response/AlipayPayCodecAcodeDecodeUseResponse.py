#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayCodecAcodeDecodeUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayCodecAcodeDecodeUseResponse, self).__init__()
        self._biz_id = None
        self._biz_inst_code = None
        self._business_info = None
        self._create_time = None
        self._encode_inst_code = None
        self._expire_time = None
        self._pay_account = None
        self._pay_account_auth_expire = None
        self._pay_amount_limit = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_inst_code(self):
        return self._biz_inst_code

    @biz_inst_code.setter
    def biz_inst_code(self, value):
        self._biz_inst_code = value
    @property
    def business_info(self):
        return self._business_info

    @business_info.setter
    def business_info(self, value):
        self._business_info = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def encode_inst_code(self):
        return self._encode_inst_code

    @encode_inst_code.setter
    def encode_inst_code(self, value):
        self._encode_inst_code = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def pay_account(self):
        return self._pay_account

    @pay_account.setter
    def pay_account(self, value):
        self._pay_account = value
    @property
    def pay_account_auth_expire(self):
        return self._pay_account_auth_expire

    @pay_account_auth_expire.setter
    def pay_account_auth_expire(self, value):
        self._pay_account_auth_expire = value
    @property
    def pay_amount_limit(self):
        return self._pay_amount_limit

    @pay_amount_limit.setter
    def pay_amount_limit(self, value):
        self._pay_amount_limit = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayCodecAcodeDecodeUseResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'biz_inst_code' in response:
            self.biz_inst_code = response['biz_inst_code']
        if 'business_info' in response:
            self.business_info = response['business_info']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'encode_inst_code' in response:
            self.encode_inst_code = response['encode_inst_code']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'pay_account' in response:
            self.pay_account = response['pay_account']
        if 'pay_account_auth_expire' in response:
            self.pay_account_auth_expire = response['pay_account_auth_expire']
        if 'pay_amount_limit' in response:
            self.pay_amount_limit = response['pay_amount_limit']
