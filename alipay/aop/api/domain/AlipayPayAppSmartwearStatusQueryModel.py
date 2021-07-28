#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppSmartwearStatusQueryModel(object):

    def __init__(self):
        self._device_model = None

    @property
    def device_model(self):
        return self._device_model

    @device_model.setter
    def device_model(self, value):
        self._device_model = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_model:
            if hasattr(self.device_model, 'to_alipay_dict'):
                params['device_model'] = self.device_model.to_alipay_dict()
            else:
                params['device_model'] = self.device_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppSmartwearStatusQueryModel()
        if 'device_model' in d:
            o.device_model = d['device_model']
        return o


