#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MpcDeliveryInfo import MpcDeliveryInfo
from alipay.aop.api.domain.MpcProductResult import MpcProductResult


class SingleOrderVO(object):

    def __init__(self):
        self._can_sell = None
        self._delivery_info_list = None
        self._product_list = None

    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def delivery_info_list(self):
        return self._delivery_info_list

    @delivery_info_list.setter
    def delivery_info_list(self, value):
        if isinstance(value, list):
            self._delivery_info_list = list()
            for i in value:
                if isinstance(i, MpcDeliveryInfo):
                    self._delivery_info_list.append(i)
                else:
                    self._delivery_info_list.append(MpcDeliveryInfo.from_alipay_dict(i))
    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        if isinstance(value, list):
            self._product_list = list()
            for i in value:
                if isinstance(i, MpcProductResult):
                    self._product_list.append(i)
                else:
                    self._product_list.append(MpcProductResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.can_sell:
            if hasattr(self.can_sell, 'to_alipay_dict'):
                params['can_sell'] = self.can_sell.to_alipay_dict()
            else:
                params['can_sell'] = self.can_sell
        if self.delivery_info_list:
            if isinstance(self.delivery_info_list, list):
                for i in range(0, len(self.delivery_info_list)):
                    element = self.delivery_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_info_list[i] = element.to_alipay_dict()
            if hasattr(self.delivery_info_list, 'to_alipay_dict'):
                params['delivery_info_list'] = self.delivery_info_list.to_alipay_dict()
            else:
                params['delivery_info_list'] = self.delivery_info_list
        if self.product_list:
            if isinstance(self.product_list, list):
                for i in range(0, len(self.product_list)):
                    element = self.product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_list[i] = element.to_alipay_dict()
            if hasattr(self.product_list, 'to_alipay_dict'):
                params['product_list'] = self.product_list.to_alipay_dict()
            else:
                params['product_list'] = self.product_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SingleOrderVO()
        if 'can_sell' in d:
            o.can_sell = d['can_sell']
        if 'delivery_info_list' in d:
            o.delivery_info_list = d['delivery_info_list']
        if 'product_list' in d:
            o.product_list = d['product_list']
        return o


