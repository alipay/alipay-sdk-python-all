#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleIovData(object):

    def __init__(self):
        self._iov_desc = None
        self._iov_timestamp = None
        self._iov_type = None
        self._iov_unit = None
        self._iov_value = None

    @property
    def iov_desc(self):
        return self._iov_desc

    @iov_desc.setter
    def iov_desc(self, value):
        self._iov_desc = value
    @property
    def iov_timestamp(self):
        return self._iov_timestamp

    @iov_timestamp.setter
    def iov_timestamp(self, value):
        self._iov_timestamp = value
    @property
    def iov_type(self):
        return self._iov_type

    @iov_type.setter
    def iov_type(self, value):
        self._iov_type = value
    @property
    def iov_unit(self):
        return self._iov_unit

    @iov_unit.setter
    def iov_unit(self, value):
        self._iov_unit = value
    @property
    def iov_value(self):
        return self._iov_value

    @iov_value.setter
    def iov_value(self, value):
        self._iov_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.iov_desc:
            if hasattr(self.iov_desc, 'to_alipay_dict'):
                params['iov_desc'] = self.iov_desc.to_alipay_dict()
            else:
                params['iov_desc'] = self.iov_desc
        if self.iov_timestamp:
            if hasattr(self.iov_timestamp, 'to_alipay_dict'):
                params['iov_timestamp'] = self.iov_timestamp.to_alipay_dict()
            else:
                params['iov_timestamp'] = self.iov_timestamp
        if self.iov_type:
            if hasattr(self.iov_type, 'to_alipay_dict'):
                params['iov_type'] = self.iov_type.to_alipay_dict()
            else:
                params['iov_type'] = self.iov_type
        if self.iov_unit:
            if hasattr(self.iov_unit, 'to_alipay_dict'):
                params['iov_unit'] = self.iov_unit.to_alipay_dict()
            else:
                params['iov_unit'] = self.iov_unit
        if self.iov_value:
            if hasattr(self.iov_value, 'to_alipay_dict'):
                params['iov_value'] = self.iov_value.to_alipay_dict()
            else:
                params['iov_value'] = self.iov_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleIovData()
        if 'iov_desc' in d:
            o.iov_desc = d['iov_desc']
        if 'iov_timestamp' in d:
            o.iov_timestamp = d['iov_timestamp']
        if 'iov_type' in d:
            o.iov_type = d['iov_type']
        if 'iov_unit' in d:
            o.iov_unit = d['iov_unit']
        if 'iov_value' in d:
            o.iov_value = d['iov_value']
        return o


