#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizOrderQueryResponse import BizOrderQueryResponse


class AlipayOfflineMarketApplyorderBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketApplyorderBatchqueryResponse, self).__init__()
        self._biz_order_infos = None
        self._current_page_no = None
        self._page_size = None
        self._total_items = None
        self._total_page_no = None

    @property
    def biz_order_infos(self):
        return self._biz_order_infos

    @biz_order_infos.setter
    def biz_order_infos(self, value):
        if isinstance(value, list):
            self._biz_order_infos = list()
            for i in value:
                if isinstance(i, BizOrderQueryResponse):
                    self._biz_order_infos.append(i)
                else:
                    self._biz_order_infos.append(BizOrderQueryResponse.from_alipay_dict(i))
    @property
    def current_page_no(self):
        return self._current_page_no

    @current_page_no.setter
    def current_page_no(self, value):
        self._current_page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value
    @property
    def total_page_no(self):
        return self._total_page_no

    @total_page_no.setter
    def total_page_no(self, value):
        self._total_page_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketApplyorderBatchqueryResponse, self).parse_response_content(response_content)
        if 'biz_order_infos' in response:
            self.biz_order_infos = response['biz_order_infos']
        if 'current_page_no' in response:
            self.current_page_no = response['current_page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_page_no' in response:
            self.total_page_no = response['total_page_no']
