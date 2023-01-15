#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterpriseAuthApplyDTO(object):

    def __init__(self):
        self._apply_time = None
        self._audit_status = None
        self._auth_apply_id = None
        self._enterprise_code = None
        self._enterprise_name = None
        self._legal_id_number = None
        self._legal_name = None
        self._license_end_date = None
        self._license_img_url = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def auth_apply_id(self):
        return self._auth_apply_id

    @auth_apply_id.setter
    def auth_apply_id(self, value):
        self._auth_apply_id = value
    @property
    def enterprise_code(self):
        return self._enterprise_code

    @enterprise_code.setter
    def enterprise_code(self, value):
        self._enterprise_code = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def legal_id_number(self):
        return self._legal_id_number

    @legal_id_number.setter
    def legal_id_number(self, value):
        self._legal_id_number = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
    @property
    def license_end_date(self):
        return self._license_end_date

    @license_end_date.setter
    def license_end_date(self, value):
        self._license_end_date = value
    @property
    def license_img_url(self):
        return self._license_img_url

    @license_img_url.setter
    def license_img_url(self, value):
        self._license_img_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.auth_apply_id:
            if hasattr(self.auth_apply_id, 'to_alipay_dict'):
                params['auth_apply_id'] = self.auth_apply_id.to_alipay_dict()
            else:
                params['auth_apply_id'] = self.auth_apply_id
        if self.enterprise_code:
            if hasattr(self.enterprise_code, 'to_alipay_dict'):
                params['enterprise_code'] = self.enterprise_code.to_alipay_dict()
            else:
                params['enterprise_code'] = self.enterprise_code
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.legal_id_number:
            if hasattr(self.legal_id_number, 'to_alipay_dict'):
                params['legal_id_number'] = self.legal_id_number.to_alipay_dict()
            else:
                params['legal_id_number'] = self.legal_id_number
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = self.legal_name.to_alipay_dict()
            else:
                params['legal_name'] = self.legal_name
        if self.license_end_date:
            if hasattr(self.license_end_date, 'to_alipay_dict'):
                params['license_end_date'] = self.license_end_date.to_alipay_dict()
            else:
                params['license_end_date'] = self.license_end_date
        if self.license_img_url:
            if hasattr(self.license_img_url, 'to_alipay_dict'):
                params['license_img_url'] = self.license_img_url.to_alipay_dict()
            else:
                params['license_img_url'] = self.license_img_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriseAuthApplyDTO()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'auth_apply_id' in d:
            o.auth_apply_id = d['auth_apply_id']
        if 'enterprise_code' in d:
            o.enterprise_code = d['enterprise_code']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'legal_id_number' in d:
            o.legal_id_number = d['legal_id_number']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'license_end_date' in d:
            o.license_end_date = d['license_end_date']
        if 'license_img_url' in d:
            o.license_img_url = d['license_img_url']
        return o


