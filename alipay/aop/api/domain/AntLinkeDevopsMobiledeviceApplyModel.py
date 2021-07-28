#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntLinkeDevopsMobiledeviceApplyModel(object):

    def __init__(self):
        self._device_id = None
        self._model = None
        self._region = None
        self._take_time = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def take_time(self):
        return self._take_time

    @take_time.setter
    def take_time(self, value):
        self._take_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.model:
            if hasattr(self.model, 'to_alipay_dict'):
                params['model'] = self.model.to_alipay_dict()
            else:
                params['model'] = self.model
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.take_time:
            if hasattr(self.take_time, 'to_alipay_dict'):
                params['take_time'] = self.take_time.to_alipay_dict()
            else:
                params['take_time'] = self.take_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntLinkeDevopsMobiledeviceApplyModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'model' in d:
            o.model = d['model']
        if 'region' in d:
            o.region = d['region']
        if 'take_time' in d:
            o.take_time = d['take_time']
        return o


