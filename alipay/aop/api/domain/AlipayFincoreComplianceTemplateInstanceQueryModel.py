#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceTemplateInstanceQueryModel(object):

    def __init__(self):
        self._biz_instance_id = None
        self._source_system_id = None
        self._tenant = None

    @property
    def biz_instance_id(self):
        return self._biz_instance_id

    @biz_instance_id.setter
    def biz_instance_id(self, value):
        self._biz_instance_id = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_instance_id:
            if hasattr(self.biz_instance_id, 'to_alipay_dict'):
                params['biz_instance_id'] = self.biz_instance_id.to_alipay_dict()
            else:
                params['biz_instance_id'] = self.biz_instance_id
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceTemplateInstanceQueryModel()
        if 'biz_instance_id' in d:
            o.biz_instance_id = d['biz_instance_id']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


