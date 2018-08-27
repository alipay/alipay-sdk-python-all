#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DishRecommend import DishRecommend


class KoubeiCateringDishRecommendQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishRecommendQueryResponse, self).__init__()
        self._dish_list = None

    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        if isinstance(value, list):
            self._dish_list = list()
            for i in value:
                if isinstance(i, DishRecommend):
                    self._dish_list.append(i)
                else:
                    self._dish_list.append(DishRecommend.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishRecommendQueryResponse, self).parse_response_content(response_content)
        if 'dish_list' in response:
            self.dish_list = response['dish_list']
