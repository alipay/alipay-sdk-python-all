#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmpeDeviceModelInfo(object):

    def __init__(self):
        self._hardware_params = None
        self._model_id = None
        self._model_name = None
        self._model_no = None

    @property
    def hardware_params(self):
        return self._hardware_params

    @hardware_params.setter
    def hardware_params(self, value):
        self._hardware_params = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value
    @property
    def model_no(self):
        return self._model_no

    @model_no.setter
    def model_no(self, value):
        self._model_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.hardware_params:
            if hasattr(self.hardware_params, 'to_alipay_dict'):
                params['hardware_params'] = self.hardware_params.to_alipay_dict()
            else:
                params['hardware_params'] = self.hardware_params
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        if self.model_name:
            if hasattr(self.model_name, 'to_alipay_dict'):
                params['model_name'] = self.model_name.to_alipay_dict()
            else:
                params['model_name'] = self.model_name
        if self.model_no:
            if hasattr(self.model_no, 'to_alipay_dict'):
                params['model_no'] = self.model_no.to_alipay_dict()
            else:
                params['model_no'] = self.model_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmpeDeviceModelInfo()
        if 'hardware_params' in d:
            o.hardware_params = d['hardware_params']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'model_name' in d:
            o.model_name = d['model_name']
        if 'model_no' in d:
            o.model_no = d['model_no']
        return o


