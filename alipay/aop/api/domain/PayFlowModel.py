#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayFlowShopInfoModel import PayFlowShopInfoModel


class PayFlowModel(object):

    def __init__(self):
        self._is_effective = None
        self._shop_list = None
        self._shop_num = None

    @property
    def is_effective(self):
        return self._is_effective

    @is_effective.setter
    def is_effective(self, value):
        self._is_effective = value
    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                if isinstance(i, PayFlowShopInfoModel):
                    self._shop_list.append(i)
                else:
                    self._shop_list.append(PayFlowShopInfoModel.from_alipay_dict(i))
    @property
    def shop_num(self):
        return self._shop_num

    @shop_num.setter
    def shop_num(self, value):
        self._shop_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_effective:
            if hasattr(self.is_effective, 'to_alipay_dict'):
                params['is_effective'] = self.is_effective.to_alipay_dict()
            else:
                params['is_effective'] = self.is_effective
        if self.shop_list:
            if isinstance(self.shop_list, list):
                for i in range(0, len(self.shop_list)):
                    element = self.shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_list, 'to_alipay_dict'):
                params['shop_list'] = self.shop_list.to_alipay_dict()
            else:
                params['shop_list'] = self.shop_list
        if self.shop_num:
            if hasattr(self.shop_num, 'to_alipay_dict'):
                params['shop_num'] = self.shop_num.to_alipay_dict()
            else:
                params['shop_num'] = self.shop_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayFlowModel()
        if 'is_effective' in d:
            o.is_effective = d['is_effective']
        if 'shop_list' in d:
            o.shop_list = d['shop_list']
        if 'shop_num' in d:
            o.shop_num = d['shop_num']
        return o


