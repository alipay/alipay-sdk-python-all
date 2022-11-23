#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskStrategy(object):

    def __init__(self):
        self._has_detail = None
        self._strategy_hit_flag = None
        self._strategy_id = None
        self._strategy_name = None
        self._strategy_value = None
        self._strategy_value_status = None
        self._strategy_value_type = None

    @property
    def has_detail(self):
        return self._has_detail

    @has_detail.setter
    def has_detail(self, value):
        self._has_detail = value
    @property
    def strategy_hit_flag(self):
        return self._strategy_hit_flag

    @strategy_hit_flag.setter
    def strategy_hit_flag(self, value):
        self._strategy_hit_flag = value
    @property
    def strategy_id(self):
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, value):
        self._strategy_id = value
    @property
    def strategy_name(self):
        return self._strategy_name

    @strategy_name.setter
    def strategy_name(self, value):
        self._strategy_name = value
    @property
    def strategy_value(self):
        return self._strategy_value

    @strategy_value.setter
    def strategy_value(self, value):
        self._strategy_value = value
    @property
    def strategy_value_status(self):
        return self._strategy_value_status

    @strategy_value_status.setter
    def strategy_value_status(self, value):
        self._strategy_value_status = value
    @property
    def strategy_value_type(self):
        return self._strategy_value_type

    @strategy_value_type.setter
    def strategy_value_type(self, value):
        self._strategy_value_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_detail:
            if hasattr(self.has_detail, 'to_alipay_dict'):
                params['has_detail'] = self.has_detail.to_alipay_dict()
            else:
                params['has_detail'] = self.has_detail
        if self.strategy_hit_flag:
            if hasattr(self.strategy_hit_flag, 'to_alipay_dict'):
                params['strategy_hit_flag'] = self.strategy_hit_flag.to_alipay_dict()
            else:
                params['strategy_hit_flag'] = self.strategy_hit_flag
        if self.strategy_id:
            if hasattr(self.strategy_id, 'to_alipay_dict'):
                params['strategy_id'] = self.strategy_id.to_alipay_dict()
            else:
                params['strategy_id'] = self.strategy_id
        if self.strategy_name:
            if hasattr(self.strategy_name, 'to_alipay_dict'):
                params['strategy_name'] = self.strategy_name.to_alipay_dict()
            else:
                params['strategy_name'] = self.strategy_name
        if self.strategy_value:
            if hasattr(self.strategy_value, 'to_alipay_dict'):
                params['strategy_value'] = self.strategy_value.to_alipay_dict()
            else:
                params['strategy_value'] = self.strategy_value
        if self.strategy_value_status:
            if hasattr(self.strategy_value_status, 'to_alipay_dict'):
                params['strategy_value_status'] = self.strategy_value_status.to_alipay_dict()
            else:
                params['strategy_value_status'] = self.strategy_value_status
        if self.strategy_value_type:
            if hasattr(self.strategy_value_type, 'to_alipay_dict'):
                params['strategy_value_type'] = self.strategy_value_type.to_alipay_dict()
            else:
                params['strategy_value_type'] = self.strategy_value_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskStrategy()
        if 'has_detail' in d:
            o.has_detail = d['has_detail']
        if 'strategy_hit_flag' in d:
            o.strategy_hit_flag = d['strategy_hit_flag']
        if 'strategy_id' in d:
            o.strategy_id = d['strategy_id']
        if 'strategy_name' in d:
            o.strategy_name = d['strategy_name']
        if 'strategy_value' in d:
            o.strategy_value = d['strategy_value']
        if 'strategy_value_status' in d:
            o.strategy_value_status = d['strategy_value_status']
        if 'strategy_value_type' in d:
            o.strategy_value_type = d['strategy_value_type']
        return o


