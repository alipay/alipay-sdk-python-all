#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiTenantInfo(object):

    def __init__(self):
        self._status = None
        self._tenant_desc = None
        self._tenant_name = None
        self._tnt_inst_id = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_desc(self):
        return self._tenant_desc

    @tenant_desc.setter
    def tenant_desc(self, value):
        self._tenant_desc = value
    @property
    def tenant_name(self):
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, value):
        self._tenant_name = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tenant_desc:
            if hasattr(self.tenant_desc, 'to_alipay_dict'):
                params['tenant_desc'] = self.tenant_desc.to_alipay_dict()
            else:
                params['tenant_desc'] = self.tenant_desc
        if self.tenant_name:
            if hasattr(self.tenant_name, 'to_alipay_dict'):
                params['tenant_name'] = self.tenant_name.to_alipay_dict()
            else:
                params['tenant_name'] = self.tenant_name
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiTenantInfo()
        if 'status' in d:
            o.status = d['status']
        if 'tenant_desc' in d:
            o.tenant_desc = d['tenant_desc']
        if 'tenant_name' in d:
            o.tenant_name = d['tenant_name']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


