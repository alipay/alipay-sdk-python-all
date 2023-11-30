#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCommonAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonAgreementSignResponse, self).__init__()
        self._sign_id = None

    @property
    def sign_id(self):
        return self._sign_id

    @sign_id.setter
    def sign_id(self, value):
        self._sign_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonAgreementSignResponse, self).parse_response_content(response_content)
        if 'sign_id' in response:
            self.sign_id = response['sign_id']
