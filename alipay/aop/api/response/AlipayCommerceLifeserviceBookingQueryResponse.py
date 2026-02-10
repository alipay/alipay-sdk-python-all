#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LifeServiceBookingInfo import LifeServiceBookingInfo


class AlipayCommerceLifeserviceBookingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceBookingQueryResponse, self).__init__()
        self._booking_infos = None
        self._page_num = None
        self._page_size = None
        self._total = None

    @property
    def booking_infos(self):
        return self._booking_infos

    @booking_infos.setter
    def booking_infos(self, value):
        if isinstance(value, list):
            self._booking_infos = list()
            for i in value:
                if isinstance(i, LifeServiceBookingInfo):
                    self._booking_infos.append(i)
                else:
                    self._booking_infos.append(LifeServiceBookingInfo.from_alipay_dict(i))
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
        response = super(AlipayCommerceLifeserviceBookingQueryResponse, self).parse_response_content(response_content)
        if 'booking_infos' in response:
            self.booking_infos = response['booking_infos']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
