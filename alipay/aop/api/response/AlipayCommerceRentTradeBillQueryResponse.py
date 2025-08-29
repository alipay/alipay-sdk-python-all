#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentBillRoyaltyDetailDto import RentBillRoyaltyDetailDto


class AlipayCommerceRentTradeBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentTradeBillQueryResponse, self).__init__()
        self._rent_royalty_detail = None

    @property
    def rent_royalty_detail(self):
        return self._rent_royalty_detail

    @rent_royalty_detail.setter
    def rent_royalty_detail(self, value):
        if isinstance(value, RentBillRoyaltyDetailDto):
            self._rent_royalty_detail = value
        else:
            self._rent_royalty_detail = RentBillRoyaltyDetailDto.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentTradeBillQueryResponse, self).parse_response_content(response_content)
        if 'rent_royalty_detail' in response:
            self.rent_royalty_detail = response['rent_royalty_detail']
