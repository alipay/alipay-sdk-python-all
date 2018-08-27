#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceHolographicFactorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceHolographicFactorQueryResponse, self).__init__()
        self._cert_no = None
        self._mobile = None
        self._muti_loan_factor_map = None
        self._rsm_factor_map = None
        self._user_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def muti_loan_factor_map(self):
        return self._muti_loan_factor_map

    @muti_loan_factor_map.setter
    def muti_loan_factor_map(self, value):
        self._muti_loan_factor_map = value
    @property
    def rsm_factor_map(self):
        return self._rsm_factor_map

    @rsm_factor_map.setter
    def rsm_factor_map(self, value):
        self._rsm_factor_map = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceHolographicFactorQueryResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'muti_loan_factor_map' in response:
            self.muti_loan_factor_map = response['muti_loan_factor_map']
        if 'rsm_factor_map' in response:
            self.rsm_factor_map = response['rsm_factor_map']
        if 'user_name' in response:
            self.user_name = response['user_name']
