#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HittedRule import HittedRule


class DatadigitalAicsDtcontroldcRealtimeDetectResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAicsDtcontroldcRealtimeDetectResponse, self).__init__()
        self._biz_code = None
        self._biz_success = None
        self._biz_token = None
        self._hitted_rule_list = None
        self._message = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def hitted_rule_list(self):
        return self._hitted_rule_list

    @hitted_rule_list.setter
    def hitted_rule_list(self, value):
        if isinstance(value, list):
            self._hitted_rule_list = list()
            for i in value:
                if isinstance(i, HittedRule):
                    self._hitted_rule_list.append(i)
                else:
                    self._hitted_rule_list.append(HittedRule.from_alipay_dict(i))
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAicsDtcontroldcRealtimeDetectResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_success' in response:
            self.biz_success = response['biz_success']
        if 'biz_token' in response:
            self.biz_token = response['biz_token']
        if 'hitted_rule_list' in response:
            self.hitted_rule_list = response['hitted_rule_list']
        if 'message' in response:
            self.message = response['message']
