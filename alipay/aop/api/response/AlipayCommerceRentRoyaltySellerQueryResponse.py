#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentRoyaltyInfo import RentRoyaltyInfo


class AlipayCommerceRentRoyaltySellerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentRoyaltySellerQueryResponse, self).__init__()
        self._royalty_info = None

    @property
    def royalty_info(self):
        return self._royalty_info

    @royalty_info.setter
    def royalty_info(self, value):
        if isinstance(value, RentRoyaltyInfo):
            self._royalty_info = value
        else:
            self._royalty_info = RentRoyaltyInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentRoyaltySellerQueryResponse, self).parse_response_content(response_content)
        if 'royalty_info' in response:
            self.royalty_info = response['royalty_info']
