#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCardTemplatePriceDateRule import MerchantCardTemplatePriceDateRule
from alipay.aop.api.domain.MerchantCardTemplatePriceWeekRule import MerchantCardTemplatePriceWeekRule


class MerchantCardTemplateCalendarPrice(object):

    def __init__(self):
        self._date_price_list = None
        self._week_price_list = None

    @property
    def date_price_list(self):
        return self._date_price_list

    @date_price_list.setter
    def date_price_list(self, value):
        if isinstance(value, list):
            self._date_price_list = list()
            for i in value:
                if isinstance(i, MerchantCardTemplatePriceDateRule):
                    self._date_price_list.append(i)
                else:
                    self._date_price_list.append(MerchantCardTemplatePriceDateRule.from_alipay_dict(i))
    @property
    def week_price_list(self):
        return self._week_price_list

    @week_price_list.setter
    def week_price_list(self, value):
        if isinstance(value, list):
            self._week_price_list = list()
            for i in value:
                if isinstance(i, MerchantCardTemplatePriceWeekRule):
                    self._week_price_list.append(i)
                else:
                    self._week_price_list.append(MerchantCardTemplatePriceWeekRule.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.date_price_list:
            if isinstance(self.date_price_list, list):
                for i in range(0, len(self.date_price_list)):
                    element = self.date_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.date_price_list[i] = element.to_alipay_dict()
            if hasattr(self.date_price_list, 'to_alipay_dict'):
                params['date_price_list'] = self.date_price_list.to_alipay_dict()
            else:
                params['date_price_list'] = self.date_price_list
        if self.week_price_list:
            if isinstance(self.week_price_list, list):
                for i in range(0, len(self.week_price_list)):
                    element = self.week_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week_price_list[i] = element.to_alipay_dict()
            if hasattr(self.week_price_list, 'to_alipay_dict'):
                params['week_price_list'] = self.week_price_list.to_alipay_dict()
            else:
                params['week_price_list'] = self.week_price_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantCardTemplateCalendarPrice()
        if 'date_price_list' in d:
            o.date_price_list = d['date_price_list']
        if 'week_price_list' in d:
            o.week_price_list = d['week_price_list']
        return o


