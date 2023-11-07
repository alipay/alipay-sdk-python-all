#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcDepartmentUpgradeSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcDepartmentUpgradeSubmitResponse, self).__init__()
        self._process_id = None
        self._sign_url = None

    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcDepartmentUpgradeSubmitResponse, self).parse_response_content(response_content)
        if 'process_id' in response:
            self.process_id = response['process_id']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
