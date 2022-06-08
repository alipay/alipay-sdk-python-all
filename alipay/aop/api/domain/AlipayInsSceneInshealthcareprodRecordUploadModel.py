#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInshealthcareprodRecordUploadModel(object):

    def __init__(self):
        self._cid = None
        self._device_battery = None
        self._device_sn = None
        self._device_type = None
        self._device_user = None
        self._lac = None
        self._meal = None
        self._measure_time = None
        self._measure_value = None
        self._mnc = None

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def device_battery(self):
        return self._device_battery

    @device_battery.setter
    def device_battery(self, value):
        self._device_battery = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def device_user(self):
        return self._device_user

    @device_user.setter
    def device_user(self, value):
        self._device_user = value
    @property
    def lac(self):
        return self._lac

    @lac.setter
    def lac(self, value):
        self._lac = value
    @property
    def meal(self):
        return self._meal

    @meal.setter
    def meal(self, value):
        self._meal = value
    @property
    def measure_time(self):
        return self._measure_time

    @measure_time.setter
    def measure_time(self, value):
        self._measure_time = value
    @property
    def measure_value(self):
        return self._measure_value

    @measure_value.setter
    def measure_value(self, value):
        self._measure_value = value
    @property
    def mnc(self):
        return self._mnc

    @mnc.setter
    def mnc(self, value):
        self._mnc = value


    def to_alipay_dict(self):
        params = dict()
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.device_battery:
            if hasattr(self.device_battery, 'to_alipay_dict'):
                params['device_battery'] = self.device_battery.to_alipay_dict()
            else:
                params['device_battery'] = self.device_battery
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.device_user:
            if hasattr(self.device_user, 'to_alipay_dict'):
                params['device_user'] = self.device_user.to_alipay_dict()
            else:
                params['device_user'] = self.device_user
        if self.lac:
            if hasattr(self.lac, 'to_alipay_dict'):
                params['lac'] = self.lac.to_alipay_dict()
            else:
                params['lac'] = self.lac
        if self.meal:
            if hasattr(self.meal, 'to_alipay_dict'):
                params['meal'] = self.meal.to_alipay_dict()
            else:
                params['meal'] = self.meal
        if self.measure_time:
            if hasattr(self.measure_time, 'to_alipay_dict'):
                params['measure_time'] = self.measure_time.to_alipay_dict()
            else:
                params['measure_time'] = self.measure_time
        if self.measure_value:
            if hasattr(self.measure_value, 'to_alipay_dict'):
                params['measure_value'] = self.measure_value.to_alipay_dict()
            else:
                params['measure_value'] = self.measure_value
        if self.mnc:
            if hasattr(self.mnc, 'to_alipay_dict'):
                params['mnc'] = self.mnc.to_alipay_dict()
            else:
                params['mnc'] = self.mnc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInshealthcareprodRecordUploadModel()
        if 'cid' in d:
            o.cid = d['cid']
        if 'device_battery' in d:
            o.device_battery = d['device_battery']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'device_user' in d:
            o.device_user = d['device_user']
        if 'lac' in d:
            o.lac = d['lac']
        if 'meal' in d:
            o.meal = d['meal']
        if 'measure_time' in d:
            o.measure_time = d['measure_time']
        if 'measure_value' in d:
            o.measure_value = d['measure_value']
        if 'mnc' in d:
            o.mnc = d['mnc']
        return o


