#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEnterpriseAddressModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseAddressModifyResponse, self).__init__()
        self._address_id = None

    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, value):
        self._address_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseAddressModifyResponse, self).parse_response_content(response_content)
        if 'address_id' in response:
            self.address_id = response['address_id']
