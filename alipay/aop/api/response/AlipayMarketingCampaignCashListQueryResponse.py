#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CashCampaignInfo import CashCampaignInfo


class AlipayMarketingCampaignCashListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignCashListQueryResponse, self).__init__()
        self._camp_list = None
        self._page_index = None
        self._page_size = None
        self._total_size = None

    @property
    def camp_list(self):
        return self._camp_list

    @camp_list.setter
    def camp_list(self, value):
        if isinstance(value, list):
            self._camp_list = list()
            for i in value:
                if isinstance(i, CashCampaignInfo):
                    self._camp_list.append(i)
                else:
                    self._camp_list.append(CashCampaignInfo.from_alipay_dict(i))
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignCashListQueryResponse, self).parse_response_content(response_content)
        if 'camp_list' in response:
            self.camp_list = response['camp_list']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
