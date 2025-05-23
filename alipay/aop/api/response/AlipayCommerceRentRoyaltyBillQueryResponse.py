#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentRoyaltyBillInfoDTO import RentRoyaltyBillInfoDTO


class AlipayCommerceRentRoyaltyBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentRoyaltyBillQueryResponse, self).__init__()
        self._royalty_bill_info_list = None
        self._total_count = None

    @property
    def royalty_bill_info_list(self):
        return self._royalty_bill_info_list

    @royalty_bill_info_list.setter
    def royalty_bill_info_list(self, value):
        if isinstance(value, list):
            self._royalty_bill_info_list = list()
            for i in value:
                if isinstance(i, RentRoyaltyBillInfoDTO):
                    self._royalty_bill_info_list.append(i)
                else:
                    self._royalty_bill_info_list.append(RentRoyaltyBillInfoDTO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentRoyaltyBillQueryResponse, self).parse_response_content(response_content)
        if 'royalty_bill_info_list' in response:
            self.royalty_bill_info_list = response['royalty_bill_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
