#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstitutionVO import InstitutionVO


class AgreementView(object):

    def __init__(self):
        self._agreement_status = None
        self._agreement_version = None
        self._code = None
        self._content = None
        self._content_type = None
        self._contract_no = None
        self._force_read = None
        self._fund_supplier = None
        self._mandatory_reading_time = None
        self._name = None

    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
    @property
    def agreement_version(self):
        return self._agreement_version

    @agreement_version.setter
    def agreement_version(self, value):
        self._agreement_version = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def force_read(self):
        return self._force_read

    @force_read.setter
    def force_read(self, value):
        self._force_read = value
    @property
    def fund_supplier(self):
        return self._fund_supplier

    @fund_supplier.setter
    def fund_supplier(self, value):
        if isinstance(value, InstitutionVO):
            self._fund_supplier = value
        else:
            self._fund_supplier = InstitutionVO.from_alipay_dict(value)
    @property
    def mandatory_reading_time(self):
        return self._mandatory_reading_time

    @mandatory_reading_time.setter
    def mandatory_reading_time(self, value):
        self._mandatory_reading_time = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_status:
            if hasattr(self.agreement_status, 'to_alipay_dict'):
                params['agreement_status'] = self.agreement_status.to_alipay_dict()
            else:
                params['agreement_status'] = self.agreement_status
        if self.agreement_version:
            if hasattr(self.agreement_version, 'to_alipay_dict'):
                params['agreement_version'] = self.agreement_version.to_alipay_dict()
            else:
                params['agreement_version'] = self.agreement_version
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.force_read:
            if hasattr(self.force_read, 'to_alipay_dict'):
                params['force_read'] = self.force_read.to_alipay_dict()
            else:
                params['force_read'] = self.force_read
        if self.fund_supplier:
            if hasattr(self.fund_supplier, 'to_alipay_dict'):
                params['fund_supplier'] = self.fund_supplier.to_alipay_dict()
            else:
                params['fund_supplier'] = self.fund_supplier
        if self.mandatory_reading_time:
            if hasattr(self.mandatory_reading_time, 'to_alipay_dict'):
                params['mandatory_reading_time'] = self.mandatory_reading_time.to_alipay_dict()
            else:
                params['mandatory_reading_time'] = self.mandatory_reading_time
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgreementView()
        if 'agreement_status' in d:
            o.agreement_status = d['agreement_status']
        if 'agreement_version' in d:
            o.agreement_version = d['agreement_version']
        if 'code' in d:
            o.code = d['code']
        if 'content' in d:
            o.content = d['content']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'force_read' in d:
            o.force_read = d['force_read']
        if 'fund_supplier' in d:
            o.fund_supplier = d['fund_supplier']
        if 'mandatory_reading_time' in d:
            o.mandatory_reading_time = d['mandatory_reading_time']
        if 'name' in d:
            o.name = d['name']
        return o


