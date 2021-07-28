#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceCustomerCreateModel(object):

    def __init__(self):
        self._company_email = None
        self._company_name = None
        self._legal_person_cert_no = None
        self._legal_person_cert_type = None
        self._legal_person_name = None
        self._legal_person_phone_num = None
        self._org_code = None
        self._role_type = None
        self._user_cert_no = None
        self._user_cert_type = None
        self._user_person_name = None
        self._user_phone_num = None

    @property
    def company_email(self):
        return self._company_email

    @company_email.setter
    def company_email(self, value):
        self._company_email = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_cert_type(self):
        return self._legal_person_cert_type

    @legal_person_cert_type.setter
    def legal_person_cert_type(self, value):
        self._legal_person_cert_type = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def legal_person_phone_num(self):
        return self._legal_person_phone_num

    @legal_person_phone_num.setter
    def legal_person_phone_num(self, value):
        self._legal_person_phone_num = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        self._user_cert_no = value
    @property
    def user_cert_type(self):
        return self._user_cert_type

    @user_cert_type.setter
    def user_cert_type(self, value):
        self._user_cert_type = value
    @property
    def user_person_name(self):
        return self._user_person_name

    @user_person_name.setter
    def user_person_name(self, value):
        self._user_person_name = value
    @property
    def user_phone_num(self):
        return self._user_phone_num

    @user_phone_num.setter
    def user_phone_num(self, value):
        self._user_phone_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_email:
            if hasattr(self.company_email, 'to_alipay_dict'):
                params['company_email'] = self.company_email.to_alipay_dict()
            else:
                params['company_email'] = self.company_email
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.legal_person_cert_no:
            if hasattr(self.legal_person_cert_no, 'to_alipay_dict'):
                params['legal_person_cert_no'] = self.legal_person_cert_no.to_alipay_dict()
            else:
                params['legal_person_cert_no'] = self.legal_person_cert_no
        if self.legal_person_cert_type:
            if hasattr(self.legal_person_cert_type, 'to_alipay_dict'):
                params['legal_person_cert_type'] = self.legal_person_cert_type.to_alipay_dict()
            else:
                params['legal_person_cert_type'] = self.legal_person_cert_type
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.legal_person_phone_num:
            if hasattr(self.legal_person_phone_num, 'to_alipay_dict'):
                params['legal_person_phone_num'] = self.legal_person_phone_num.to_alipay_dict()
            else:
                params['legal_person_phone_num'] = self.legal_person_phone_num
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.user_cert_no:
            if hasattr(self.user_cert_no, 'to_alipay_dict'):
                params['user_cert_no'] = self.user_cert_no.to_alipay_dict()
            else:
                params['user_cert_no'] = self.user_cert_no
        if self.user_cert_type:
            if hasattr(self.user_cert_type, 'to_alipay_dict'):
                params['user_cert_type'] = self.user_cert_type.to_alipay_dict()
            else:
                params['user_cert_type'] = self.user_cert_type
        if self.user_person_name:
            if hasattr(self.user_person_name, 'to_alipay_dict'):
                params['user_person_name'] = self.user_person_name.to_alipay_dict()
            else:
                params['user_person_name'] = self.user_person_name
        if self.user_phone_num:
            if hasattr(self.user_phone_num, 'to_alipay_dict'):
                params['user_phone_num'] = self.user_phone_num.to_alipay_dict()
            else:
                params['user_phone_num'] = self.user_phone_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceCustomerCreateModel()
        if 'company_email' in d:
            o.company_email = d['company_email']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_cert_type' in d:
            o.legal_person_cert_type = d['legal_person_cert_type']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'legal_person_phone_num' in d:
            o.legal_person_phone_num = d['legal_person_phone_num']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'user_cert_no' in d:
            o.user_cert_no = d['user_cert_no']
        if 'user_cert_type' in d:
            o.user_cert_type = d['user_cert_type']
        if 'user_person_name' in d:
            o.user_person_name = d['user_person_name']
        if 'user_phone_num' in d:
            o.user_phone_num = d['user_phone_num']
        return o


