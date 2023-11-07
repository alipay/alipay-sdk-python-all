#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardCycleInfo import CardCycleInfo
from alipay.aop.api.domain.CardDiscountRecoverRuleInfo import CardDiscountRecoverRuleInfo
from alipay.aop.api.domain.CardPeriodPriceInfo import CardPeriodPriceInfo
from alipay.aop.api.domain.CardUsableShopInfo import CardUsableShopInfo


class CardTemplateUseInfo(object):

    def __init__(self):
        self._cycle_info = None
        self._discount_recover_rule_info = None
        self._expire_period = None
        self._period_price_list = None
        self._usable_count = None
        self._usable_shop_list = None
        self._use_instruction = None

    @property
    def cycle_info(self):
        return self._cycle_info

    @cycle_info.setter
    def cycle_info(self, value):
        if isinstance(value, CardCycleInfo):
            self._cycle_info = value
        else:
            self._cycle_info = CardCycleInfo.from_alipay_dict(value)
    @property
    def discount_recover_rule_info(self):
        return self._discount_recover_rule_info

    @discount_recover_rule_info.setter
    def discount_recover_rule_info(self, value):
        if isinstance(value, CardDiscountRecoverRuleInfo):
            self._discount_recover_rule_info = value
        else:
            self._discount_recover_rule_info = CardDiscountRecoverRuleInfo.from_alipay_dict(value)
    @property
    def expire_period(self):
        return self._expire_period

    @expire_period.setter
    def expire_period(self, value):
        self._expire_period = value
    @property
    def period_price_list(self):
        return self._period_price_list

    @period_price_list.setter
    def period_price_list(self, value):
        if isinstance(value, list):
            self._period_price_list = list()
            for i in value:
                if isinstance(i, CardPeriodPriceInfo):
                    self._period_price_list.append(i)
                else:
                    self._period_price_list.append(CardPeriodPriceInfo.from_alipay_dict(i))
    @property
    def usable_count(self):
        return self._usable_count

    @usable_count.setter
    def usable_count(self, value):
        self._usable_count = value
    @property
    def usable_shop_list(self):
        return self._usable_shop_list

    @usable_shop_list.setter
    def usable_shop_list(self, value):
        if isinstance(value, list):
            self._usable_shop_list = list()
            for i in value:
                if isinstance(i, CardUsableShopInfo):
                    self._usable_shop_list.append(i)
                else:
                    self._usable_shop_list.append(CardUsableShopInfo.from_alipay_dict(i))
    @property
    def use_instruction(self):
        return self._use_instruction

    @use_instruction.setter
    def use_instruction(self, value):
        self._use_instruction = value


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_info:
            if hasattr(self.cycle_info, 'to_alipay_dict'):
                params['cycle_info'] = self.cycle_info.to_alipay_dict()
            else:
                params['cycle_info'] = self.cycle_info
        if self.discount_recover_rule_info:
            if hasattr(self.discount_recover_rule_info, 'to_alipay_dict'):
                params['discount_recover_rule_info'] = self.discount_recover_rule_info.to_alipay_dict()
            else:
                params['discount_recover_rule_info'] = self.discount_recover_rule_info
        if self.expire_period:
            if hasattr(self.expire_period, 'to_alipay_dict'):
                params['expire_period'] = self.expire_period.to_alipay_dict()
            else:
                params['expire_period'] = self.expire_period
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
        if self.usable_count:
            if hasattr(self.usable_count, 'to_alipay_dict'):
                params['usable_count'] = self.usable_count.to_alipay_dict()
            else:
                params['usable_count'] = self.usable_count
        if self.usable_shop_list:
            if isinstance(self.usable_shop_list, list):
                for i in range(0, len(self.usable_shop_list)):
                    element = self.usable_shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.usable_shop_list[i] = element.to_alipay_dict()
            if hasattr(self.usable_shop_list, 'to_alipay_dict'):
                params['usable_shop_list'] = self.usable_shop_list.to_alipay_dict()
            else:
                params['usable_shop_list'] = self.usable_shop_list
        if self.use_instruction:
            if hasattr(self.use_instruction, 'to_alipay_dict'):
                params['use_instruction'] = self.use_instruction.to_alipay_dict()
            else:
                params['use_instruction'] = self.use_instruction
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardTemplateUseInfo()
        if 'cycle_info' in d:
            o.cycle_info = d['cycle_info']
        if 'discount_recover_rule_info' in d:
            o.discount_recover_rule_info = d['discount_recover_rule_info']
        if 'expire_period' in d:
            o.expire_period = d['expire_period']
        if 'period_price_list' in d:
            o.period_price_list = d['period_price_list']
        if 'usable_count' in d:
            o.usable_count = d['usable_count']
        if 'usable_shop_list' in d:
            o.usable_shop_list = d['usable_shop_list']
        if 'use_instruction' in d:
            o.use_instruction = d['use_instruction']
        return o


