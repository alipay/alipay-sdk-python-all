#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyApplyCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyApplyCreateResponse, self).__init__()
        self._apply_no = None
        self._ip_role_id = None
        self._sub_apply_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def sub_apply_no(self):
        return self._sub_apply_no

    @sub_apply_no.setter
    def sub_apply_no(self, value):
        self._sub_apply_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyApplyCreateResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'sub_apply_no' in response:
            self.sub_apply_no = response['sub_apply_no']
