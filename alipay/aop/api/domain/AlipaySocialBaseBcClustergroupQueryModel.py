#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseBcClustergroupQueryModel(object):

    def __init__(self):
        self._cluster_id = None
        self._operate_business_id = None
        self._tenant_id = None

    @property
    def cluster_id(self):
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, value):
        self._cluster_id = value
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
        if self.cluster_id:
            if hasattr(self.cluster_id, 'to_alipay_dict'):
                params['cluster_id'] = self.cluster_id.to_alipay_dict()
            else:
                params['cluster_id'] = self.cluster_id
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
        o = AlipaySocialBaseBcClustergroupQueryModel()
        if 'cluster_id' in d:
            o.cluster_id = d['cluster_id']
        if 'operate_business_id' in d:
            o.operate_business_id = d['operate_business_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


