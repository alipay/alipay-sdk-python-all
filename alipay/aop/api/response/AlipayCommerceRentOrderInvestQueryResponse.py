#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentInfo import RentInfo


class AlipayCommerceRentOrderInvestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentOrderInvestQueryResponse, self).__init__()
        self._rent_info = None

    @property
    def rent_info(self):
        return self._rent_info

    @rent_info.setter
    def rent_info(self, value):
        if isinstance(value, RentInfo):
            self._rent_info = value
        else:
            self._rent_info = RentInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentOrderInvestQueryResponse, self).parse_response_content(response_content)
        if 'rent_info' in response:
            self.rent_info = response['rent_info']
