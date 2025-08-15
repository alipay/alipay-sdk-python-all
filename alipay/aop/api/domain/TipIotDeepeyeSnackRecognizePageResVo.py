#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TipIotDeepeyeSnackRecognizePageResVo(object):

    def __init__(self):
        self._corr_rate = None
        self._corr_session_cnt = None
        self._device_cnt = None
        self._device_id = None
        self._dim = None
        self._dt = None
        self._isv_name = None
        self._isv_pid = None
        self._merchant_cnt = None
        self._merchant_id = None
        self._merchant_name = None
        self._only_1_corr_session_cnt = None
        self._only_1_session_cnt = None
        self._select_rate = None
        self._selectai_session_cnt = None
        self._session_cnt = None
        self._store_cnt = None
        self._store_id = None
        self._store_name = None
        self._time_period = None
        self._top_1_corr_rate = None
        self._top_1_corr_session_cnt = None
        self._weigh_session_cnt = None

    @property
    def corr_rate(self):
        return self._corr_rate

    @corr_rate.setter
    def corr_rate(self, value):
        self._corr_rate = value
    @property
    def corr_session_cnt(self):
        return self._corr_session_cnt

    @corr_session_cnt.setter
    def corr_session_cnt(self, value):
        self._corr_session_cnt = value
    @property
    def device_cnt(self):
        return self._device_cnt

    @device_cnt.setter
    def device_cnt(self, value):
        self._device_cnt = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def dim(self):
        return self._dim

    @dim.setter
    def dim(self, value):
        self._dim = value
    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def merchant_cnt(self):
        return self._merchant_cnt

    @merchant_cnt.setter
    def merchant_cnt(self, value):
        self._merchant_cnt = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def only_1_corr_session_cnt(self):
        return self._only_1_corr_session_cnt

    @only_1_corr_session_cnt.setter
    def only_1_corr_session_cnt(self, value):
        self._only_1_corr_session_cnt = value
    @property
    def only_1_session_cnt(self):
        return self._only_1_session_cnt

    @only_1_session_cnt.setter
    def only_1_session_cnt(self, value):
        self._only_1_session_cnt = value
    @property
    def select_rate(self):
        return self._select_rate

    @select_rate.setter
    def select_rate(self, value):
        self._select_rate = value
    @property
    def selectai_session_cnt(self):
        return self._selectai_session_cnt

    @selectai_session_cnt.setter
    def selectai_session_cnt(self, value):
        self._selectai_session_cnt = value
    @property
    def session_cnt(self):
        return self._session_cnt

    @session_cnt.setter
    def session_cnt(self, value):
        self._session_cnt = value
    @property
    def store_cnt(self):
        return self._store_cnt

    @store_cnt.setter
    def store_cnt(self, value):
        self._store_cnt = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def time_period(self):
        return self._time_period

    @time_period.setter
    def time_period(self, value):
        self._time_period = value
    @property
    def top_1_corr_rate(self):
        return self._top_1_corr_rate

    @top_1_corr_rate.setter
    def top_1_corr_rate(self, value):
        self._top_1_corr_rate = value
    @property
    def top_1_corr_session_cnt(self):
        return self._top_1_corr_session_cnt

    @top_1_corr_session_cnt.setter
    def top_1_corr_session_cnt(self, value):
        self._top_1_corr_session_cnt = value
    @property
    def weigh_session_cnt(self):
        return self._weigh_session_cnt

    @weigh_session_cnt.setter
    def weigh_session_cnt(self, value):
        self._weigh_session_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.corr_rate:
            if hasattr(self.corr_rate, 'to_alipay_dict'):
                params['corr_rate'] = self.corr_rate.to_alipay_dict()
            else:
                params['corr_rate'] = self.corr_rate
        if self.corr_session_cnt:
            if hasattr(self.corr_session_cnt, 'to_alipay_dict'):
                params['corr_session_cnt'] = self.corr_session_cnt.to_alipay_dict()
            else:
                params['corr_session_cnt'] = self.corr_session_cnt
        if self.device_cnt:
            if hasattr(self.device_cnt, 'to_alipay_dict'):
                params['device_cnt'] = self.device_cnt.to_alipay_dict()
            else:
                params['device_cnt'] = self.device_cnt
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.dim:
            if hasattr(self.dim, 'to_alipay_dict'):
                params['dim'] = self.dim.to_alipay_dict()
            else:
                params['dim'] = self.dim
        if self.dt:
            if hasattr(self.dt, 'to_alipay_dict'):
                params['dt'] = self.dt.to_alipay_dict()
            else:
                params['dt'] = self.dt
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.merchant_cnt:
            if hasattr(self.merchant_cnt, 'to_alipay_dict'):
                params['merchant_cnt'] = self.merchant_cnt.to_alipay_dict()
            else:
                params['merchant_cnt'] = self.merchant_cnt
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.only_1_corr_session_cnt:
            if hasattr(self.only_1_corr_session_cnt, 'to_alipay_dict'):
                params['only_1_corr_session_cnt'] = self.only_1_corr_session_cnt.to_alipay_dict()
            else:
                params['only_1_corr_session_cnt'] = self.only_1_corr_session_cnt
        if self.only_1_session_cnt:
            if hasattr(self.only_1_session_cnt, 'to_alipay_dict'):
                params['only_1_session_cnt'] = self.only_1_session_cnt.to_alipay_dict()
            else:
                params['only_1_session_cnt'] = self.only_1_session_cnt
        if self.select_rate:
            if hasattr(self.select_rate, 'to_alipay_dict'):
                params['select_rate'] = self.select_rate.to_alipay_dict()
            else:
                params['select_rate'] = self.select_rate
        if self.selectai_session_cnt:
            if hasattr(self.selectai_session_cnt, 'to_alipay_dict'):
                params['selectai_session_cnt'] = self.selectai_session_cnt.to_alipay_dict()
            else:
                params['selectai_session_cnt'] = self.selectai_session_cnt
        if self.session_cnt:
            if hasattr(self.session_cnt, 'to_alipay_dict'):
                params['session_cnt'] = self.session_cnt.to_alipay_dict()
            else:
                params['session_cnt'] = self.session_cnt
        if self.store_cnt:
            if hasattr(self.store_cnt, 'to_alipay_dict'):
                params['store_cnt'] = self.store_cnt.to_alipay_dict()
            else:
                params['store_cnt'] = self.store_cnt
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.time_period:
            if hasattr(self.time_period, 'to_alipay_dict'):
                params['time_period'] = self.time_period.to_alipay_dict()
            else:
                params['time_period'] = self.time_period
        if self.top_1_corr_rate:
            if hasattr(self.top_1_corr_rate, 'to_alipay_dict'):
                params['top_1_corr_rate'] = self.top_1_corr_rate.to_alipay_dict()
            else:
                params['top_1_corr_rate'] = self.top_1_corr_rate
        if self.top_1_corr_session_cnt:
            if hasattr(self.top_1_corr_session_cnt, 'to_alipay_dict'):
                params['top_1_corr_session_cnt'] = self.top_1_corr_session_cnt.to_alipay_dict()
            else:
                params['top_1_corr_session_cnt'] = self.top_1_corr_session_cnt
        if self.weigh_session_cnt:
            if hasattr(self.weigh_session_cnt, 'to_alipay_dict'):
                params['weigh_session_cnt'] = self.weigh_session_cnt.to_alipay_dict()
            else:
                params['weigh_session_cnt'] = self.weigh_session_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TipIotDeepeyeSnackRecognizePageResVo()
        if 'corr_rate' in d:
            o.corr_rate = d['corr_rate']
        if 'corr_session_cnt' in d:
            o.corr_session_cnt = d['corr_session_cnt']
        if 'device_cnt' in d:
            o.device_cnt = d['device_cnt']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'dim' in d:
            o.dim = d['dim']
        if 'dt' in d:
            o.dt = d['dt']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'merchant_cnt' in d:
            o.merchant_cnt = d['merchant_cnt']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'only_1_corr_session_cnt' in d:
            o.only_1_corr_session_cnt = d['only_1_corr_session_cnt']
        if 'only_1_session_cnt' in d:
            o.only_1_session_cnt = d['only_1_session_cnt']
        if 'select_rate' in d:
            o.select_rate = d['select_rate']
        if 'selectai_session_cnt' in d:
            o.selectai_session_cnt = d['selectai_session_cnt']
        if 'session_cnt' in d:
            o.session_cnt = d['session_cnt']
        if 'store_cnt' in d:
            o.store_cnt = d['store_cnt']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'time_period' in d:
            o.time_period = d['time_period']
        if 'top_1_corr_rate' in d:
            o.top_1_corr_rate = d['top_1_corr_rate']
        if 'top_1_corr_session_cnt' in d:
            o.top_1_corr_session_cnt = d['top_1_corr_session_cnt']
        if 'weigh_session_cnt' in d:
            o.weigh_session_cnt = d['weigh_session_cnt']
        return o


