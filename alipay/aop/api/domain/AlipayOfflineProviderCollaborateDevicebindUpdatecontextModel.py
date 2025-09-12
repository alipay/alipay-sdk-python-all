#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UpdateContentExtAttribute import UpdateContentExtAttribute


class AlipayOfflineProviderCollaborateDevicebindUpdatecontextModel(object):

    def __init__(self):
        self._device_sn = None
        self._ext_params = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        if isinstance(value, UpdateContentExtAttribute):
            self._ext_params = value
        else:
            self._ext_params = UpdateContentExtAttribute.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderCollaborateDevicebindUpdatecontextModel()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        return o


