#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceCompanyclerkCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceCompanyclerkCreateResponse, self).__init__()
        self._company_clerk_id = None
        self._out_clerk_id = None

    @property
    def company_clerk_id(self):
        return self._company_clerk_id

    @company_clerk_id.setter
    def company_clerk_id(self, value):
        self._company_clerk_id = value
    @property
    def out_clerk_id(self):
        return self._out_clerk_id

    @out_clerk_id.setter
    def out_clerk_id(self, value):
        self._out_clerk_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceCompanyclerkCreateResponse, self).parse_response_content(response_content)
        if 'company_clerk_id' in response:
            self.company_clerk_id = response['company_clerk_id']
        if 'out_clerk_id' in response:
            self.out_clerk_id = response['out_clerk_id']
