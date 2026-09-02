#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EbikeChargeStation import EbikeChargeStation


class AlipayCommerceTransportEbikeChargestationsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEbikeChargestationsQueryResponse, self).__init__()
        self._all_brand_chargestations_link = None
        self._all_brand_chargestations_total = None
        self._ebike_charge_station_list = None
        self._page_no = None
        self._page_size = None
        self._total = None

    @property
    def all_brand_chargestations_link(self):
        return self._all_brand_chargestations_link

    @all_brand_chargestations_link.setter
    def all_brand_chargestations_link(self, value):
        self._all_brand_chargestations_link = value
    @property
    def all_brand_chargestations_total(self):
        return self._all_brand_chargestations_total

    @all_brand_chargestations_total.setter
    def all_brand_chargestations_total(self, value):
        self._all_brand_chargestations_total = value
    @property
    def ebike_charge_station_list(self):
        return self._ebike_charge_station_list

    @ebike_charge_station_list.setter
    def ebike_charge_station_list(self, value):
        if isinstance(value, list):
            self._ebike_charge_station_list = list()
            for i in value:
                if isinstance(i, EbikeChargeStation):
                    self._ebike_charge_station_list.append(i)
                else:
                    self._ebike_charge_station_list.append(EbikeChargeStation.from_alipay_dict(i))
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
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
        response = super(AlipayCommerceTransportEbikeChargestationsQueryResponse, self).parse_response_content(response_content)
        if 'all_brand_chargestations_link' in response:
            self.all_brand_chargestations_link = response['all_brand_chargestations_link']
        if 'all_brand_chargestations_total' in response:
            self.all_brand_chargestations_total = response['all_brand_chargestations_total']
        if 'ebike_charge_station_list' in response:
            self.ebike_charge_station_list = response['ebike_charge_station_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
