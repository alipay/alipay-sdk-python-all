#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConsumerProfile import ConsumerProfile
from alipay.aop.api.domain.NearbyCrowdDensity import NearbyCrowdDensity
from alipay.aop.api.domain.RecommendGoods import RecommendGoods
from alipay.aop.api.domain.SalesData import SalesData


class AlipayCommerceIotVendingmachineProfileQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotVendingmachineProfileQueryResponse, self).__init__()
        self._consumer_profile_list = None
        self._nearby_crowd_density_list = None
        self._recommend_goods_list = None
        self._sales_data_list = None

    @property
    def consumer_profile_list(self):
        return self._consumer_profile_list

    @consumer_profile_list.setter
    def consumer_profile_list(self, value):
        if isinstance(value, list):
            self._consumer_profile_list = list()
            for i in value:
                if isinstance(i, ConsumerProfile):
                    self._consumer_profile_list.append(i)
                else:
                    self._consumer_profile_list.append(ConsumerProfile.from_alipay_dict(i))
    @property
    def nearby_crowd_density_list(self):
        return self._nearby_crowd_density_list

    @nearby_crowd_density_list.setter
    def nearby_crowd_density_list(self, value):
        if isinstance(value, list):
            self._nearby_crowd_density_list = list()
            for i in value:
                if isinstance(i, NearbyCrowdDensity):
                    self._nearby_crowd_density_list.append(i)
                else:
                    self._nearby_crowd_density_list.append(NearbyCrowdDensity.from_alipay_dict(i))
    @property
    def recommend_goods_list(self):
        return self._recommend_goods_list

    @recommend_goods_list.setter
    def recommend_goods_list(self, value):
        if isinstance(value, list):
            self._recommend_goods_list = list()
            for i in value:
                if isinstance(i, RecommendGoods):
                    self._recommend_goods_list.append(i)
                else:
                    self._recommend_goods_list.append(RecommendGoods.from_alipay_dict(i))
    @property
    def sales_data_list(self):
        return self._sales_data_list

    @sales_data_list.setter
    def sales_data_list(self, value):
        if isinstance(value, list):
            self._sales_data_list = list()
            for i in value:
                if isinstance(i, SalesData):
                    self._sales_data_list.append(i)
                else:
                    self._sales_data_list.append(SalesData.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotVendingmachineProfileQueryResponse, self).parse_response_content(response_content)
        if 'consumer_profile_list' in response:
            self.consumer_profile_list = response['consumer_profile_list']
        if 'nearby_crowd_density_list' in response:
            self.nearby_crowd_density_list = response['nearby_crowd_density_list']
        if 'recommend_goods_list' in response:
            self.recommend_goods_list = response['recommend_goods_list']
        if 'sales_data_list' in response:
            self.sales_data_list = response['sales_data_list']
