#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DefiCustCompanyDTO(object):

    def __init__(self):
        self._company_cert_no = None
        self._company_cert_type = None
        self._company_name = None
        self._legal_person_cert_no = None
        self._legal_person_cert_type = None
        self._legal_person_name = None

    @property
    def company_cert_no(self):
        return self._company_cert_no

    @company_cert_no.setter
    def company_cert_no(self, value):
        self._company_cert_no = value
    @property
    def company_cert_type(self):
        return self._company_cert_type

    @company_cert_type.setter
    def company_cert_type(self, value):
        self._company_cert_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.company_cert_no:
            if hasattr(self.company_cert_no, 'to_alipay_dict'):
                params['company_cert_no'] = self.company_cert_no.to_alipay_dict()
            else:
                params['company_cert_no'] = self.company_cert_no
        if self.company_cert_type:
            if hasattr(self.company_cert_type, 'to_alipay_dict'):
                params['company_cert_type'] = self.company_cert_type.to_alipay_dict()
            else:
                params['company_cert_type'] = self.company_cert_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DefiCustCompanyDTO()
        if 'company_cert_no' in d:
            o.company_cert_no = d['company_cert_no']
        if 'company_cert_type' in d:
            o.company_cert_type = d['company_cert_type']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_cert_type' in d:
            o.legal_person_cert_type = d['legal_person_cert_type']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        return o


