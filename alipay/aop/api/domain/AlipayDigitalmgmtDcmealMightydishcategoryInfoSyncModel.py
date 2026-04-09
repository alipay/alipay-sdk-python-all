#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DcmealDishCategoryDetail import DcmealDishCategoryDetail


class AlipayDigitalmgmtDcmealMightydishcategoryInfoSyncModel(object):

    def __init__(self):
        self._dish_category_list = None

    @property
    def dish_category_list(self):
        return self._dish_category_list

    @dish_category_list.setter
    def dish_category_list(self, value):
        if isinstance(value, list):
            self._dish_category_list = list()
            for i in value:
                if isinstance(i, DcmealDishCategoryDetail):
                    self._dish_category_list.append(i)
                else:
                    self._dish_category_list.append(DcmealDishCategoryDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.dish_category_list:
            if isinstance(self.dish_category_list, list):
                for i in range(0, len(self.dish_category_list)):
                    element = self.dish_category_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_category_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_category_list, 'to_alipay_dict'):
                params['dish_category_list'] = self.dish_category_list.to_alipay_dict()
            else:
                params['dish_category_list'] = self.dish_category_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtDcmealMightydishcategoryInfoSyncModel()
        if 'dish_category_list' in d:
            o.dish_category_list = d['dish_category_list']
        return o


