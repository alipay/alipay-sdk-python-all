#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenbizmockMapExt import OpenbizmockMapExt


class SecurityCertProfileExt(object):

    def __init__(self):
        self._biz_type = None
        self._cert_id = None
        self._cert_storage_key = None
        self._cert_unique_id = None
        self._gmt_enable = None
        self._openbizmock_map_ext = None
        self._partner_id = None
        self._sec_id = None
        self._valid_end_time = None
        self._valid_start_time = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cert_id(self):
        return self._cert_id

    @cert_id.setter
    def cert_id(self, value):
        self._cert_id = value
    @property
    def cert_storage_key(self):
        return self._cert_storage_key

    @cert_storage_key.setter
    def cert_storage_key(self, value):
        self._cert_storage_key = value
    @property
    def cert_unique_id(self):
        return self._cert_unique_id

    @cert_unique_id.setter
    def cert_unique_id(self, value):
        self._cert_unique_id = value
    @property
    def gmt_enable(self):
        return self._gmt_enable

    @gmt_enable.setter
    def gmt_enable(self, value):
        self._gmt_enable = value
    @property
    def openbizmock_map_ext(self):
        return self._openbizmock_map_ext

    @openbizmock_map_ext.setter
    def openbizmock_map_ext(self, value):
        if isinstance(value, list):
            self._openbizmock_map_ext = list()
            for i in value:
                if isinstance(i, OpenbizmockMapExt):
                    self._openbizmock_map_ext.append(i)
                else:
                    self._openbizmock_map_ext.append(OpenbizmockMapExt.from_alipay_dict(i))
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def sec_id(self):
        return self._sec_id

    @sec_id.setter
    def sec_id(self, value):
        self._sec_id = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value
    @property
    def valid_start_time(self):
        return self._valid_start_time

    @valid_start_time.setter
    def valid_start_time(self, value):
        self._valid_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cert_id:
            if hasattr(self.cert_id, 'to_alipay_dict'):
                params['cert_id'] = self.cert_id.to_alipay_dict()
            else:
                params['cert_id'] = self.cert_id
        if self.cert_storage_key:
            if hasattr(self.cert_storage_key, 'to_alipay_dict'):
                params['cert_storage_key'] = self.cert_storage_key.to_alipay_dict()
            else:
                params['cert_storage_key'] = self.cert_storage_key
        if self.cert_unique_id:
            if hasattr(self.cert_unique_id, 'to_alipay_dict'):
                params['cert_unique_id'] = self.cert_unique_id.to_alipay_dict()
            else:
                params['cert_unique_id'] = self.cert_unique_id
        if self.gmt_enable:
            if hasattr(self.gmt_enable, 'to_alipay_dict'):
                params['gmt_enable'] = self.gmt_enable.to_alipay_dict()
            else:
                params['gmt_enable'] = self.gmt_enable
        if self.openbizmock_map_ext:
            if isinstance(self.openbizmock_map_ext, list):
                for i in range(0, len(self.openbizmock_map_ext)):
                    element = self.openbizmock_map_ext[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.openbizmock_map_ext[i] = element.to_alipay_dict()
            if hasattr(self.openbizmock_map_ext, 'to_alipay_dict'):
                params['openbizmock_map_ext'] = self.openbizmock_map_ext.to_alipay_dict()
            else:
                params['openbizmock_map_ext'] = self.openbizmock_map_ext
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.sec_id:
            if hasattr(self.sec_id, 'to_alipay_dict'):
                params['sec_id'] = self.sec_id.to_alipay_dict()
            else:
                params['sec_id'] = self.sec_id
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        if self.valid_start_time:
            if hasattr(self.valid_start_time, 'to_alipay_dict'):
                params['valid_start_time'] = self.valid_start_time.to_alipay_dict()
            else:
                params['valid_start_time'] = self.valid_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SecurityCertProfileExt()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cert_id' in d:
            o.cert_id = d['cert_id']
        if 'cert_storage_key' in d:
            o.cert_storage_key = d['cert_storage_key']
        if 'cert_unique_id' in d:
            o.cert_unique_id = d['cert_unique_id']
        if 'gmt_enable' in d:
            o.gmt_enable = d['gmt_enable']
        if 'openbizmock_map_ext' in d:
            o.openbizmock_map_ext = d['openbizmock_map_ext']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'sec_id' in d:
            o.sec_id = d['sec_id']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        if 'valid_start_time' in d:
            o.valid_start_time = d['valid_start_time']
        return o


