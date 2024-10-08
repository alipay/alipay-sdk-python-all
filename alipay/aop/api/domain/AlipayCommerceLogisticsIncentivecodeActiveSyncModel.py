#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsIncentivecodeActiveSyncModel(object):

    def __init__(self):
        self._active_code_open_id = None
        self._active_code_user_id = None
        self._active_latitude = None
        self._active_longitude = None
        self._active_time = None
        self._active_type = None
        self._incentive_code = None
        self._logistics_code = None

    @property
    def active_code_open_id(self):
        return self._active_code_open_id

    @active_code_open_id.setter
    def active_code_open_id(self, value):
        self._active_code_open_id = value
    @property
    def active_code_user_id(self):
        return self._active_code_user_id

    @active_code_user_id.setter
    def active_code_user_id(self, value):
        self._active_code_user_id = value
    @property
    def active_latitude(self):
        return self._active_latitude

    @active_latitude.setter
    def active_latitude(self, value):
        self._active_latitude = value
    @property
    def active_longitude(self):
        return self._active_longitude

    @active_longitude.setter
    def active_longitude(self, value):
        self._active_longitude = value
    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def active_type(self):
        return self._active_type

    @active_type.setter
    def active_type(self, value):
        self._active_type = value
    @property
    def incentive_code(self):
        return self._incentive_code

    @incentive_code.setter
    def incentive_code(self, value):
        self._incentive_code = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_code_open_id:
            if hasattr(self.active_code_open_id, 'to_alipay_dict'):
                params['active_code_open_id'] = self.active_code_open_id.to_alipay_dict()
            else:
                params['active_code_open_id'] = self.active_code_open_id
        if self.active_code_user_id:
            if hasattr(self.active_code_user_id, 'to_alipay_dict'):
                params['active_code_user_id'] = self.active_code_user_id.to_alipay_dict()
            else:
                params['active_code_user_id'] = self.active_code_user_id
        if self.active_latitude:
            if hasattr(self.active_latitude, 'to_alipay_dict'):
                params['active_latitude'] = self.active_latitude.to_alipay_dict()
            else:
                params['active_latitude'] = self.active_latitude
        if self.active_longitude:
            if hasattr(self.active_longitude, 'to_alipay_dict'):
                params['active_longitude'] = self.active_longitude.to_alipay_dict()
            else:
                params['active_longitude'] = self.active_longitude
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.active_type:
            if hasattr(self.active_type, 'to_alipay_dict'):
                params['active_type'] = self.active_type.to_alipay_dict()
            else:
                params['active_type'] = self.active_type
        if self.incentive_code:
            if hasattr(self.incentive_code, 'to_alipay_dict'):
                params['incentive_code'] = self.incentive_code.to_alipay_dict()
            else:
                params['incentive_code'] = self.incentive_code
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsIncentivecodeActiveSyncModel()
        if 'active_code_open_id' in d:
            o.active_code_open_id = d['active_code_open_id']
        if 'active_code_user_id' in d:
            o.active_code_user_id = d['active_code_user_id']
        if 'active_latitude' in d:
            o.active_latitude = d['active_latitude']
        if 'active_longitude' in d:
            o.active_longitude = d['active_longitude']
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'active_type' in d:
            o.active_type = d['active_type']
        if 'incentive_code' in d:
            o.incentive_code = d['incentive_code']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        return o


