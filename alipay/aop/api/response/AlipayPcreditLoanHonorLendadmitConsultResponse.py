#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorLendadmitConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorLendadmitConsultResponse, self).__init__()
        self._exempt_verify = None
        self._refuse_code = None
        self._refuse_msg = None
        self._refuse_msg_data = None
        self._status = None
        self._verify_list = None
        self._verify_url = None

    @property
    def exempt_verify(self):
        return self._exempt_verify

    @exempt_verify.setter
    def exempt_verify(self, value):
        self._exempt_verify = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def refuse_msg_data(self):
        return self._refuse_msg_data

    @refuse_msg_data.setter
    def refuse_msg_data(self, value):
        self._refuse_msg_data = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def verify_list(self):
        return self._verify_list

    @verify_list.setter
    def verify_list(self, value):
        if isinstance(value, list):
            self._verify_list = list()
            for i in value:
                self._verify_list.append(i)
    @property
    def verify_url(self):
        return self._verify_url

    @verify_url.setter
    def verify_url(self, value):
        self._verify_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorLendadmitConsultResponse, self).parse_response_content(response_content)
        if 'exempt_verify' in response:
            self.exempt_verify = response['exempt_verify']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'refuse_msg_data' in response:
            self.refuse_msg_data = response['refuse_msg_data']
        if 'status' in response:
            self.status = response['status']
        if 'verify_list' in response:
            self.verify_list = response['verify_list']
        if 'verify_url' in response:
            self.verify_url = response['verify_url']
