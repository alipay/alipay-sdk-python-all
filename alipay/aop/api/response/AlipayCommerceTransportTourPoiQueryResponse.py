#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PoimInfoQueryOpenapiResult import PoimInfoQueryOpenapiResult


class AlipayCommerceTransportTourPoiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTourPoiQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._poim_info_data = None
        self._total_pages = None
        self._total_size = None

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
    def poim_info_data(self):
        return self._poim_info_data

    @poim_info_data.setter
    def poim_info_data(self, value):
        if isinstance(value, PoimInfoQueryOpenapiResult):
            self._poim_info_data = value
        else:
            self._poim_info_data = PoimInfoQueryOpenapiResult.from_alipay_dict(value)
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTourPoiQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'poim_info_data' in response:
            self.poim_info_data = response['poim_info_data']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_size' in response:
            self.total_size = response['total_size']
