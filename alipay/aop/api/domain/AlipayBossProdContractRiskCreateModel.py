#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Attach import Attach
from alipay.aop.api.domain.People import People
from alipay.aop.api.domain.RiskPartnerDTO import RiskPartnerDTO
from alipay.aop.api.domain.RiskPartnerDTO import RiskPartnerDTO


class AlipayBossProdContractRiskCreateModel(object):

    def __init__(self):
        self._attach = None
        self._business_id = None
        self._business_line = None
        self._file_url = None
        self._invoice_type_list = None
        self._operator = None
        self._payment_account_list = None
        self._risk_partner_a_list = None
        self._risk_partner_b_list = None
        self._risk_types = None
        self._source_system_id = None
        self._tenant = None

    @property
    def attach(self):
        return self._attach

    @attach.setter
    def attach(self, value):
        if isinstance(value, Attach):
            self._attach = value
        else:
            self._attach = Attach.from_alipay_dict(value)
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def business_line(self):
        return self._business_line

    @business_line.setter
    def business_line(self, value):
        self._business_line = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def invoice_type_list(self):
        return self._invoice_type_list

    @invoice_type_list.setter
    def invoice_type_list(self, value):
        if isinstance(value, list):
            self._invoice_type_list = list()
            for i in value:
                self._invoice_type_list.append(i)
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        if isinstance(value, People):
            self._operator = value
        else:
            self._operator = People.from_alipay_dict(value)
    @property
    def payment_account_list(self):
        return self._payment_account_list

    @payment_account_list.setter
    def payment_account_list(self, value):
        if isinstance(value, list):
            self._payment_account_list = list()
            for i in value:
                self._payment_account_list.append(i)
    @property
    def risk_partner_a_list(self):
        return self._risk_partner_a_list

    @risk_partner_a_list.setter
    def risk_partner_a_list(self, value):
        if isinstance(value, list):
            self._risk_partner_a_list = list()
            for i in value:
                if isinstance(i, RiskPartnerDTO):
                    self._risk_partner_a_list.append(i)
                else:
                    self._risk_partner_a_list.append(RiskPartnerDTO.from_alipay_dict(i))
    @property
    def risk_partner_b_list(self):
        return self._risk_partner_b_list

    @risk_partner_b_list.setter
    def risk_partner_b_list(self, value):
        if isinstance(value, list):
            self._risk_partner_b_list = list()
            for i in value:
                if isinstance(i, RiskPartnerDTO):
                    self._risk_partner_b_list.append(i)
                else:
                    self._risk_partner_b_list.append(RiskPartnerDTO.from_alipay_dict(i))
    @property
    def risk_types(self):
        return self._risk_types

    @risk_types.setter
    def risk_types(self, value):
        if isinstance(value, list):
            self._risk_types = list()
            for i in value:
                self._risk_types.append(i)
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
        if self.attach:
            if hasattr(self.attach, 'to_alipay_dict'):
                params['attach'] = self.attach.to_alipay_dict()
            else:
                params['attach'] = self.attach
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.business_line:
            if hasattr(self.business_line, 'to_alipay_dict'):
                params['business_line'] = self.business_line.to_alipay_dict()
            else:
                params['business_line'] = self.business_line
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.invoice_type_list:
            if isinstance(self.invoice_type_list, list):
                for i in range(0, len(self.invoice_type_list)):
                    element = self.invoice_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_type_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_type_list, 'to_alipay_dict'):
                params['invoice_type_list'] = self.invoice_type_list.to_alipay_dict()
            else:
                params['invoice_type_list'] = self.invoice_type_list
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.payment_account_list:
            if isinstance(self.payment_account_list, list):
                for i in range(0, len(self.payment_account_list)):
                    element = self.payment_account_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_account_list[i] = element.to_alipay_dict()
            if hasattr(self.payment_account_list, 'to_alipay_dict'):
                params['payment_account_list'] = self.payment_account_list.to_alipay_dict()
            else:
                params['payment_account_list'] = self.payment_account_list
        if self.risk_partner_a_list:
            if isinstance(self.risk_partner_a_list, list):
                for i in range(0, len(self.risk_partner_a_list)):
                    element = self.risk_partner_a_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_partner_a_list[i] = element.to_alipay_dict()
            if hasattr(self.risk_partner_a_list, 'to_alipay_dict'):
                params['risk_partner_a_list'] = self.risk_partner_a_list.to_alipay_dict()
            else:
                params['risk_partner_a_list'] = self.risk_partner_a_list
        if self.risk_partner_b_list:
            if isinstance(self.risk_partner_b_list, list):
                for i in range(0, len(self.risk_partner_b_list)):
                    element = self.risk_partner_b_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_partner_b_list[i] = element.to_alipay_dict()
            if hasattr(self.risk_partner_b_list, 'to_alipay_dict'):
                params['risk_partner_b_list'] = self.risk_partner_b_list.to_alipay_dict()
            else:
                params['risk_partner_b_list'] = self.risk_partner_b_list
        if self.risk_types:
            if isinstance(self.risk_types, list):
                for i in range(0, len(self.risk_types)):
                    element = self.risk_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_types[i] = element.to_alipay_dict()
            if hasattr(self.risk_types, 'to_alipay_dict'):
                params['risk_types'] = self.risk_types.to_alipay_dict()
            else:
                params['risk_types'] = self.risk_types
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
        o = AlipayBossProdContractRiskCreateModel()
        if 'attach' in d:
            o.attach = d['attach']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'business_line' in d:
            o.business_line = d['business_line']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'invoice_type_list' in d:
            o.invoice_type_list = d['invoice_type_list']
        if 'operator' in d:
            o.operator = d['operator']
        if 'payment_account_list' in d:
            o.payment_account_list = d['payment_account_list']
        if 'risk_partner_a_list' in d:
            o.risk_partner_a_list = d['risk_partner_a_list']
        if 'risk_partner_b_list' in d:
            o.risk_partner_b_list = d['risk_partner_b_list']
        if 'risk_types' in d:
            o.risk_types = d['risk_types']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


