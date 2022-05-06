#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditPayRefuseVO import CreditPayRefuseVO


class MybankCreditLoantradePayeeArConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePayeeArConsultResponse, self).__init__()
        self._admit = None
        self._admit_alipay_login_id = None
        self._admit_alipay_user_id = None
        self._is_signed = None
        self._refuse_info = None
        self._scheme_ar_no = None
        self._sign_url = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def admit_alipay_login_id(self):
        return self._admit_alipay_login_id

    @admit_alipay_login_id.setter
    def admit_alipay_login_id(self, value):
        self._admit_alipay_login_id = value
    @property
    def admit_alipay_user_id(self):
        return self._admit_alipay_user_id

    @admit_alipay_user_id.setter
    def admit_alipay_user_id(self, value):
        self._admit_alipay_user_id = value
    @property
    def is_signed(self):
        return self._is_signed

    @is_signed.setter
    def is_signed(self, value):
        self._is_signed = value
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
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradePayeeArConsultResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'admit_alipay_login_id' in response:
            self.admit_alipay_login_id = response['admit_alipay_login_id']
        if 'admit_alipay_user_id' in response:
            self.admit_alipay_user_id = response['admit_alipay_user_id']
        if 'is_signed' in response:
            self.is_signed = response['is_signed']
        if 'refuse_info' in response:
            self.refuse_info = response['refuse_info']
        if 'scheme_ar_no' in response:
            self.scheme_ar_no = response['scheme_ar_no']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
