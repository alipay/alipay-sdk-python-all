#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingApartmentAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingApartmentAddResponse, self).__init__()
        self._apartment_id = None

    @property
    def apartment_id(self):
        return self._apartment_id

    @apartment_id.setter
    def apartment_id(self, value):
        self._apartment_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingApartmentAddResponse, self).parse_response_content(response_content)
        if 'apartment_id' in response:
            self.apartment_id = response['apartment_id']
