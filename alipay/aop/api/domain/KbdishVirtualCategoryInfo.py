#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbVirtualShopCategoryDishInfo import KbVirtualShopCategoryDishInfo


class KbdishVirtualCategoryInfo(object):

    def __init__(self):
        self._catetory_id = None
        self._dish_list = None

    @property
    def catetory_id(self):
        return self._catetory_id

    @catetory_id.setter
    def catetory_id(self, value):
        self._catetory_id = value
    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        if isinstance(value, list):
            self._dish_list = list()
            for i in value:
                if isinstance(i, KbVirtualShopCategoryDishInfo):
                    self._dish_list.append(i)
                else:
                    self._dish_list.append(KbVirtualShopCategoryDishInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_id:
            if hasattr(self.catetory_id, 'to_alipay_dict'):
                params['catetory_id'] = self.catetory_id.to_alipay_dict()
            else:
                params['catetory_id'] = self.catetory_id
        if self.dish_list:
            if isinstance(self.dish_list, list):
                for i in range(0, len(self.dish_list)):
                    element = self.dish_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_list, 'to_alipay_dict'):
                params['dish_list'] = self.dish_list.to_alipay_dict()
            else:
                params['dish_list'] = self.dish_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishVirtualCategoryInfo()
        if 'catetory_id' in d:
            o.catetory_id = d['catetory_id']
        if 'dish_list' in d:
            o.dish_list = d['dish_list']
        return o


