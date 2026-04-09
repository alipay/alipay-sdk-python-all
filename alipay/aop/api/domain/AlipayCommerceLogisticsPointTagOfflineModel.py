#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsPointTagOfflineModel(object):

    def __init__(self):
        self._logistics_nfc_id = None
        self._offline_time = None
        self._offline_type = None
        self._sn_id = None
        self._tenant_code = None

    @property
    def logistics_nfc_id(self):
        return self._logistics_nfc_id

    @logistics_nfc_id.setter
    def logistics_nfc_id(self, value):
        self._logistics_nfc_id = value
    @property
    def offline_time(self):
        return self._offline_time

    @offline_time.setter
    def offline_time(self, value):
        self._offline_time = value
    @property
    def offline_type(self):
        return self._offline_type

    @offline_type.setter
    def offline_type(self, value):
        self._offline_type = value
    @property
    def sn_id(self):
        return self._sn_id

    @sn_id.setter
    def sn_id(self, value):
        self._sn_id = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_nfc_id:
            if hasattr(self.logistics_nfc_id, 'to_alipay_dict'):
                params['logistics_nfc_id'] = self.logistics_nfc_id.to_alipay_dict()
            else:
                params['logistics_nfc_id'] = self.logistics_nfc_id
        if self.offline_time:
            if hasattr(self.offline_time, 'to_alipay_dict'):
                params['offline_time'] = self.offline_time.to_alipay_dict()
            else:
                params['offline_time'] = self.offline_time
        if self.offline_type:
            if hasattr(self.offline_type, 'to_alipay_dict'):
                params['offline_type'] = self.offline_type.to_alipay_dict()
            else:
                params['offline_type'] = self.offline_type
        if self.sn_id:
            if hasattr(self.sn_id, 'to_alipay_dict'):
                params['sn_id'] = self.sn_id.to_alipay_dict()
            else:
                params['sn_id'] = self.sn_id
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsPointTagOfflineModel()
        if 'logistics_nfc_id' in d:
            o.logistics_nfc_id = d['logistics_nfc_id']
        if 'offline_time' in d:
            o.offline_time = d['offline_time']
        if 'offline_type' in d:
            o.offline_type = d['offline_type']
        if 'sn_id' in d:
            o.sn_id = d['sn_id']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


