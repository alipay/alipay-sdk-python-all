#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PointAccountLog import PointAccountLog


class AlipayAssetPointAccountlogQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointAccountlogQueryResponse, self).__init__()
        self._current_page = None
        self._page_size = None
        self._point_account_logs = None
        self._total_count = None
        self._total_pages = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def point_account_logs(self):
        return self._point_account_logs

    @point_account_logs.setter
    def point_account_logs(self, value):
        if isinstance(value, list):
            self._point_account_logs = list()
            for i in value:
                if isinstance(i, PointAccountLog):
                    self._point_account_logs.append(i)
                else:
                    self._point_account_logs.append(PointAccountLog.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointAccountlogQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'point_account_logs' in response:
            self.point_account_logs = response['point_account_logs']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
