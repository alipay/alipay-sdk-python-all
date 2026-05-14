#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceFarmerCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceFarmerCreateResponse, self).__init__()
        self._farmer_auth_url = None
        self._farmer_id = None

    @property
    def farmer_auth_url(self):
        return self._farmer_auth_url

    @farmer_auth_url.setter
    def farmer_auth_url(self, value):
        self._farmer_auth_url = value
    @property
    def farmer_id(self):
        return self._farmer_id

    @farmer_id.setter
    def farmer_id(self, value):
        self._farmer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceFarmerCreateResponse, self).parse_response_content(response_content)
        if 'farmer_auth_url' in response:
            self.farmer_auth_url = response['farmer_auth_url']
        if 'farmer_id' in response:
            self.farmer_id = response['farmer_id']
