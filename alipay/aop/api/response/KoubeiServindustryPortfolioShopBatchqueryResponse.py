#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PortfolioInfoOpenModel import PortfolioInfoOpenModel


class KoubeiServindustryPortfolioShopBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryPortfolioShopBatchqueryResponse, self).__init__()
        self._portfolio_count = None
        self._portfolio_info_list = None

    @property
    def portfolio_count(self):
        return self._portfolio_count

    @portfolio_count.setter
    def portfolio_count(self, value):
        self._portfolio_count = value
    @property
    def portfolio_info_list(self):
        return self._portfolio_info_list

    @portfolio_info_list.setter
    def portfolio_info_list(self, value):
        if isinstance(value, list):
            self._portfolio_info_list = list()
            for i in value:
                if isinstance(i, PortfolioInfoOpenModel):
                    self._portfolio_info_list.append(i)
                else:
                    self._portfolio_info_list.append(PortfolioInfoOpenModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryPortfolioShopBatchqueryResponse, self).parse_response_content(response_content)
        if 'portfolio_count' in response:
            self.portfolio_count = response['portfolio_count']
        if 'portfolio_info_list' in response:
            self.portfolio_info_list = response['portfolio_info_list']
