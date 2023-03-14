#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlegalchainNdalistQueryModel(object):

    def __init__(self):
        self._app_code = None
        self._instl_id = None
        self._opr_staff_id = None
        self._page = None
        self._sign_status = None
        self._size = None
        self._staff_id = None
        self._staff_name = None
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
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def staff_id(self):
        return self._staff_id

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value
    @property
    def staff_name(self):
        return self._staff_name

    @staff_name.setter
    def staff_name(self, value):
        self._staff_name = value
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
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.staff_id:
            if hasattr(self.staff_id, 'to_alipay_dict'):
                params['staff_id'] = self.staff_id.to_alipay_dict()
            else:
                params['staff_id'] = self.staff_id
        if self.staff_name:
            if hasattr(self.staff_name, 'to_alipay_dict'):
                params['staff_name'] = self.staff_name.to_alipay_dict()
            else:
                params['staff_name'] = self.staff_name
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
        o = AlipayBossProdAntlegalchainNdalistQueryModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'instl_id' in d:
            o.instl_id = d['instl_id']
        if 'opr_staff_id' in d:
            o.opr_staff_id = d['opr_staff_id']
        if 'page' in d:
            o.page = d['page']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        if 'size' in d:
            o.size = d['size']
        if 'staff_id' in d:
            o.staff_id = d['staff_id']
        if 'staff_name' in d:
            o.staff_name = d['staff_name']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


