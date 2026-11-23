#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceIdentityCredentialOpenApiGenerateResult(object):

    def __init__(self):
        self._credential_hex = None
        self._device_id = None
        self._status = None

    @property
    def credential_hex(self):
        return self._credential_hex

    @credential_hex.setter
    def credential_hex(self, value):
        self._credential_hex = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.credential_hex:
            if hasattr(self.credential_hex, 'to_alipay_dict'):
                params['credential_hex'] = self.credential_hex.to_alipay_dict()
            else:
                params['credential_hex'] = self.credential_hex
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceIdentityCredentialOpenApiGenerateResult()
        if 'credential_hex' in d:
            o.credential_hex = d['credential_hex']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'status' in d:
            o.status = d['status']
        return o


