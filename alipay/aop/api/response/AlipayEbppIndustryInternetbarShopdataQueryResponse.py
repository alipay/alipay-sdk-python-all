#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InternetbarShopActivityData import InternetbarShopActivityData


class AlipayEbppIndustryInternetbarShopdataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryInternetbarShopdataQueryResponse, self).__init__()
        self._shop_activity_data = None
        self._total_count = None

    @property
    def shop_activity_data(self):
        return self._shop_activity_data

    @shop_activity_data.setter
    def shop_activity_data(self, value):
        if isinstance(value, list):
            self._shop_activity_data = list()
            for i in value:
                if isinstance(i, InternetbarShopActivityData):
                    self._shop_activity_data.append(i)
                else:
                    self._shop_activity_data.append(InternetbarShopActivityData.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryInternetbarShopdataQueryResponse, self).parse_response_content(response_content)
        if 'shop_activity_data' in response:
            self.shop_activity_data = response['shop_activity_data']
        if 'total_count' in response:
            self.total_count = response['total_count']
