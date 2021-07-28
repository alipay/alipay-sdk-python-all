#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MarketingActivityInfo import MarketingActivityInfo


class AlipayMarketingCampaignSelfActivityBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignSelfActivityBatchqueryResponse, self).__init__()
        self._activity_list = None
        self._current_pages = None
        self._items_per_page = None
        self._total_items = None
        self._total_pages = None

    @property
    def activity_list(self):
        return self._activity_list

    @activity_list.setter
    def activity_list(self, value):
        if isinstance(value, list):
            self._activity_list = list()
            for i in value:
                if isinstance(i, MarketingActivityInfo):
                    self._activity_list.append(i)
                else:
                    self._activity_list.append(MarketingActivityInfo.from_alipay_dict(i))
    @property
    def current_pages(self):
        return self._current_pages

    @current_pages.setter
    def current_pages(self, value):
        self._current_pages = value
    @property
    def items_per_page(self):
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, value):
        self._items_per_page = value
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignSelfActivityBatchqueryResponse, self).parse_response_content(response_content)
        if 'activity_list' in response:
            self.activity_list = response['activity_list']
        if 'current_pages' in response:
            self.current_pages = response['current_pages']
        if 'items_per_page' in response:
            self.items_per_page = response['items_per_page']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
