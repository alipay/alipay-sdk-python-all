#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO


class OpenApiOperationAnalysisCustomerTrdLvlAliasDTO(object):

    def __init__(self):
        self._alipay_app_id = None
        self._alipay_app_name = None
        self._channel_type = None
        self._dt = None
        self._level_all_uv = None
        self._level_uv = None
        self._level_uv_percent = None
        self._multi_app_id = None
        self._multi_app_name = None
        self._trade_level_granularity = None
        self._traded_level = None

    @property
    def alipay_app_id(self):
        return self._alipay_app_id

    @alipay_app_id.setter
    def alipay_app_id(self, value):
        self._alipay_app_id = value
    @property
    def alipay_app_name(self):
        return self._alipay_app_name

    @alipay_app_name.setter
    def alipay_app_name(self, value):
        self._alipay_app_name = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def level_all_uv(self):
        return self._level_all_uv

    @level_all_uv.setter
    def level_all_uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._level_all_uv = value
        else:
            self._level_all_uv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def level_uv(self):
        return self._level_uv

    @level_uv.setter
    def level_uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._level_uv = value
        else:
            self._level_uv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def level_uv_percent(self):
        return self._level_uv_percent

    @level_uv_percent.setter
    def level_uv_percent(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._level_uv_percent = value
        else:
            self._level_uv_percent = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def multi_app_id(self):
        return self._multi_app_id

    @multi_app_id.setter
    def multi_app_id(self, value):
        self._multi_app_id = value
    @property
    def multi_app_name(self):
        return self._multi_app_name

    @multi_app_name.setter
    def multi_app_name(self, value):
        self._multi_app_name = value
    @property
    def trade_level_granularity(self):
        return self._trade_level_granularity

    @trade_level_granularity.setter
    def trade_level_granularity(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._trade_level_granularity = value
        else:
            self._trade_level_granularity = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def traded_level(self):
        return self._traded_level

    @traded_level.setter
    def traded_level(self, value):
        self._traded_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_app_id:
            if hasattr(self.alipay_app_id, 'to_alipay_dict'):
                params['alipay_app_id'] = self.alipay_app_id.to_alipay_dict()
            else:
                params['alipay_app_id'] = self.alipay_app_id
        if self.alipay_app_name:
            if hasattr(self.alipay_app_name, 'to_alipay_dict'):
                params['alipay_app_name'] = self.alipay_app_name.to_alipay_dict()
            else:
                params['alipay_app_name'] = self.alipay_app_name
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.dt:
            if hasattr(self.dt, 'to_alipay_dict'):
                params['dt'] = self.dt.to_alipay_dict()
            else:
                params['dt'] = self.dt
        if self.level_all_uv:
            if hasattr(self.level_all_uv, 'to_alipay_dict'):
                params['level_all_uv'] = self.level_all_uv.to_alipay_dict()
            else:
                params['level_all_uv'] = self.level_all_uv
        if self.level_uv:
            if hasattr(self.level_uv, 'to_alipay_dict'):
                params['level_uv'] = self.level_uv.to_alipay_dict()
            else:
                params['level_uv'] = self.level_uv
        if self.level_uv_percent:
            if hasattr(self.level_uv_percent, 'to_alipay_dict'):
                params['level_uv_percent'] = self.level_uv_percent.to_alipay_dict()
            else:
                params['level_uv_percent'] = self.level_uv_percent
        if self.multi_app_id:
            if hasattr(self.multi_app_id, 'to_alipay_dict'):
                params['multi_app_id'] = self.multi_app_id.to_alipay_dict()
            else:
                params['multi_app_id'] = self.multi_app_id
        if self.multi_app_name:
            if hasattr(self.multi_app_name, 'to_alipay_dict'):
                params['multi_app_name'] = self.multi_app_name.to_alipay_dict()
            else:
                params['multi_app_name'] = self.multi_app_name
        if self.trade_level_granularity:
            if hasattr(self.trade_level_granularity, 'to_alipay_dict'):
                params['trade_level_granularity'] = self.trade_level_granularity.to_alipay_dict()
            else:
                params['trade_level_granularity'] = self.trade_level_granularity
        if self.traded_level:
            if hasattr(self.traded_level, 'to_alipay_dict'):
                params['traded_level'] = self.traded_level.to_alipay_dict()
            else:
                params['traded_level'] = self.traded_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOperationAnalysisCustomerTrdLvlAliasDTO()
        if 'alipay_app_id' in d:
            o.alipay_app_id = d['alipay_app_id']
        if 'alipay_app_name' in d:
            o.alipay_app_name = d['alipay_app_name']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'dt' in d:
            o.dt = d['dt']
        if 'level_all_uv' in d:
            o.level_all_uv = d['level_all_uv']
        if 'level_uv' in d:
            o.level_uv = d['level_uv']
        if 'level_uv_percent' in d:
            o.level_uv_percent = d['level_uv_percent']
        if 'multi_app_id' in d:
            o.multi_app_id = d['multi_app_id']
        if 'multi_app_name' in d:
            o.multi_app_name = d['multi_app_name']
        if 'trade_level_granularity' in d:
            o.trade_level_granularity = d['trade_level_granularity']
        if 'traded_level' in d:
            o.traded_level = d['traded_level']
        return o


