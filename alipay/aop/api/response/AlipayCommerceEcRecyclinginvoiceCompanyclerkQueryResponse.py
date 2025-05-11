#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceCompanyclerkQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceCompanyclerkQueryResponse, self).__init__()
        self._clerk_name = None
        self._clerk_phone = None
        self._clerk_role = None
        self._company_clerk_id = None
        self._out_clerk_id = None

    @property
    def clerk_name(self):
        return self._clerk_name

    @clerk_name.setter
    def clerk_name(self, value):
        self._clerk_name = value
    @property
    def clerk_phone(self):
        return self._clerk_phone

    @clerk_phone.setter
    def clerk_phone(self, value):
        self._clerk_phone = value
    @property
    def clerk_role(self):
        return self._clerk_role

    @clerk_role.setter
    def clerk_role(self, value):
        self._clerk_role = value
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
        response = super(AlipayCommerceEcRecyclinginvoiceCompanyclerkQueryResponse, self).parse_response_content(response_content)
        if 'clerk_name' in response:
            self.clerk_name = response['clerk_name']
        if 'clerk_phone' in response:
            self.clerk_phone = response['clerk_phone']
        if 'clerk_role' in response:
            self.clerk_role = response['clerk_role']
        if 'company_clerk_id' in response:
            self.company_clerk_id = response['company_clerk_id']
        if 'out_clerk_id' in response:
            self.out_clerk_id = response['out_clerk_id']
