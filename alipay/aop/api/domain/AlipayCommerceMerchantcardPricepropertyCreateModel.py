#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardPeriodPrice import CardPeriodPrice


class AlipayCommerceMerchantcardPricepropertyCreateModel(object):

    def __init__(self):
        self._card_template_id = None
        self._period_price_list = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def period_price_list(self):
        return self._period_price_list

    @period_price_list.setter
    def period_price_list(self, value):
        if isinstance(value, list):
            self._period_price_list = list()
            for i in value:
                if isinstance(i, CardPeriodPrice):
                    self._period_price_list.append(i)
                else:
                    self._period_price_list.append(CardPeriodPrice.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.period_price_list:
            if isinstance(self.period_price_list, list):
                for i in range(0, len(self.period_price_list)):
                    element = self.period_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.period_price_list[i] = element.to_alipay_dict()
            if hasattr(self.period_price_list, 'to_alipay_dict'):
                params['period_price_list'] = self.period_price_list.to_alipay_dict()
            else:
                params['period_price_list'] = self.period_price_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardPricepropertyCreateModel()
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'period_price_list' in d:
            o.period_price_list = d['period_price_list']
        return o


