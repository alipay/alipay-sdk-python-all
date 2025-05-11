#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ClerkInfo import ClerkInfo


class AlipayCommerceEcRecyclinginvoiceInvoiceclerkQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceInvoiceclerkQueryResponse, self).__init__()
        self._clerk_info_list = None

    @property
    def clerk_info_list(self):
        return self._clerk_info_list

    @clerk_info_list.setter
    def clerk_info_list(self, value):
        if isinstance(value, ClerkInfo):
            self._clerk_info_list = value
        else:
            self._clerk_info_list = ClerkInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceInvoiceclerkQueryResponse, self).parse_response_content(response_content)
        if 'clerk_info_list' in response:
            self.clerk_info_list = response['clerk_info_list']
