#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HonorAlipayAccountModel import HonorAlipayAccountModel


class AlipayPcreditLoanHonorUserbindCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorUserbindCheckResponse, self).__init__()
        self._access = None
        self._account_list = None
        self._bind_check_serial_no = None
        self._fail_code = None
        self._fail_reason = None
        self._refuse_msg_data = None

    @property
    def access(self):
        return self._access

    @access.setter
    def access(self, value):
        self._access = value
    @property
    def account_list(self):
        return self._account_list

    @account_list.setter
    def account_list(self, value):
        if isinstance(value, list):
            self._account_list = list()
            for i in value:
                if isinstance(i, HonorAlipayAccountModel):
                    self._account_list.append(i)
                else:
                    self._account_list.append(HonorAlipayAccountModel.from_alipay_dict(i))
    @property
    def bind_check_serial_no(self):
        return self._bind_check_serial_no

    @bind_check_serial_no.setter
    def bind_check_serial_no(self, value):
        self._bind_check_serial_no = value
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def refuse_msg_data(self):
        return self._refuse_msg_data

    @refuse_msg_data.setter
    def refuse_msg_data(self, value):
        self._refuse_msg_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorUserbindCheckResponse, self).parse_response_content(response_content)
        if 'access' in response:
            self.access = response['access']
        if 'account_list' in response:
            self.account_list = response['account_list']
        if 'bind_check_serial_no' in response:
            self.bind_check_serial_no = response['bind_check_serial_no']
        if 'fail_code' in response:
            self.fail_code = response['fail_code']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'refuse_msg_data' in response:
            self.refuse_msg_data = response['refuse_msg_data']
