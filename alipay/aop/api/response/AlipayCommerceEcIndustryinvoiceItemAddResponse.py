#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcIndustryinvoiceItemAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcIndustryinvoiceItemAddResponse, self).__init__()
        self._company_item_id = None

    @property
    def company_item_id(self):
        return self._company_item_id

    @company_item_id.setter
    def company_item_id(self, value):
        self._company_item_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcIndustryinvoiceItemAddResponse, self).parse_response_content(response_content)
        if 'company_item_id' in response:
            self.company_item_id = response['company_item_id']
