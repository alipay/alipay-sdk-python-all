#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenCertifyMetaInfo(object):

    def __init__(self):
        self._device_type = None

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenCertifyMetaInfo()
        if 'device_type' in d:
            o.device_type = d['device_type']
        return o


