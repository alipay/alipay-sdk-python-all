#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EquipmentAuthRemoveQueryBypageDTO(object):

    def __init__(self):
        self._device_id = None
        self._unbind_time = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def unbind_time(self):
        return self._unbind_time

    @unbind_time.setter
    def unbind_time(self, value):
        self._unbind_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.unbind_time:
            if hasattr(self.unbind_time, 'to_alipay_dict'):
                params['unbind_time'] = self.unbind_time.to_alipay_dict()
            else:
                params['unbind_time'] = self.unbind_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EquipmentAuthRemoveQueryBypageDTO()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'unbind_time' in d:
            o.unbind_time = d['unbind_time']
        return o


