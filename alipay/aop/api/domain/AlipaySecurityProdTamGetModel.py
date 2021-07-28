#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdTamGetModel(object):

    def __init__(self):
        self._business_id = None
        self._condition = None
        self._ext_info = None
        self._sp_aik_pub = None
        self._sp_id = None
        self._ta_id = None
        self._ta_version = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def sp_aik_pub(self):
        return self._sp_aik_pub

    @sp_aik_pub.setter
    def sp_aik_pub(self, value):
        self._sp_aik_pub = value
    @property
    def sp_id(self):
        return self._sp_id

    @sp_id.setter
    def sp_id(self, value):
        self._sp_id = value
    @property
    def ta_id(self):
        return self._ta_id

    @ta_id.setter
    def ta_id(self, value):
        self._ta_id = value
    @property
    def ta_version(self):
        return self._ta_version

    @ta_version.setter
    def ta_version(self, value):
        self._ta_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.condition:
            if hasattr(self.condition, 'to_alipay_dict'):
                params['condition'] = self.condition.to_alipay_dict()
            else:
                params['condition'] = self.condition
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.sp_aik_pub:
            if hasattr(self.sp_aik_pub, 'to_alipay_dict'):
                params['sp_aik_pub'] = self.sp_aik_pub.to_alipay_dict()
            else:
                params['sp_aik_pub'] = self.sp_aik_pub
        if self.sp_id:
            if hasattr(self.sp_id, 'to_alipay_dict'):
                params['sp_id'] = self.sp_id.to_alipay_dict()
            else:
                params['sp_id'] = self.sp_id
        if self.ta_id:
            if hasattr(self.ta_id, 'to_alipay_dict'):
                params['ta_id'] = self.ta_id.to_alipay_dict()
            else:
                params['ta_id'] = self.ta_id
        if self.ta_version:
            if hasattr(self.ta_version, 'to_alipay_dict'):
                params['ta_version'] = self.ta_version.to_alipay_dict()
            else:
                params['ta_version'] = self.ta_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdTamGetModel()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'condition' in d:
            o.condition = d['condition']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'sp_aik_pub' in d:
            o.sp_aik_pub = d['sp_aik_pub']
        if 'sp_id' in d:
            o.sp_id = d['sp_id']
        if 'ta_id' in d:
            o.ta_id = d['ta_id']
        if 'ta_version' in d:
            o.ta_version = d['ta_version']
        return o


