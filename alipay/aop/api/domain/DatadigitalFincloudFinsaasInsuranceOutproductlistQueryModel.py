#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasInsuranceOutproductlistQueryModel(object):

    def __init__(self):
        self._instance_id = None
        self._out_tenant_id = None

    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def out_tenant_id(self):
        return self._out_tenant_id

    @out_tenant_id.setter
    def out_tenant_id(self, value):
        self._out_tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.out_tenant_id:
            if hasattr(self.out_tenant_id, 'to_alipay_dict'):
                params['out_tenant_id'] = self.out_tenant_id.to_alipay_dict()
            else:
                params['out_tenant_id'] = self.out_tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasInsuranceOutproductlistQueryModel()
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'out_tenant_id' in d:
            o.out_tenant_id = d['out_tenant_id']
        return o


