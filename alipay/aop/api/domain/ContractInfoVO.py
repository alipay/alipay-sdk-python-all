#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractApprovalInfoVO import ContractApprovalInfoVO


class ContractInfoVO(object):

    def __init__(self):
        self._approval_infos = None
        self._contract_amount = None
        self._contract_name = None
        self._contract_no = None
        self._currency = None
        self._stats_type = None

    @property
    def approval_infos(self):
        return self._approval_infos

    @approval_infos.setter
    def approval_infos(self, value):
        if isinstance(value, list):
            self._approval_infos = list()
            for i in value:
                if isinstance(i, ContractApprovalInfoVO):
                    self._approval_infos.append(i)
                else:
                    self._approval_infos.append(ContractApprovalInfoVO.from_alipay_dict(i))
    @property
    def contract_amount(self):
        return self._contract_amount

    @contract_amount.setter
    def contract_amount(self, value):
        self._contract_amount = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def stats_type(self):
        return self._stats_type

    @stats_type.setter
    def stats_type(self, value):
        self._stats_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.approval_infos:
            if isinstance(self.approval_infos, list):
                for i in range(0, len(self.approval_infos)):
                    element = self.approval_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.approval_infos[i] = element.to_alipay_dict()
            if hasattr(self.approval_infos, 'to_alipay_dict'):
                params['approval_infos'] = self.approval_infos.to_alipay_dict()
            else:
                params['approval_infos'] = self.approval_infos
        if self.contract_amount:
            if hasattr(self.contract_amount, 'to_alipay_dict'):
                params['contract_amount'] = self.contract_amount.to_alipay_dict()
            else:
                params['contract_amount'] = self.contract_amount
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.stats_type:
            if hasattr(self.stats_type, 'to_alipay_dict'):
                params['stats_type'] = self.stats_type.to_alipay_dict()
            else:
                params['stats_type'] = self.stats_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractInfoVO()
        if 'approval_infos' in d:
            o.approval_infos = d['approval_infos']
        if 'contract_amount' in d:
            o.contract_amount = d['contract_amount']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'currency' in d:
            o.currency = d['currency']
        if 'stats_type' in d:
            o.stats_type = d['stats_type']
        return o


