#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingApartmentRentalAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingApartmentRentalAddResponse, self).__init__()
        self._apartment_house_id = None

    @property
    def apartment_house_id(self):
        return self._apartment_house_id

    @apartment_house_id.setter
    def apartment_house_id(self, value):
        self._apartment_house_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingApartmentRentalAddResponse, self).parse_response_content(response_content)
        if 'apartment_house_id' in response:
            self.apartment_house_id = response['apartment_house_id']
