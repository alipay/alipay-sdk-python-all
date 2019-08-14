#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddressDTO import AddressDTO


class AlipayOpenAppServiceMiniappnearbypoiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServiceMiniappnearbypoiQueryResponse, self).__init__()
        self._addresses = None

    @property
    def addresses(self):
        return self._addresses

    @addresses.setter
    def addresses(self, value):
        if isinstance(value, AddressDTO):
            self._addresses = value
        else:
            self._addresses = AddressDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServiceMiniappnearbypoiQueryResponse, self).parse_response_content(response_content)
        if 'addresses' in response:
            self.addresses = response['addresses']
