#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandBenefitConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandBenefitConfirmResponse, self).__init__()
        self._benefit_instance_id = None
        self._detail_msg = None
        self._error_code = None
        self._grant_sn = None
        self._record_id = None
        self._result = None

    @property
    def benefit_instance_id(self):
        return self._benefit_instance_id

    @benefit_instance_id.setter
    def benefit_instance_id(self, value):
        self._benefit_instance_id = value
    @property
    def detail_msg(self):
        return self._detail_msg

    @detail_msg.setter
    def detail_msg(self, value):
        self._detail_msg = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def grant_sn(self):
        return self._grant_sn

    @grant_sn.setter
    def grant_sn(self, value):
        self._grant_sn = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandBenefitConfirmResponse, self).parse_response_content(response_content)
        if 'benefit_instance_id' in response:
            self.benefit_instance_id = response['benefit_instance_id']
        if 'detail_msg' in response:
            self.detail_msg = response['detail_msg']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'grant_sn' in response:
            self.grant_sn = response['grant_sn']
        if 'record_id' in response:
            self.record_id = response['record_id']
        if 'result' in response:
            self.result = response['result']
