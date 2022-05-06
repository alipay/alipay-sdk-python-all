#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditPayRefuseVO import CreditPayRefuseVO


class MybankCreditLoantradePayerArConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePayerArConsultResponse, self).__init__()
        self._admit = None
        self._ip_id = None
        self._ip_role_id = None
        self._refuse_info = None
        self._scheme_ar_no = None
        self._sign_status = None
        self._sign_url = None
        self._signed = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def refuse_info(self):
        return self._refuse_info

    @refuse_info.setter
    def refuse_info(self, value):
        if isinstance(value, CreditPayRefuseVO):
            self._refuse_info = value
        else:
            self._refuse_info = CreditPayRefuseVO.from_alipay_dict(value)
    @property
    def scheme_ar_no(self):
        return self._scheme_ar_no

    @scheme_ar_no.setter
    def scheme_ar_no(self, value):
        self._scheme_ar_no = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value
    @property
    def signed(self):
        return self._signed

    @signed.setter
    def signed(self, value):
        self._signed = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradePayerArConsultResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'ip_id' in response:
            self.ip_id = response['ip_id']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'refuse_info' in response:
            self.refuse_info = response['refuse_info']
        if 'scheme_ar_no' in response:
            self.scheme_ar_no = response['scheme_ar_no']
        if 'sign_status' in response:
            self.sign_status = response['sign_status']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
        if 'signed' in response:
            self.signed = response['signed']
