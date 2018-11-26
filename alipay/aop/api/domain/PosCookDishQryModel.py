#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosCookDishCateModel import PosCookDishCateModel
from alipay.aop.api.domain.PosCookDishQryDetailModel import PosCookDishQryDetailModel


class PosCookDishQryModel(object):

    def __init__(self):
        self._cate_list = None
        self._dish_list = None

    @property
    def cate_list(self):
        return self._cate_list

    @cate_list.setter
    def cate_list(self, value):
        if isinstance(value, list):
            self._cate_list = list()
            for i in value:
                if isinstance(i, PosCookDishCateModel):
                    self._cate_list.append(i)
                else:
                    self._cate_list.append(PosCookDishCateModel.from_alipay_dict(i))
    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        if isinstance(value, list):
            self._dish_list = list()
            for i in value:
                if isinstance(i, PosCookDishQryDetailModel):
                    self._dish_list.append(i)
                else:
                    self._dish_list.append(PosCookDishQryDetailModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cate_list:
            if isinstance(self.cate_list, list):
                for i in range(0, len(self.cate_list)):
                    element = self.cate_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cate_list[i] = element.to_alipay_dict()
            if hasattr(self.cate_list, 'to_alipay_dict'):
                params['cate_list'] = self.cate_list.to_alipay_dict()
            else:
                params['cate_list'] = self.cate_list
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
        o = PosCookDishQryModel()
        if 'cate_list' in d:
            o.cate_list = d['cate_list']
        if 'dish_list' in d:
            o.dish_list = d['dish_list']
        return o


