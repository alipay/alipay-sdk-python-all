#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmCrmTtsmessageQueryModel(object):

    def __init__(self):
        self._acid = None
        self._tenant_id = None

    @property
    def acid(self):
        return self._acid

    @acid.setter
    def acid(self, value):
        self._acid = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.acid:
            if hasattr(self.acid, 'to_alipay_dict'):
                params['acid'] = self.acid.to_alipay_dict()
            else:
                params['acid'] = self.acid
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmCrmTtsmessageQueryModel()
        if 'acid' in d:
            o.acid = d['acid']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


