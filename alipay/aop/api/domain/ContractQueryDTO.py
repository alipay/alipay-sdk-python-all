#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractAttachDTO import ContractAttachDTO
from alipay.aop.api.domain.ContractAttachDTO import ContractAttachDTO


class ContractQueryDTO(object):

    def __init__(self):
        self._bussiness_number = None
        self._contract_attaches = None
        self._contract_code = None
        self._contract_doc = None
        self._contract_name = None
        self._imprint_id = None
        self._source_system_id = None
        self._status = None
        self._tenant = None

    @property
    def bussiness_number(self):
        return self._bussiness_number

    @bussiness_number.setter
    def bussiness_number(self, value):
        self._bussiness_number = value
    @property
    def contract_attaches(self):
        return self._contract_attaches

    @contract_attaches.setter
    def contract_attaches(self, value):
        if isinstance(value, list):
            self._contract_attaches = list()
            for i in value:
                if isinstance(i, ContractAttachDTO):
                    self._contract_attaches.append(i)
                else:
                    self._contract_attaches.append(ContractAttachDTO.from_alipay_dict(i))
    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def contract_doc(self):
        return self._contract_doc

    @contract_doc.setter
    def contract_doc(self, value):
        if isinstance(value, ContractAttachDTO):
            self._contract_doc = value
        else:
            self._contract_doc = ContractAttachDTO.from_alipay_dict(value)
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def imprint_id(self):
        return self._imprint_id

    @imprint_id.setter
    def imprint_id(self, value):
        self._imprint_id = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.bussiness_number:
            if hasattr(self.bussiness_number, 'to_alipay_dict'):
                params['bussiness_number'] = self.bussiness_number.to_alipay_dict()
            else:
                params['bussiness_number'] = self.bussiness_number
        if self.contract_attaches:
            if isinstance(self.contract_attaches, list):
                for i in range(0, len(self.contract_attaches)):
                    element = self.contract_attaches[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_attaches[i] = element.to_alipay_dict()
            if hasattr(self.contract_attaches, 'to_alipay_dict'):
                params['contract_attaches'] = self.contract_attaches.to_alipay_dict()
            else:
                params['contract_attaches'] = self.contract_attaches
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.contract_doc:
            if hasattr(self.contract_doc, 'to_alipay_dict'):
                params['contract_doc'] = self.contract_doc.to_alipay_dict()
            else:
                params['contract_doc'] = self.contract_doc
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.imprint_id:
            if hasattr(self.imprint_id, 'to_alipay_dict'):
                params['imprint_id'] = self.imprint_id.to_alipay_dict()
            else:
                params['imprint_id'] = self.imprint_id
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = ContractQueryDTO()
        if 'bussiness_number' in d:
            o.bussiness_number = d['bussiness_number']
        if 'contract_attaches' in d:
            o.contract_attaches = d['contract_attaches']
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'contract_doc' in d:
            o.contract_doc = d['contract_doc']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'imprint_id' in d:
            o.imprint_id = d['imprint_id']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'status' in d:
            o.status = d['status']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


