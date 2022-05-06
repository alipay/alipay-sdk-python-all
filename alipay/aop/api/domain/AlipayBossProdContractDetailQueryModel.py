#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdContractDetailQueryModel(object):

    def __init__(self):
        self._business_id = None
        self._contract_code = None
        self._is_pdf_required = None
        self._source_system_id = None
        self._tenant = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def is_pdf_required(self):
        return self._is_pdf_required

    @is_pdf_required.setter
    def is_pdf_required(self, value):
        self._is_pdf_required = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.is_pdf_required:
            if hasattr(self.is_pdf_required, 'to_alipay_dict'):
                params['is_pdf_required'] = self.is_pdf_required.to_alipay_dict()
            else:
                params['is_pdf_required'] = self.is_pdf_required
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdContractDetailQueryModel()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'is_pdf_required' in d:
            o.is_pdf_required = d['is_pdf_required']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


