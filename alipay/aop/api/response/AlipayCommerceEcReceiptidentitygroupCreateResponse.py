#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcReceiptidentitygroupCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcReceiptidentitygroupCreateResponse, self).__init__()
        self._identity_group_id = None

    @property
    def identity_group_id(self):
        return self._identity_group_id

    @identity_group_id.setter
    def identity_group_id(self, value):
        self._identity_group_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcReceiptidentitygroupCreateResponse, self).parse_response_content(response_content)
        if 'identity_group_id' in response:
            self.identity_group_id = response['identity_group_id']
