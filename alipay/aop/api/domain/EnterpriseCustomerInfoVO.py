#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterpriseCustomerInfoVO(object):

    def __init__(self):
        self._cert_name = None
        self._enterprise_addr = None
        self._enterprise_bank_name = None
        self._enterprise_bank_no = None
        self._legal_cert_no = None
        self._legal_mobile_phone = None
        self._legal_name = None
        self._unified_social_cert_code = None

    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def enterprise_addr(self):
        return self._enterprise_addr

    @enterprise_addr.setter
    def enterprise_addr(self, value):
        self._enterprise_addr = value
    @property
    def enterprise_bank_name(self):
        return self._enterprise_bank_name

    @enterprise_bank_name.setter
    def enterprise_bank_name(self, value):
        self._enterprise_bank_name = value
    @property
    def enterprise_bank_no(self):
        return self._enterprise_bank_no

    @enterprise_bank_no.setter
    def enterprise_bank_no(self, value):
        self._enterprise_bank_no = value
    @property
    def legal_cert_no(self):
        return self._legal_cert_no

    @legal_cert_no.setter
    def legal_cert_no(self, value):
        self._legal_cert_no = value
    @property
    def legal_mobile_phone(self):
        return self._legal_mobile_phone

    @legal_mobile_phone.setter
    def legal_mobile_phone(self, value):
        self._legal_mobile_phone = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
    @property
    def unified_social_cert_code(self):
        return self._unified_social_cert_code

    @unified_social_cert_code.setter
    def unified_social_cert_code(self, value):
        self._unified_social_cert_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.enterprise_addr:
            if hasattr(self.enterprise_addr, 'to_alipay_dict'):
                params['enterprise_addr'] = self.enterprise_addr.to_alipay_dict()
            else:
                params['enterprise_addr'] = self.enterprise_addr
        if self.enterprise_bank_name:
            if hasattr(self.enterprise_bank_name, 'to_alipay_dict'):
                params['enterprise_bank_name'] = self.enterprise_bank_name.to_alipay_dict()
            else:
                params['enterprise_bank_name'] = self.enterprise_bank_name
        if self.enterprise_bank_no:
            if hasattr(self.enterprise_bank_no, 'to_alipay_dict'):
                params['enterprise_bank_no'] = self.enterprise_bank_no.to_alipay_dict()
            else:
                params['enterprise_bank_no'] = self.enterprise_bank_no
        if self.legal_cert_no:
            if hasattr(self.legal_cert_no, 'to_alipay_dict'):
                params['legal_cert_no'] = self.legal_cert_no.to_alipay_dict()
            else:
                params['legal_cert_no'] = self.legal_cert_no
        if self.legal_mobile_phone:
            if hasattr(self.legal_mobile_phone, 'to_alipay_dict'):
                params['legal_mobile_phone'] = self.legal_mobile_phone.to_alipay_dict()
            else:
                params['legal_mobile_phone'] = self.legal_mobile_phone
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = self.legal_name.to_alipay_dict()
            else:
                params['legal_name'] = self.legal_name
        if self.unified_social_cert_code:
            if hasattr(self.unified_social_cert_code, 'to_alipay_dict'):
                params['unified_social_cert_code'] = self.unified_social_cert_code.to_alipay_dict()
            else:
                params['unified_social_cert_code'] = self.unified_social_cert_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriseCustomerInfoVO()
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'enterprise_addr' in d:
            o.enterprise_addr = d['enterprise_addr']
        if 'enterprise_bank_name' in d:
            o.enterprise_bank_name = d['enterprise_bank_name']
        if 'enterprise_bank_no' in d:
            o.enterprise_bank_no = d['enterprise_bank_no']
        if 'legal_cert_no' in d:
            o.legal_cert_no = d['legal_cert_no']
        if 'legal_mobile_phone' in d:
            o.legal_mobile_phone = d['legal_mobile_phone']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'unified_social_cert_code' in d:
            o.unified_social_cert_code = d['unified_social_cert_code']
        return o


