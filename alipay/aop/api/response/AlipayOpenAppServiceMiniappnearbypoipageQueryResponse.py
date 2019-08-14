#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddressDTO import AddressDTO


class AlipayOpenAppServiceMiniappnearbypoipageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServiceMiniappnearbypoipageQueryResponse, self).__init__()
        self._addresses = None
        self._page_num = None
        self._page_size = None
        self._total = None

    @property
    def addresses(self):
        return self._addresses

    @addresses.setter
    def addresses(self, value):
        if isinstance(value, AddressDTO):
            self._addresses = value
        else:
            self._addresses = AddressDTO.from_alipay_dict(value)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServiceMiniappnearbypoipageQueryResponse, self).parse_response_content(response_content)
        if 'addresses' in response:
            self.addresses = response['addresses']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
