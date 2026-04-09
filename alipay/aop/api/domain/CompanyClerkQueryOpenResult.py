#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyClerkQueryOpenResult(object):

    def __init__(self):
        self._clerk_name = None
        self._clerk_phone = None
        self._clerk_role = None
        self._clerk_status = None
        self._company_clerk_id = None
        self._out_clerk_id = None

    @property
    def clerk_name(self):
        return self._clerk_name

    @clerk_name.setter
    def clerk_name(self, value):
        self._clerk_name = value
    @property
    def clerk_phone(self):
        return self._clerk_phone

    @clerk_phone.setter
    def clerk_phone(self, value):
        self._clerk_phone = value
    @property
    def clerk_role(self):
        return self._clerk_role

    @clerk_role.setter
    def clerk_role(self, value):
        self._clerk_role = value
    @property
    def clerk_status(self):
        return self._clerk_status

    @clerk_status.setter
    def clerk_status(self, value):
        self._clerk_status = value
    @property
    def company_clerk_id(self):
        return self._company_clerk_id

    @company_clerk_id.setter
    def company_clerk_id(self, value):
        self._company_clerk_id = value
    @property
    def out_clerk_id(self):
        return self._out_clerk_id

    @out_clerk_id.setter
    def out_clerk_id(self, value):
        self._out_clerk_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.clerk_name:
            if hasattr(self.clerk_name, 'to_alipay_dict'):
                params['clerk_name'] = self.clerk_name.to_alipay_dict()
            else:
                params['clerk_name'] = self.clerk_name
        if self.clerk_phone:
            if hasattr(self.clerk_phone, 'to_alipay_dict'):
                params['clerk_phone'] = self.clerk_phone.to_alipay_dict()
            else:
                params['clerk_phone'] = self.clerk_phone
        if self.clerk_role:
            if hasattr(self.clerk_role, 'to_alipay_dict'):
                params['clerk_role'] = self.clerk_role.to_alipay_dict()
            else:
                params['clerk_role'] = self.clerk_role
        if self.clerk_status:
            if hasattr(self.clerk_status, 'to_alipay_dict'):
                params['clerk_status'] = self.clerk_status.to_alipay_dict()
            else:
                params['clerk_status'] = self.clerk_status
        if self.company_clerk_id:
            if hasattr(self.company_clerk_id, 'to_alipay_dict'):
                params['company_clerk_id'] = self.company_clerk_id.to_alipay_dict()
            else:
                params['company_clerk_id'] = self.company_clerk_id
        if self.out_clerk_id:
            if hasattr(self.out_clerk_id, 'to_alipay_dict'):
                params['out_clerk_id'] = self.out_clerk_id.to_alipay_dict()
            else:
                params['out_clerk_id'] = self.out_clerk_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyClerkQueryOpenResult()
        if 'clerk_name' in d:
            o.clerk_name = d['clerk_name']
        if 'clerk_phone' in d:
            o.clerk_phone = d['clerk_phone']
        if 'clerk_role' in d:
            o.clerk_role = d['clerk_role']
        if 'clerk_status' in d:
            o.clerk_status = d['clerk_status']
        if 'company_clerk_id' in d:
            o.company_clerk_id = d['company_clerk_id']
        if 'out_clerk_id' in d:
            o.out_clerk_id = d['out_clerk_id']
        return o


