#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalEnterprisesubsidyFailureTransferModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._cur_company_id = None
        self._father_company_id = None
        self._mdtrt_id = None
        self._name = None
        self._setl_id = None

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
    def cur_company_id(self):
        return self._cur_company_id

    @cur_company_id.setter
    def cur_company_id(self, value):
        self._cur_company_id = value
    @property
    def father_company_id(self):
        return self._father_company_id

    @father_company_id.setter
    def father_company_id(self, value):
        self._father_company_id = value
    @property
    def mdtrt_id(self):
        return self._mdtrt_id

    @mdtrt_id.setter
    def mdtrt_id(self, value):
        self._mdtrt_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def setl_id(self):
        return self._setl_id

    @setl_id.setter
    def setl_id(self, value):
        self._setl_id = value


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
        if self.cur_company_id:
            if hasattr(self.cur_company_id, 'to_alipay_dict'):
                params['cur_company_id'] = self.cur_company_id.to_alipay_dict()
            else:
                params['cur_company_id'] = self.cur_company_id
        if self.father_company_id:
            if hasattr(self.father_company_id, 'to_alipay_dict'):
                params['father_company_id'] = self.father_company_id.to_alipay_dict()
            else:
                params['father_company_id'] = self.father_company_id
        if self.mdtrt_id:
            if hasattr(self.mdtrt_id, 'to_alipay_dict'):
                params['mdtrt_id'] = self.mdtrt_id.to_alipay_dict()
            else:
                params['mdtrt_id'] = self.mdtrt_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.setl_id:
            if hasattr(self.setl_id, 'to_alipay_dict'):
                params['setl_id'] = self.setl_id.to_alipay_dict()
            else:
                params['setl_id'] = self.setl_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalEnterprisesubsidyFailureTransferModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'cur_company_id' in d:
            o.cur_company_id = d['cur_company_id']
        if 'father_company_id' in d:
            o.father_company_id = d['father_company_id']
        if 'mdtrt_id' in d:
            o.mdtrt_id = d['mdtrt_id']
        if 'name' in d:
            o.name = d['name']
        if 'setl_id' in d:
            o.setl_id = d['setl_id']
        return o


