#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DishCategoryEntity import DishCategoryEntity


class KoubeiCateringPosCategorylistQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosCategorylistQueryResponse, self).__init__()
        self._category_entity_list = None

    @property
    def category_entity_list(self):
        return self._category_entity_list

    @category_entity_list.setter
    def category_entity_list(self, value):
        if isinstance(value, list):
            self._category_entity_list = list()
            for i in value:
                if isinstance(i, DishCategoryEntity):
                    self._category_entity_list.append(i)
                else:
                    self._category_entity_list.append(DishCategoryEntity.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosCategorylistQueryResponse, self).parse_response_content(response_content)
        if 'category_entity_list' in response:
            self.category_entity_list = response['category_entity_list']
