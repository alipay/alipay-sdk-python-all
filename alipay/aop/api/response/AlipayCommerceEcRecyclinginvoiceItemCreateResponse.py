#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceItemCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceItemCreateResponse, self).__init__()
        self._company_item_id = None
        self._out_item_id = None

    @property
    def company_item_id(self):
        return self._company_item_id

    @company_item_id.setter
    def company_item_id(self, value):
        self._company_item_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceItemCreateResponse, self).parse_response_content(response_content)
        if 'company_item_id' in response:
            self.company_item_id = response['company_item_id']
        if 'out_item_id' in response:
            self.out_item_id = response['out_item_id']
