#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinFwhSignApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinFwhSignApplyResponse, self).__init__()
        self._accepted_no = None
        self._merchant_member_id = None
        self._sign_id = None
        self._sign_link = None

    @property
    def accepted_no(self):
        return self._accepted_no

    @accepted_no.setter
    def accepted_no(self, value):
        self._accepted_no = value
    @property
    def merchant_member_id(self):
        return self._merchant_member_id

    @merchant_member_id.setter
    def merchant_member_id(self, value):
        self._merchant_member_id = value
    @property
    def sign_id(self):
        return self._sign_id

    @sign_id.setter
    def sign_id(self, value):
        self._sign_id = value
    @property
    def sign_link(self):
        return self._sign_link

    @sign_link.setter
    def sign_link(self, value):
        self._sign_link = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinFwhSignApplyResponse, self).parse_response_content(response_content)
        if 'accepted_no' in response:
            self.accepted_no = response['accepted_no']
        if 'merchant_member_id' in response:
            self.merchant_member_id = response['merchant_member_id']
        if 'sign_id' in response:
            self.sign_id = response['sign_id']
        if 'sign_link' in response:
            self.sign_link = response['sign_link']
