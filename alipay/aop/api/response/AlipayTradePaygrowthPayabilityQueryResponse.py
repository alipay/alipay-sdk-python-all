#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecommendInfo import RecommendInfo


class AlipayTradePaygrowthPayabilityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePaygrowthPayabilityQueryResponse, self).__init__()
        self._enable_to_pay = None
        self._need_recommend = None
        self._recommend_info = None

    @property
    def enable_to_pay(self):
        return self._enable_to_pay

    @enable_to_pay.setter
    def enable_to_pay(self, value):
        self._enable_to_pay = value
    @property
    def need_recommend(self):
        return self._need_recommend

    @need_recommend.setter
    def need_recommend(self, value):
        self._need_recommend = value
    @property
    def recommend_info(self):
        return self._recommend_info

    @recommend_info.setter
    def recommend_info(self, value):
        if isinstance(value, RecommendInfo):
            self._recommend_info = value
        else:
            self._recommend_info = RecommendInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayTradePaygrowthPayabilityQueryResponse, self).parse_response_content(response_content)
        if 'enable_to_pay' in response:
            self.enable_to_pay = response['enable_to_pay']
        if 'need_recommend' in response:
            self.need_recommend = response['need_recommend']
        if 'recommend_info' in response:
            self.recommend_info = response['recommend_info']
