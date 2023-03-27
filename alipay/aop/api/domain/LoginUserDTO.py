#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LabelDTO import LabelDTO


class LoginUserDTO(object):

    def __init__(self):
        self._ip_role_id = None
        self._tenant_ext_info = None
        self._tenant_id = None
        self._tenant_name = None
        self._tenant_status = None

    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def tenant_ext_info(self):
        return self._tenant_ext_info

    @tenant_ext_info.setter
    def tenant_ext_info(self, value):
        if isinstance(value, LabelDTO):
            self._tenant_ext_info = value
        else:
            self._tenant_ext_info = LabelDTO.from_alipay_dict(value)
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def tenant_name(self):
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, value):
        self._tenant_name = value
    @property
    def tenant_status(self):
        return self._tenant_status

    @tenant_status.setter
    def tenant_status(self, value):
        self._tenant_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.tenant_ext_info:
            if hasattr(self.tenant_ext_info, 'to_alipay_dict'):
                params['tenant_ext_info'] = self.tenant_ext_info.to_alipay_dict()
            else:
                params['tenant_ext_info'] = self.tenant_ext_info
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.tenant_name:
            if hasattr(self.tenant_name, 'to_alipay_dict'):
                params['tenant_name'] = self.tenant_name.to_alipay_dict()
            else:
                params['tenant_name'] = self.tenant_name
        if self.tenant_status:
            if hasattr(self.tenant_status, 'to_alipay_dict'):
                params['tenant_status'] = self.tenant_status.to_alipay_dict()
            else:
                params['tenant_status'] = self.tenant_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoginUserDTO()
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'tenant_ext_info' in d:
            o.tenant_ext_info = d['tenant_ext_info']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'tenant_name' in d:
            o.tenant_name = d['tenant_name']
        if 'tenant_status' in d:
            o.tenant_status = d['tenant_status']
        return o


