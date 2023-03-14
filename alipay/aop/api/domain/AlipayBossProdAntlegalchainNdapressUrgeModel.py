#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlegalchainNdapressUrgeModel(object):

    def __init__(self):
        self._app_code = None
        self._instl_id = None
        self._opr_staff_id = None
        self._staff_ids = None
        self._tenant = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def instl_id(self):
        return self._instl_id

    @instl_id.setter
    def instl_id(self, value):
        self._instl_id = value
    @property
    def opr_staff_id(self):
        return self._opr_staff_id

    @opr_staff_id.setter
    def opr_staff_id(self, value):
        self._opr_staff_id = value
    @property
    def staff_ids(self):
        return self._staff_ids

    @staff_ids.setter
    def staff_ids(self, value):
        if isinstance(value, list):
            self._staff_ids = list()
            for i in value:
                self._staff_ids.append(i)
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.instl_id:
            if hasattr(self.instl_id, 'to_alipay_dict'):
                params['instl_id'] = self.instl_id.to_alipay_dict()
            else:
                params['instl_id'] = self.instl_id
        if self.opr_staff_id:
            if hasattr(self.opr_staff_id, 'to_alipay_dict'):
                params['opr_staff_id'] = self.opr_staff_id.to_alipay_dict()
            else:
                params['opr_staff_id'] = self.opr_staff_id
        if self.staff_ids:
            if isinstance(self.staff_ids, list):
                for i in range(0, len(self.staff_ids)):
                    element = self.staff_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.staff_ids[i] = element.to_alipay_dict()
            if hasattr(self.staff_ids, 'to_alipay_dict'):
                params['staff_ids'] = self.staff_ids.to_alipay_dict()
            else:
                params['staff_ids'] = self.staff_ids
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
        o = AlipayBossProdAntlegalchainNdapressUrgeModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'instl_id' in d:
            o.instl_id = d['instl_id']
        if 'opr_staff_id' in d:
            o.opr_staff_id = d['opr_staff_id']
        if 'staff_ids' in d:
            o.staff_ids = d['staff_ids']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


