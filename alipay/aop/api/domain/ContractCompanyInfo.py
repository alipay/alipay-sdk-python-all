#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractSignArea import ContractSignArea


class ContractCompanyInfo(object):

    def __init__(self):
        self._company_cert_no = None
        self._company_name = None
        self._legal_person_cert_no = None
        self._legal_person_name = None
        self._sign_area = None

    @property
    def company_cert_no(self):
        return self._company_cert_no

    @company_cert_no.setter
    def company_cert_no(self, value):
        self._company_cert_no = value
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
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def sign_area(self):
        return self._sign_area

    @sign_area.setter
    def sign_area(self, value):
        if isinstance(value, ContractSignArea):
            self._sign_area = value
        else:
            self._sign_area = ContractSignArea.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.company_cert_no:
            if hasattr(self.company_cert_no, 'to_alipay_dict'):
                params['company_cert_no'] = self.company_cert_no.to_alipay_dict()
            else:
                params['company_cert_no'] = self.company_cert_no
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
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.sign_area:
            if hasattr(self.sign_area, 'to_alipay_dict'):
                params['sign_area'] = self.sign_area.to_alipay_dict()
            else:
                params['sign_area'] = self.sign_area
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractCompanyInfo()
        if 'company_cert_no' in d:
            o.company_cert_no = d['company_cert_no']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'sign_area' in d:
            o.sign_area = d['sign_area']
        return o


