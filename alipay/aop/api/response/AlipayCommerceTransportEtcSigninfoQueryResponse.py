#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcSigninfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcSigninfoQueryResponse, self).__init__()
        self._biz_agreement_no = None
        self._sign_status = None
        self._sign_status_code = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def sign_status_code(self):
        return self._sign_status_code

    @sign_status_code.setter
    def sign_status_code(self, value):
        self._sign_status_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcSigninfoQueryResponse, self).parse_response_content(response_content)
        if 'biz_agreement_no' in response:
            self.biz_agreement_no = response['biz_agreement_no']
        if 'sign_status' in response:
            self.sign_status = response['sign_status']
        if 'sign_status_code' in response:
            self.sign_status_code = response['sign_status_code']
