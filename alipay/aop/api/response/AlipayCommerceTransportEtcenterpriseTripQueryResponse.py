#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EtcTripInfo import EtcTripInfo


class AlipayCommerceTransportEtcenterpriseTripQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseTripQueryResponse, self).__init__()
        self._biz_code = None
        self._biz_msg = None
        self._has_next = None
        self._page_num = None
        self._page_size = None
        self._total_page = None
        self._total_size = None
        self._trip_list = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
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
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value
    @property
    def trip_list(self):
        return self._trip_list

    @trip_list.setter
    def trip_list(self, value):
        if isinstance(value, list):
            self._trip_list = list()
            for i in value:
                if isinstance(i, EtcTripInfo):
                    self._trip_list.append(i)
                else:
                    self._trip_list.append(EtcTripInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseTripQueryResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'total_size' in response:
            self.total_size = response['total_size']
        if 'trip_list' in response:
            self.trip_list = response['trip_list']
