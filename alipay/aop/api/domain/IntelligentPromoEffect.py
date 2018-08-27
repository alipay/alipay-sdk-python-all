#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IntelligentPromoEffect(object):

    def __init__(self):
        self._avg_prize_increase = None
        self._cost = None
        self._current_total_amount = None
        self._effect_id = None
        self._gmt_from = None
        self._gmt_to = None
        self._gmv = None
        self._remain_stock_num = None
        self._repay_rate_increase = None
        self._send_count_increase = None
        self._take_count = None
        self._type = None
        self._use_count = None

    @property
    def avg_prize_increase(self):
        return self._avg_prize_increase

    @avg_prize_increase.setter
    def avg_prize_increase(self, value):
        self._avg_prize_increase = value
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def current_total_amount(self):
        return self._current_total_amount

    @current_total_amount.setter
    def current_total_amount(self, value):
        self._current_total_amount = value
    @property
    def effect_id(self):
        return self._effect_id

    @effect_id.setter
    def effect_id(self, value):
        self._effect_id = value
    @property
    def gmt_from(self):
        return self._gmt_from

    @gmt_from.setter
    def gmt_from(self, value):
        self._gmt_from = value
    @property
    def gmt_to(self):
        return self._gmt_to

    @gmt_to.setter
    def gmt_to(self, value):
        self._gmt_to = value
    @property
    def gmv(self):
        return self._gmv

    @gmv.setter
    def gmv(self, value):
        self._gmv = value
    @property
    def remain_stock_num(self):
        return self._remain_stock_num

    @remain_stock_num.setter
    def remain_stock_num(self, value):
        self._remain_stock_num = value
    @property
    def repay_rate_increase(self):
        return self._repay_rate_increase

    @repay_rate_increase.setter
    def repay_rate_increase(self, value):
        self._repay_rate_increase = value
    @property
    def send_count_increase(self):
        return self._send_count_increase

    @send_count_increase.setter
    def send_count_increase(self, value):
        self._send_count_increase = value
    @property
    def take_count(self):
        return self._take_count

    @take_count.setter
    def take_count(self, value):
        self._take_count = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def use_count(self):
        return self._use_count

    @use_count.setter
    def use_count(self, value):
        self._use_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_prize_increase:
            if hasattr(self.avg_prize_increase, 'to_alipay_dict'):
                params['avg_prize_increase'] = self.avg_prize_increase.to_alipay_dict()
            else:
                params['avg_prize_increase'] = self.avg_prize_increase
        if self.cost:
            if hasattr(self.cost, 'to_alipay_dict'):
                params['cost'] = self.cost.to_alipay_dict()
            else:
                params['cost'] = self.cost
        if self.current_total_amount:
            if hasattr(self.current_total_amount, 'to_alipay_dict'):
                params['current_total_amount'] = self.current_total_amount.to_alipay_dict()
            else:
                params['current_total_amount'] = self.current_total_amount
        if self.effect_id:
            if hasattr(self.effect_id, 'to_alipay_dict'):
                params['effect_id'] = self.effect_id.to_alipay_dict()
            else:
                params['effect_id'] = self.effect_id
        if self.gmt_from:
            if hasattr(self.gmt_from, 'to_alipay_dict'):
                params['gmt_from'] = self.gmt_from.to_alipay_dict()
            else:
                params['gmt_from'] = self.gmt_from
        if self.gmt_to:
            if hasattr(self.gmt_to, 'to_alipay_dict'):
                params['gmt_to'] = self.gmt_to.to_alipay_dict()
            else:
                params['gmt_to'] = self.gmt_to
        if self.gmv:
            if hasattr(self.gmv, 'to_alipay_dict'):
                params['gmv'] = self.gmv.to_alipay_dict()
            else:
                params['gmv'] = self.gmv
        if self.remain_stock_num:
            if hasattr(self.remain_stock_num, 'to_alipay_dict'):
                params['remain_stock_num'] = self.remain_stock_num.to_alipay_dict()
            else:
                params['remain_stock_num'] = self.remain_stock_num
        if self.repay_rate_increase:
            if hasattr(self.repay_rate_increase, 'to_alipay_dict'):
                params['repay_rate_increase'] = self.repay_rate_increase.to_alipay_dict()
            else:
                params['repay_rate_increase'] = self.repay_rate_increase
        if self.send_count_increase:
            if hasattr(self.send_count_increase, 'to_alipay_dict'):
                params['send_count_increase'] = self.send_count_increase.to_alipay_dict()
            else:
                params['send_count_increase'] = self.send_count_increase
        if self.take_count:
            if hasattr(self.take_count, 'to_alipay_dict'):
                params['take_count'] = self.take_count.to_alipay_dict()
            else:
                params['take_count'] = self.take_count
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.use_count:
            if hasattr(self.use_count, 'to_alipay_dict'):
                params['use_count'] = self.use_count.to_alipay_dict()
            else:
                params['use_count'] = self.use_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IntelligentPromoEffect()
        if 'avg_prize_increase' in d:
            o.avg_prize_increase = d['avg_prize_increase']
        if 'cost' in d:
            o.cost = d['cost']
        if 'current_total_amount' in d:
            o.current_total_amount = d['current_total_amount']
        if 'effect_id' in d:
            o.effect_id = d['effect_id']
        if 'gmt_from' in d:
            o.gmt_from = d['gmt_from']
        if 'gmt_to' in d:
            o.gmt_to = d['gmt_to']
        if 'gmv' in d:
            o.gmv = d['gmv']
        if 'remain_stock_num' in d:
            o.remain_stock_num = d['remain_stock_num']
        if 'repay_rate_increase' in d:
            o.repay_rate_increase = d['repay_rate_increase']
        if 'send_count_increase' in d:
            o.send_count_increase = d['send_count_increase']
        if 'take_count' in d:
            o.take_count = d['take_count']
        if 'type' in d:
            o.type = d['type']
        if 'use_count' in d:
            o.use_count = d['use_count']
        return o


