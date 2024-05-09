#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupEntryCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupEntryCreateResponse, self).__init__()
        self._binding_link = None

    @property
    def binding_link(self):
        return self._binding_link

    @binding_link.setter
    def binding_link(self, value):
        self._binding_link = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupEntryCreateResponse, self).parse_response_content(response_content)
        if 'binding_link' in response:
            self.binding_link = response['binding_link']
