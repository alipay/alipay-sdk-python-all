#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryRentSignSyncModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._enterprise_credit_no = None
        self._enterprise_name = None
        self._enterprise_no = None
        self._enterprise_proof = None
        self._org_code = None
        self._rent_sign_status = None
        self._rent_sign_type = None
        self._request_party = None
        self._user_name = None
        self._user_record_no = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def enterprise_credit_no(self):
        return self._enterprise_credit_no

    @enterprise_credit_no.setter
    def enterprise_credit_no(self, value):
        self._enterprise_credit_no = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def enterprise_no(self):
        return self._enterprise_no

    @enterprise_no.setter
    def enterprise_no(self, value):
        self._enterprise_no = value
    @property
    def enterprise_proof(self):
        return self._enterprise_proof

    @enterprise_proof.setter
    def enterprise_proof(self, value):
        self._enterprise_proof = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def rent_sign_status(self):
        return self._rent_sign_status

    @rent_sign_status.setter
    def rent_sign_status(self, value):
        self._rent_sign_status = value
    @property
    def rent_sign_type(self):
        return self._rent_sign_type

    @rent_sign_type.setter
    def rent_sign_type(self, value):
        self._rent_sign_type = value
    @property
    def request_party(self):
        return self._request_party

    @request_party.setter
    def request_party(self, value):
        self._request_party = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_record_no(self):
        return self._user_record_no

    @user_record_no.setter
    def user_record_no(self, value):
        self._user_record_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.enterprise_credit_no:
            if hasattr(self.enterprise_credit_no, 'to_alipay_dict'):
                params['enterprise_credit_no'] = self.enterprise_credit_no.to_alipay_dict()
            else:
                params['enterprise_credit_no'] = self.enterprise_credit_no
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.enterprise_no:
            if hasattr(self.enterprise_no, 'to_alipay_dict'):
                params['enterprise_no'] = self.enterprise_no.to_alipay_dict()
            else:
                params['enterprise_no'] = self.enterprise_no
        if self.enterprise_proof:
            if hasattr(self.enterprise_proof, 'to_alipay_dict'):
                params['enterprise_proof'] = self.enterprise_proof.to_alipay_dict()
            else:
                params['enterprise_proof'] = self.enterprise_proof
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.rent_sign_status:
            if hasattr(self.rent_sign_status, 'to_alipay_dict'):
                params['rent_sign_status'] = self.rent_sign_status.to_alipay_dict()
            else:
                params['rent_sign_status'] = self.rent_sign_status
        if self.rent_sign_type:
            if hasattr(self.rent_sign_type, 'to_alipay_dict'):
                params['rent_sign_type'] = self.rent_sign_type.to_alipay_dict()
            else:
                params['rent_sign_type'] = self.rent_sign_type
        if self.request_party:
            if hasattr(self.request_party, 'to_alipay_dict'):
                params['request_party'] = self.request_party.to_alipay_dict()
            else:
                params['request_party'] = self.request_party
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_record_no:
            if hasattr(self.user_record_no, 'to_alipay_dict'):
                params['user_record_no'] = self.user_record_no.to_alipay_dict()
            else:
                params['user_record_no'] = self.user_record_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryRentSignSyncModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'enterprise_credit_no' in d:
            o.enterprise_credit_no = d['enterprise_credit_no']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'enterprise_no' in d:
            o.enterprise_no = d['enterprise_no']
        if 'enterprise_proof' in d:
            o.enterprise_proof = d['enterprise_proof']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'rent_sign_status' in d:
            o.rent_sign_status = d['rent_sign_status']
        if 'rent_sign_type' in d:
            o.rent_sign_type = d['rent_sign_type']
        if 'request_party' in d:
            o.request_party = d['request_party']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_record_no' in d:
            o.user_record_no = d['user_record_no']
        return o


