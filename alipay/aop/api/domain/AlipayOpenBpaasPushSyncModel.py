#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenBpaasPushSyncModel(object):

    def __init__(self):
        self._bpaas_app_id = None
        self._bpaas_app_version = None
        self._device_sn = None
        self._supplier_id = None

    @property
    def bpaas_app_id(self):
        return self._bpaas_app_id

    @bpaas_app_id.setter
    def bpaas_app_id(self, value):
        self._bpaas_app_id = value
    @property
    def bpaas_app_version(self):
        return self._bpaas_app_version

    @bpaas_app_version.setter
    def bpaas_app_version(self, value):
        self._bpaas_app_version = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        if isinstance(value, list):
            self._device_sn = list()
            for i in value:
                self._device_sn.append(i)
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bpaas_app_id:
            if hasattr(self.bpaas_app_id, 'to_alipay_dict'):
                params['bpaas_app_id'] = self.bpaas_app_id.to_alipay_dict()
            else:
                params['bpaas_app_id'] = self.bpaas_app_id
        if self.bpaas_app_version:
            if hasattr(self.bpaas_app_version, 'to_alipay_dict'):
                params['bpaas_app_version'] = self.bpaas_app_version.to_alipay_dict()
            else:
                params['bpaas_app_version'] = self.bpaas_app_version
        if self.device_sn:
            if isinstance(self.device_sn, list):
                for i in range(0, len(self.device_sn)):
                    element = self.device_sn[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_sn[i] = element.to_alipay_dict()
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenBpaasPushSyncModel()
        if 'bpaas_app_id' in d:
            o.bpaas_app_id = d['bpaas_app_id']
        if 'bpaas_app_version' in d:
            o.bpaas_app_version = d['bpaas_app_version']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


