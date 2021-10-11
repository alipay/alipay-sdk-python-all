#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationIsvStatusSyncModel(object):

    def __init__(self):
        self._service_code = None
        self._service_sub_type = None
        self._status = None
        self._store_id = None

    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_sub_type(self):
        return self._service_sub_type

    @service_sub_type.setter
    def service_sub_type(self, value):
        self._service_sub_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_sub_type:
            if hasattr(self.service_sub_type, 'to_alipay_dict'):
                params['service_sub_type'] = self.service_sub_type.to_alipay_dict()
            else:
                params['service_sub_type'] = self.service_sub_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationIsvStatusSyncModel()
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_sub_type' in d:
            o.service_sub_type = d['service_sub_type']
        if 'status' in d:
            o.status = d['status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


