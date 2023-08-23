#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegisterApplyInfoDTO(object):

    def __init__(self):
        self._apply_id = None
        self._apply_time = None
        self._audit_remark = None
        self._audit_status = None
        self._audit_time = None
        self._enterprise_alias = None
        self._enterprise_email = None
        self._enterprise_id = None
        self._enterprise_name = None
        self._out_biz_no = None
        self._parent_enterprise_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def audit_remark(self):
        return self._audit_remark

    @audit_remark.setter
    def audit_remark(self, value):
        self._audit_remark = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def audit_time(self):
        return self._audit_time

    @audit_time.setter
    def audit_time(self, value):
        self._audit_time = value
    @property
    def enterprise_alias(self):
        return self._enterprise_alias

    @enterprise_alias.setter
    def enterprise_alias(self, value):
        self._enterprise_alias = value
    @property
    def enterprise_email(self):
        return self._enterprise_email

    @enterprise_email.setter
    def enterprise_email(self, value):
        self._enterprise_email = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def parent_enterprise_id(self):
        return self._parent_enterprise_id

    @parent_enterprise_id.setter
    def parent_enterprise_id(self, value):
        self._parent_enterprise_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.audit_remark:
            if hasattr(self.audit_remark, 'to_alipay_dict'):
                params['audit_remark'] = self.audit_remark.to_alipay_dict()
            else:
                params['audit_remark'] = self.audit_remark
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.audit_time:
            if hasattr(self.audit_time, 'to_alipay_dict'):
                params['audit_time'] = self.audit_time.to_alipay_dict()
            else:
                params['audit_time'] = self.audit_time
        if self.enterprise_alias:
            if hasattr(self.enterprise_alias, 'to_alipay_dict'):
                params['enterprise_alias'] = self.enterprise_alias.to_alipay_dict()
            else:
                params['enterprise_alias'] = self.enterprise_alias
        if self.enterprise_email:
            if hasattr(self.enterprise_email, 'to_alipay_dict'):
                params['enterprise_email'] = self.enterprise_email.to_alipay_dict()
            else:
                params['enterprise_email'] = self.enterprise_email
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.parent_enterprise_id:
            if hasattr(self.parent_enterprise_id, 'to_alipay_dict'):
                params['parent_enterprise_id'] = self.parent_enterprise_id.to_alipay_dict()
            else:
                params['parent_enterprise_id'] = self.parent_enterprise_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterApplyInfoDTO()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'audit_remark' in d:
            o.audit_remark = d['audit_remark']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'audit_time' in d:
            o.audit_time = d['audit_time']
        if 'enterprise_alias' in d:
            o.enterprise_alias = d['enterprise_alias']
        if 'enterprise_email' in d:
            o.enterprise_email = d['enterprise_email']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'parent_enterprise_id' in d:
            o.parent_enterprise_id = d['parent_enterprise_id']
        return o


