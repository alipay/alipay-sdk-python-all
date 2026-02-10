#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationPromoActivitySignupResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoActivitySignupResponse, self).__init__()
        self._sign_up_data = None

    @property
    def sign_up_data(self):
        return self._sign_up_data

    @sign_up_data.setter
    def sign_up_data(self, value):
        self._sign_up_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoActivitySignupResponse, self).parse_response_content(response_content)
        if 'sign_up_data' in response:
            self.sign_up_data = response['sign_up_data']
