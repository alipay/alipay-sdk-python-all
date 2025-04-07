#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingHouseSaleAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingHouseSaleAddResponse, self).__init__()
        self._housing_id = None

    @property
    def housing_id(self):
        return self._housing_id

    @housing_id.setter
    def housing_id(self, value):
        self._housing_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingHouseSaleAddResponse, self).parse_response_content(response_content)
        if 'housing_id' in response:
            self.housing_id = response['housing_id']
