#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayUserDeviceInfo import AlipayUserDeviceInfo
from alipay.aop.api.domain.AlipayUserPrincipalInfo import AlipayUserPrincipalInfo


class AlipayUserCustomerIdentifyModel(object):

    def __init__(self):
        self._biz_type = None
        self._device_info = None
        self._ext_info = None
        self._principal = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        if isinstance(value, AlipayUserDeviceInfo):
            self._device_info = value
        else:
            self._device_info = AlipayUserDeviceInfo.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        if isinstance(value, AlipayUserPrincipalInfo):
            self._principal = value
        else:
            self._principal = AlipayUserPrincipalInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCustomerIdentifyModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'principal' in d:
            o.principal = d['principal']
        return o


