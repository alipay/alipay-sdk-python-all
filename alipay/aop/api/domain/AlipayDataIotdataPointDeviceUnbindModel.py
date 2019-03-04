#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataIotdataPointDeviceUnbindModel(object):

    def __init__(self):
        self._business_id = None
        self._device_id = None
        self._point_id = None
        self._remark = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def point_id(self):
        return self._point_id

    @point_id.setter
    def point_id(self, value):
        self._point_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.point_id:
            if hasattr(self.point_id, 'to_alipay_dict'):
                params['point_id'] = self.point_id.to_alipay_dict()
            else:
                params['point_id'] = self.point_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataIotdataPointDeviceUnbindModel()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'point_id' in d:
            o.point_id = d['point_id']
        if 'remark' in d:
            o.remark = d['remark']
        return o


