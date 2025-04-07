#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentEnterpriseSealSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentEnterpriseSealSignResponse, self).__init__()
        self._biz_no = None
        self._sign_flow_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentEnterpriseSealSignResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'sign_flow_id' in response:
            self.sign_flow_id = response['sign_flow_id']
