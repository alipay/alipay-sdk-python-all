#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IifaaDidCdidDetail(object):

    def __init__(self):
        self._alter_code = None
        self._cdid = None
        self._cert_sign = None
        self._vc_id = None

    @property
    def alter_code(self):
        return self._alter_code

    @alter_code.setter
    def alter_code(self, value):
        self._alter_code = value
    @property
    def cdid(self):
        return self._cdid

    @cdid.setter
    def cdid(self, value):
        self._cdid = value
    @property
    def cert_sign(self):
        return self._cert_sign

    @cert_sign.setter
    def cert_sign(self, value):
        self._cert_sign = value
    @property
    def vc_id(self):
        return self._vc_id

    @vc_id.setter
    def vc_id(self, value):
        self._vc_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alter_code:
            if hasattr(self.alter_code, 'to_alipay_dict'):
                params['alter_code'] = self.alter_code.to_alipay_dict()
            else:
                params['alter_code'] = self.alter_code
        if self.cdid:
            if hasattr(self.cdid, 'to_alipay_dict'):
                params['cdid'] = self.cdid.to_alipay_dict()
            else:
                params['cdid'] = self.cdid
        if self.cert_sign:
            if hasattr(self.cert_sign, 'to_alipay_dict'):
                params['cert_sign'] = self.cert_sign.to_alipay_dict()
            else:
                params['cert_sign'] = self.cert_sign
        if self.vc_id:
            if hasattr(self.vc_id, 'to_alipay_dict'):
                params['vc_id'] = self.vc_id.to_alipay_dict()
            else:
                params['vc_id'] = self.vc_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IifaaDidCdidDetail()
        if 'alter_code' in d:
            o.alter_code = d['alter_code']
        if 'cdid' in d:
            o.cdid = d['cdid']
        if 'cert_sign' in d:
            o.cert_sign = d['cert_sign']
        if 'vc_id' in d:
            o.vc_id = d['vc_id']
        return o


