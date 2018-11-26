#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryKmsPubkeyQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._cert_no_hash = None
        self._cert_type = None
        self._sub_biz_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cert_no_hash(self):
        return self._cert_no_hash

    @cert_no_hash.setter
    def cert_no_hash(self, value):
        self._cert_no_hash = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cert_no_hash:
            if hasattr(self.cert_no_hash, 'to_alipay_dict'):
                params['cert_no_hash'] = self.cert_no_hash.to_alipay_dict()
            else:
                params['cert_no_hash'] = self.cert_no_hash
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryKmsPubkeyQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cert_no_hash' in d:
            o.cert_no_hash = d['cert_no_hash']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


