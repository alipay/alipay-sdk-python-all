#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseBcClustermsgQueryModel(object):

    def __init__(self):
        self._operate_business_id = None
        self._tenant_id = None

    @property
    def operate_business_id(self):
        return self._operate_business_id

    @operate_business_id.setter
    def operate_business_id(self, value):
        self._operate_business_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operate_business_id:
            if hasattr(self.operate_business_id, 'to_alipay_dict'):
                params['operate_business_id'] = self.operate_business_id.to_alipay_dict()
            else:
                params['operate_business_id'] = self.operate_business_id
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
        o = AlipaySocialBaseBcClustermsgQueryModel()
        if 'operate_business_id' in d:
            o.operate_business_id = d['operate_business_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


