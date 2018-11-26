#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DishCategoryEntity import DishCategoryEntity


class KoubeiCateringPosCategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosCategoryQueryResponse, self).__init__()
        self._dish_category_entity = None

    @property
    def dish_category_entity(self):
        return self._dish_category_entity

    @dish_category_entity.setter
    def dish_category_entity(self, value):
        if isinstance(value, DishCategoryEntity):
            self._dish_category_entity = value
        else:
            self._dish_category_entity = DishCategoryEntity.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosCategoryQueryResponse, self).parse_response_content(response_content)
        if 'dish_category_entity' in response:
            self.dish_category_entity = response['dish_category_entity']
