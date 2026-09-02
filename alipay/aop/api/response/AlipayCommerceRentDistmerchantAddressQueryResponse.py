#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DistributionMerchantAddressDTO import DistributionMerchantAddressDTO


class AlipayCommerceRentDistmerchantAddressQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentDistmerchantAddressQueryResponse, self).__init__()
        self._addresses = None

    @property
    def addresses(self):
        return self._addresses

    @addresses.setter
    def addresses(self, value):
        if isinstance(value, list):
            self._addresses = list()
            for i in value:
                if isinstance(i, DistributionMerchantAddressDTO):
                    self._addresses.append(i)
                else:
                    self._addresses.append(DistributionMerchantAddressDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentDistmerchantAddressQueryResponse, self).parse_response_content(response_content)
        if 'addresses' in response:
            self.addresses = response['addresses']
