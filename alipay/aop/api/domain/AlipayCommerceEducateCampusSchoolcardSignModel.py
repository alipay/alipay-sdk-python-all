#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCampusSchoolcardSignModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._expire_at = None
        self._identity = None
        self._identity_type = None
        self._name = None
        self._school_id = None
        self._student_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def expire_at(self):
        return self._expire_at

    @expire_at.setter
    def expire_at(self, value):
        self._expire_at = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.expire_at:
            if hasattr(self.expire_at, 'to_alipay_dict'):
                params['expire_at'] = self.expire_at.to_alipay_dict()
            else:
                params['expire_at'] = self.expire_at
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCampusSchoolcardSignModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'expire_at' in d:
            o.expire_at = d['expire_at']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'name' in d:
            o.name = d['name']
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'student_id' in d:
            o.student_id = d['student_id']
        return o


