#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YunTaskRankStatistic import YunTaskRankStatistic


class AlipayCommerceYuntaskRankstatisticsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskRankstatisticsQueryResponse, self).__init__()
        self._page = None
        self._page_size = None
        self._rank_statistic = None
        self._total_size = None

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def rank_statistic(self):
        return self._rank_statistic

    @rank_statistic.setter
    def rank_statistic(self, value):
        if isinstance(value, list):
            self._rank_statistic = list()
            for i in value:
                if isinstance(i, YunTaskRankStatistic):
                    self._rank_statistic.append(i)
                else:
                    self._rank_statistic.append(YunTaskRankStatistic.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskRankstatisticsQueryResponse, self).parse_response_content(response_content)
        if 'page' in response:
            self.page = response['page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'rank_statistic' in response:
            self.rank_statistic = response['rank_statistic']
        if 'total_size' in response:
            self.total_size = response['total_size']
