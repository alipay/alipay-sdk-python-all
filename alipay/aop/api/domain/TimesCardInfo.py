#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BreakCostsInfo import BreakCostsInfo
from alipay.aop.api.domain.UseDuration import UseDuration


class TimesCardInfo(object):

    def __init__(self):
        self._break_costs_info = None
        self._funding_model = None
        self._limit_num = None
        self._limit_type = None
        self._remain_stock = None
        self._stock_num = None
        self._support_withdraw = None
        self._use_duration = None

    @property
    def break_costs_info(self):
        return self._break_costs_info

    @break_costs_info.setter
    def break_costs_info(self, value):
        if isinstance(value, BreakCostsInfo):
            self._break_costs_info = value
        else:
            self._break_costs_info = BreakCostsInfo.from_alipay_dict(value)
    @property
    def funding_model(self):
        return self._funding_model

    @funding_model.setter
    def funding_model(self, value):
        if isinstance(value, list):
            self._funding_model = list()
            for i in value:
                self._funding_model.append(i)
    @property
    def limit_num(self):
        return self._limit_num

    @limit_num.setter
    def limit_num(self, value):
        self._limit_num = value
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def remain_stock(self):
        return self._remain_stock

    @remain_stock.setter
    def remain_stock(self, value):
        self._remain_stock = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def support_withdraw(self):
        return self._support_withdraw

    @support_withdraw.setter
    def support_withdraw(self, value):
        self._support_withdraw = value
    @property
    def use_duration(self):
        return self._use_duration

    @use_duration.setter
    def use_duration(self, value):
        if isinstance(value, UseDuration):
            self._use_duration = value
        else:
            self._use_duration = UseDuration.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.break_costs_info:
            if hasattr(self.break_costs_info, 'to_alipay_dict'):
                params['break_costs_info'] = self.break_costs_info.to_alipay_dict()
            else:
                params['break_costs_info'] = self.break_costs_info
        if self.funding_model:
            if isinstance(self.funding_model, list):
                for i in range(0, len(self.funding_model)):
                    element = self.funding_model[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.funding_model[i] = element.to_alipay_dict()
            if hasattr(self.funding_model, 'to_alipay_dict'):
                params['funding_model'] = self.funding_model.to_alipay_dict()
            else:
                params['funding_model'] = self.funding_model
        if self.limit_num:
            if hasattr(self.limit_num, 'to_alipay_dict'):
                params['limit_num'] = self.limit_num.to_alipay_dict()
            else:
                params['limit_num'] = self.limit_num
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        if self.remain_stock:
            if hasattr(self.remain_stock, 'to_alipay_dict'):
                params['remain_stock'] = self.remain_stock.to_alipay_dict()
            else:
                params['remain_stock'] = self.remain_stock
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        if self.support_withdraw:
            if hasattr(self.support_withdraw, 'to_alipay_dict'):
                params['support_withdraw'] = self.support_withdraw.to_alipay_dict()
            else:
                params['support_withdraw'] = self.support_withdraw
        if self.use_duration:
            if hasattr(self.use_duration, 'to_alipay_dict'):
                params['use_duration'] = self.use_duration.to_alipay_dict()
            else:
                params['use_duration'] = self.use_duration
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TimesCardInfo()
        if 'break_costs_info' in d:
            o.break_costs_info = d['break_costs_info']
        if 'funding_model' in d:
            o.funding_model = d['funding_model']
        if 'limit_num' in d:
            o.limit_num = d['limit_num']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        if 'remain_stock' in d:
            o.remain_stock = d['remain_stock']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'support_withdraw' in d:
            o.support_withdraw = d['support_withdraw']
        if 'use_duration' in d:
            o.use_duration = d['use_duration']
        return o


