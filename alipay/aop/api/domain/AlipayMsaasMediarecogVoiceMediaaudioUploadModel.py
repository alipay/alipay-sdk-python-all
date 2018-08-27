#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogVoiceMediaaudioUploadModel(object):

    def __init__(self):
        self._data = None
        self._extinfo_a = None
        self._extinfo_b = None
        self._extinfo_c = None
        self._extinfo_d = None
        self._labeltime = None
        self._vname = None
        self._vtype = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def extinfo_a(self):
        return self._extinfo_a

    @extinfo_a.setter
    def extinfo_a(self, value):
        self._extinfo_a = value
    @property
    def extinfo_b(self):
        return self._extinfo_b

    @extinfo_b.setter
    def extinfo_b(self, value):
        self._extinfo_b = value
    @property
    def extinfo_c(self):
        return self._extinfo_c

    @extinfo_c.setter
    def extinfo_c(self, value):
        self._extinfo_c = value
    @property
    def extinfo_d(self):
        return self._extinfo_d

    @extinfo_d.setter
    def extinfo_d(self, value):
        self._extinfo_d = value
    @property
    def labeltime(self):
        return self._labeltime

    @labeltime.setter
    def labeltime(self, value):
        self._labeltime = value
    @property
    def vname(self):
        return self._vname

    @vname.setter
    def vname(self, value):
        self._vname = value
    @property
    def vtype(self):
        return self._vtype

    @vtype.setter
    def vtype(self, value):
        self._vtype = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.extinfo_a:
            if hasattr(self.extinfo_a, 'to_alipay_dict'):
                params['extinfo_a'] = self.extinfo_a.to_alipay_dict()
            else:
                params['extinfo_a'] = self.extinfo_a
        if self.extinfo_b:
            if hasattr(self.extinfo_b, 'to_alipay_dict'):
                params['extinfo_b'] = self.extinfo_b.to_alipay_dict()
            else:
                params['extinfo_b'] = self.extinfo_b
        if self.extinfo_c:
            if hasattr(self.extinfo_c, 'to_alipay_dict'):
                params['extinfo_c'] = self.extinfo_c.to_alipay_dict()
            else:
                params['extinfo_c'] = self.extinfo_c
        if self.extinfo_d:
            if hasattr(self.extinfo_d, 'to_alipay_dict'):
                params['extinfo_d'] = self.extinfo_d.to_alipay_dict()
            else:
                params['extinfo_d'] = self.extinfo_d
        if self.labeltime:
            if hasattr(self.labeltime, 'to_alipay_dict'):
                params['labeltime'] = self.labeltime.to_alipay_dict()
            else:
                params['labeltime'] = self.labeltime
        if self.vname:
            if hasattr(self.vname, 'to_alipay_dict'):
                params['vname'] = self.vname.to_alipay_dict()
            else:
                params['vname'] = self.vname
        if self.vtype:
            if hasattr(self.vtype, 'to_alipay_dict'):
                params['vtype'] = self.vtype.to_alipay_dict()
            else:
                params['vtype'] = self.vtype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogVoiceMediaaudioUploadModel()
        if 'data' in d:
            o.data = d['data']
        if 'extinfo_a' in d:
            o.extinfo_a = d['extinfo_a']
        if 'extinfo_b' in d:
            o.extinfo_b = d['extinfo_b']
        if 'extinfo_c' in d:
            o.extinfo_c = d['extinfo_c']
        if 'extinfo_d' in d:
            o.extinfo_d = d['extinfo_d']
        if 'labeltime' in d:
            o.labeltime = d['labeltime']
        if 'vname' in d:
            o.vname = d['vname']
        if 'vtype' in d:
            o.vtype = d['vtype']
        return o


