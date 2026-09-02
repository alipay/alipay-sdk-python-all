#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGpStoreidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGpStoreidQueryResponse, self).__init__()
        self._a_store_id = None

    @property
    def a_store_id(self):
        return self._a_store_id

    @a_store_id.setter
    def a_store_id(self, value):
        self._a_store_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGpStoreidQueryResponse, self).parse_response_content(response_content)
        if 'a_store_id' in response:
            self.a_store_id = response['a_store_id']
