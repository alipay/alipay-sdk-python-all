#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ApartmentHouseModelDTO import ApartmentHouseModelDTO


class AlipayCommerceHousingApartmentRentalBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingApartmentRentalBatchqueryResponse, self).__init__()
        self._list = None
        self._page_num = None
        self._page_size = None
        self._total = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, ApartmentHouseModelDTO):
            self._list = value
        else:
            self._list = ApartmentHouseModelDTO.from_alipay_dict(value)
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
        response = super(AlipayCommerceHousingApartmentRentalBatchqueryResponse, self).parse_response_content(response_content)
        if 'list' in response:
            self.list = response['list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
