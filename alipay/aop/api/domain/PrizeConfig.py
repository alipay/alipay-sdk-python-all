#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CountControlConfig import CountControlConfig
from alipay.aop.api.domain.PrizePriceStrategy import PrizePriceStrategy
from alipay.aop.api.domain.PrizeValidPeriod import PrizeValidPeriod


class PrizeConfig(object):

    def __init__(self):
        self._amount = None
        self._budget_type = None
        self._count_control_config = None
        self._ext_properties = None
        self._gmt_begin = None
        self._gmt_end = None
        self._owner = None
        self._platform_type = None
        self._prize_id = None
        self._prize_name = None
        self._prize_price_strategy = None
        self._prize_type = None
        self._remain_amount = None
        self._status = None
        self._valid_period = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def count_control_config(self):
        return self._count_control_config

    @count_control_config.setter
    def count_control_config(self, value):
        if isinstance(value, list):
            self._count_control_config = list()
            for i in value:
                if isinstance(i, CountControlConfig):
                    self._count_control_config.append(i)
                else:
                    self._count_control_config.append(CountControlConfig.from_alipay_dict(i))
    @property
    def ext_properties(self):
        return self._ext_properties

    @ext_properties.setter
    def ext_properties(self, value):
        self._ext_properties = value
    @property
    def gmt_begin(self):
        return self._gmt_begin

    @gmt_begin.setter
    def gmt_begin(self, value):
        self._gmt_begin = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def platform_type(self):
        return self._platform_type

    @platform_type.setter
    def platform_type(self, value):
        self._platform_type = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_price_strategy(self):
        return self._prize_price_strategy

    @prize_price_strategy.setter
    def prize_price_strategy(self, value):
        if isinstance(value, PrizePriceStrategy):
            self._prize_price_strategy = value
        else:
            self._prize_price_strategy = PrizePriceStrategy.from_alipay_dict(value)
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self._remain_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def valid_period(self):
        return self._valid_period

    @valid_period.setter
    def valid_period(self, value):
        if isinstance(value, PrizeValidPeriod):
            self._valid_period = value
        else:
            self._valid_period = PrizeValidPeriod.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.count_control_config:
            if isinstance(self.count_control_config, list):
                for i in range(0, len(self.count_control_config)):
                    element = self.count_control_config[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.count_control_config[i] = element.to_alipay_dict()
            if hasattr(self.count_control_config, 'to_alipay_dict'):
                params['count_control_config'] = self.count_control_config.to_alipay_dict()
            else:
                params['count_control_config'] = self.count_control_config
        if self.ext_properties:
            if hasattr(self.ext_properties, 'to_alipay_dict'):
                params['ext_properties'] = self.ext_properties.to_alipay_dict()
            else:
                params['ext_properties'] = self.ext_properties
        if self.gmt_begin:
            if hasattr(self.gmt_begin, 'to_alipay_dict'):
                params['gmt_begin'] = self.gmt_begin.to_alipay_dict()
            else:
                params['gmt_begin'] = self.gmt_begin
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.platform_type:
            if hasattr(self.platform_type, 'to_alipay_dict'):
                params['platform_type'] = self.platform_type.to_alipay_dict()
            else:
                params['platform_type'] = self.platform_type
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_price_strategy:
            if hasattr(self.prize_price_strategy, 'to_alipay_dict'):
                params['prize_price_strategy'] = self.prize_price_strategy.to_alipay_dict()
            else:
                params['prize_price_strategy'] = self.prize_price_strategy
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.remain_amount:
            if hasattr(self.remain_amount, 'to_alipay_dict'):
                params['remain_amount'] = self.remain_amount.to_alipay_dict()
            else:
                params['remain_amount'] = self.remain_amount
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.valid_period:
            if hasattr(self.valid_period, 'to_alipay_dict'):
                params['valid_period'] = self.valid_period.to_alipay_dict()
            else:
                params['valid_period'] = self.valid_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizeConfig()
        if 'amount' in d:
            o.amount = d['amount']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'count_control_config' in d:
            o.count_control_config = d['count_control_config']
        if 'ext_properties' in d:
            o.ext_properties = d['ext_properties']
        if 'gmt_begin' in d:
            o.gmt_begin = d['gmt_begin']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'owner' in d:
            o.owner = d['owner']
        if 'platform_type' in d:
            o.platform_type = d['platform_type']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_price_strategy' in d:
            o.prize_price_strategy = d['prize_price_strategy']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'remain_amount' in d:
            o.remain_amount = d['remain_amount']
        if 'status' in d:
            o.status = d['status']
        if 'valid_period' in d:
            o.valid_period = d['valid_period']
        return o


