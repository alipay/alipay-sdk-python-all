#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PointLogInfo import PointLogInfo


class AlipayCommerceOperationPointHistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPointHistoryQueryResponse, self).__init__()
        self._has_next_page = None
        self._page_number = None
        self._point_amount = None
        self._point_log_list = None
        self._total_pages = None
        self._total_size = None

    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def point_amount(self):
        return self._point_amount

    @point_amount.setter
    def point_amount(self, value):
        self._point_amount = value
    @property
    def point_log_list(self):
        return self._point_log_list

    @point_log_list.setter
    def point_log_list(self, value):
        if isinstance(value, list):
            self._point_log_list = list()
            for i in value:
                if isinstance(i, PointLogInfo):
                    self._point_log_list.append(i)
                else:
                    self._point_log_list.append(PointLogInfo.from_alipay_dict(i))
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
        response = super(AlipayCommerceOperationPointHistoryQueryResponse, self).parse_response_content(response_content)
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
        if 'page_number' in response:
            self.page_number = response['page_number']
        if 'point_amount' in response:
            self.point_amount = response['point_amount']
        if 'point_log_list' in response:
            self.point_log_list = response['point_log_list']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_size' in response:
            self.total_size = response['total_size']
