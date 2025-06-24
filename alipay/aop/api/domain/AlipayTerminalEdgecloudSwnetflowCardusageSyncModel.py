#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudSwnetflowCardusageSyncModel(object):

    def __init__(self):
        self._before_day_usage = None
        self._before_month_usage = None
        self._biling_cycle = None
        self._credential_name = None
        self._current_day_usage = None
        self._current_month_usage = None
        self._data_type = None
        self._icc_id = None

    @property
    def before_day_usage(self):
        return self._before_day_usage

    @before_day_usage.setter
    def before_day_usage(self, value):
        self._before_day_usage = value
    @property
    def before_month_usage(self):
        return self._before_month_usage

    @before_month_usage.setter
    def before_month_usage(self, value):
        self._before_month_usage = value
    @property
    def biling_cycle(self):
        return self._biling_cycle

    @biling_cycle.setter
    def biling_cycle(self, value):
        self._biling_cycle = value
    @property
    def credential_name(self):
        return self._credential_name

    @credential_name.setter
    def credential_name(self, value):
        self._credential_name = value
    @property
    def current_day_usage(self):
        return self._current_day_usage

    @current_day_usage.setter
    def current_day_usage(self, value):
        self._current_day_usage = value
    @property
    def current_month_usage(self):
        return self._current_month_usage

    @current_month_usage.setter
    def current_month_usage(self, value):
        self._current_month_usage = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def icc_id(self):
        return self._icc_id

    @icc_id.setter
    def icc_id(self, value):
        self._icc_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.before_day_usage:
            if hasattr(self.before_day_usage, 'to_alipay_dict'):
                params['before_day_usage'] = self.before_day_usage.to_alipay_dict()
            else:
                params['before_day_usage'] = self.before_day_usage
        if self.before_month_usage:
            if hasattr(self.before_month_usage, 'to_alipay_dict'):
                params['before_month_usage'] = self.before_month_usage.to_alipay_dict()
            else:
                params['before_month_usage'] = self.before_month_usage
        if self.biling_cycle:
            if hasattr(self.biling_cycle, 'to_alipay_dict'):
                params['biling_cycle'] = self.biling_cycle.to_alipay_dict()
            else:
                params['biling_cycle'] = self.biling_cycle
        if self.credential_name:
            if hasattr(self.credential_name, 'to_alipay_dict'):
                params['credential_name'] = self.credential_name.to_alipay_dict()
            else:
                params['credential_name'] = self.credential_name
        if self.current_day_usage:
            if hasattr(self.current_day_usage, 'to_alipay_dict'):
                params['current_day_usage'] = self.current_day_usage.to_alipay_dict()
            else:
                params['current_day_usage'] = self.current_day_usage
        if self.current_month_usage:
            if hasattr(self.current_month_usage, 'to_alipay_dict'):
                params['current_month_usage'] = self.current_month_usage.to_alipay_dict()
            else:
                params['current_month_usage'] = self.current_month_usage
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.icc_id:
            if hasattr(self.icc_id, 'to_alipay_dict'):
                params['icc_id'] = self.icc_id.to_alipay_dict()
            else:
                params['icc_id'] = self.icc_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudSwnetflowCardusageSyncModel()
        if 'before_day_usage' in d:
            o.before_day_usage = d['before_day_usage']
        if 'before_month_usage' in d:
            o.before_month_usage = d['before_month_usage']
        if 'biling_cycle' in d:
            o.biling_cycle = d['biling_cycle']
        if 'credential_name' in d:
            o.credential_name = d['credential_name']
        if 'current_day_usage' in d:
            o.current_day_usage = d['current_day_usage']
        if 'current_month_usage' in d:
            o.current_month_usage = d['current_month_usage']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'icc_id' in d:
            o.icc_id = d['icc_id']
        return o


