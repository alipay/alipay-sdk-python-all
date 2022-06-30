#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YunTaskShopStatisticInfo import YunTaskShopStatisticInfo


class AlipayCommerceYuntaskShopstatisticsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskShopstatisticsQueryResponse, self).__init__()
        self._page = None
        self._page_size = None
        self._task_shop_statistic_info = None
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
    def task_shop_statistic_info(self):
        return self._task_shop_statistic_info

    @task_shop_statistic_info.setter
    def task_shop_statistic_info(self, value):
        if isinstance(value, list):
            self._task_shop_statistic_info = list()
            for i in value:
                if isinstance(i, YunTaskShopStatisticInfo):
                    self._task_shop_statistic_info.append(i)
                else:
                    self._task_shop_statistic_info.append(YunTaskShopStatisticInfo.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskShopstatisticsQueryResponse, self).parse_response_content(response_content)
        if 'page' in response:
            self.page = response['page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'task_shop_statistic_info' in response:
            self.task_shop_statistic_info = response['task_shop_statistic_info']
        if 'total_size' in response:
            self.total_size = response['total_size']
