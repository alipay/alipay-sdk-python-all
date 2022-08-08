#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasPutplanRecoverModel(object):

    def __init__(self):
        self._operator_id = None
        self._put_plan_id = None
        self._tenant_code = None

    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def put_plan_id(self):
        return self._put_plan_id

    @put_plan_id.setter
    def put_plan_id(self, value):
        self._put_plan_id = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.put_plan_id:
            if hasattr(self.put_plan_id, 'to_alipay_dict'):
                params['put_plan_id'] = self.put_plan_id.to_alipay_dict()
            else:
                params['put_plan_id'] = self.put_plan_id
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasPutplanRecoverModel()
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'put_plan_id' in d:
            o.put_plan_id = d['put_plan_id']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


