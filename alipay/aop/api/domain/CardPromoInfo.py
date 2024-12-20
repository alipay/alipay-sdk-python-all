#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardEachPromoInfo import CardEachPromoInfo


class CardPromoInfo(object):

    def __init__(self):
        self._each_promo_list = None
        self._funding_model = None
        self._total_promo_price = None

    @property
    def each_promo_list(self):
        return self._each_promo_list

    @each_promo_list.setter
    def each_promo_list(self, value):
        if isinstance(value, list):
            self._each_promo_list = list()
            for i in value:
                if isinstance(i, CardEachPromoInfo):
                    self._each_promo_list.append(i)
                else:
                    self._each_promo_list.append(CardEachPromoInfo.from_alipay_dict(i))
    @property
    def funding_model(self):
        return self._funding_model

    @funding_model.setter
    def funding_model(self, value):
        self._funding_model = value
    @property
    def total_promo_price(self):
        return self._total_promo_price

    @total_promo_price.setter
    def total_promo_price(self, value):
        self._total_promo_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.each_promo_list:
            if isinstance(self.each_promo_list, list):
                for i in range(0, len(self.each_promo_list)):
                    element = self.each_promo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.each_promo_list[i] = element.to_alipay_dict()
            if hasattr(self.each_promo_list, 'to_alipay_dict'):
                params['each_promo_list'] = self.each_promo_list.to_alipay_dict()
            else:
                params['each_promo_list'] = self.each_promo_list
        if self.funding_model:
            if hasattr(self.funding_model, 'to_alipay_dict'):
                params['funding_model'] = self.funding_model.to_alipay_dict()
            else:
                params['funding_model'] = self.funding_model
        if self.total_promo_price:
            if hasattr(self.total_promo_price, 'to_alipay_dict'):
                params['total_promo_price'] = self.total_promo_price.to_alipay_dict()
            else:
                params['total_promo_price'] = self.total_promo_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardPromoInfo()
        if 'each_promo_list' in d:
            o.each_promo_list = d['each_promo_list']
        if 'funding_model' in d:
            o.funding_model = d['funding_model']
        if 'total_promo_price' in d:
            o.total_promo_price = d['total_promo_price']
        return o


