#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DishCategoryEntity import DishCategoryEntity


class KoubeiCateringPosCategorySaveModel(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.category_entity_list:
            if isinstance(self.category_entity_list, list):
                for i in range(0, len(self.category_entity_list)):
                    element = self.category_entity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_entity_list[i] = element.to_alipay_dict()
            if hasattr(self.category_entity_list, 'to_alipay_dict'):
                params['category_entity_list'] = self.category_entity_list.to_alipay_dict()
            else:
                params['category_entity_list'] = self.category_entity_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosCategorySaveModel()
        if 'category_entity_list' in d:
            o.category_entity_list = d['category_entity_list']
        return o


