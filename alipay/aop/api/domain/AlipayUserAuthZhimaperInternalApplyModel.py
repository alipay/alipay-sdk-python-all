#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAuthZhimaperInternalApplyModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._linked_merchant_id = None
        self._mobile = None
        self._name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def linked_merchant_id(self):
        return self._linked_merchant_id

    @linked_merchant_id.setter
    def linked_merchant_id(self, value):
        self._linked_merchant_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.linked_merchant_id:
            if hasattr(self.linked_merchant_id, 'to_alipay_dict'):
                params['linked_merchant_id'] = self.linked_merchant_id.to_alipay_dict()
            else:
                params['linked_merchant_id'] = self.linked_merchant_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAuthZhimaperInternalApplyModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'linked_merchant_id' in d:
            o.linked_merchant_id = d['linked_merchant_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        return o


