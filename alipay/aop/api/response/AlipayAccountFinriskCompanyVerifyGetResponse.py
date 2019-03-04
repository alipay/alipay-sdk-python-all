#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VerifyInfoVO import VerifyInfoVO


class AlipayAccountFinriskCompanyVerifyGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountFinriskCompanyVerifyGetResponse, self).__init__()
        self._result_code = None
        self._result_code_third = None
        self._result_desc = None
        self._success = None
        self._verify_info = None
        self._verify_result_code = None
        self._verify_result_desc = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_code_third(self):
        return self._result_code_third

    @result_code_third.setter
    def result_code_third(self, value):
        self._result_code_third = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def verify_info(self):
        return self._verify_info

    @verify_info.setter
    def verify_info(self, value):
        if isinstance(value, list):
            self._verify_info = list()
            for i in value:
                if isinstance(i, VerifyInfoVO):
                    self._verify_info.append(i)
                else:
                    self._verify_info.append(VerifyInfoVO.from_alipay_dict(i))
    @property
    def verify_result_code(self):
        return self._verify_result_code

    @verify_result_code.setter
    def verify_result_code(self, value):
        self._verify_result_code = value
    @property
    def verify_result_desc(self):
        return self._verify_result_desc

    @verify_result_desc.setter
    def verify_result_desc(self, value):
        self._verify_result_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountFinriskCompanyVerifyGetResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_code_third' in response:
            self.result_code_third = response['result_code_third']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'success' in response:
            self.success = response['success']
        if 'verify_info' in response:
            self.verify_info = response['verify_info']
        if 'verify_result_code' in response:
            self.verify_result_code = response['verify_result_code']
        if 'verify_result_desc' in response:
            self.verify_result_desc = response['verify_result_desc']
