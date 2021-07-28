#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractFileInfo import ContractFileInfo


class ContractInfo(object):

    def __init__(self):
        self._contract_amount = None
        self._contract_file_infos = None
        self._contract_name = None
        self._contract_no = None
        self._currency = None
        self._parse_participant_infos = None
        self._self_participant_infos = None

    @property
    def contract_amount(self):
        return self._contract_amount

    @contract_amount.setter
    def contract_amount(self, value):
        self._contract_amount = value
    @property
    def contract_file_infos(self):
        return self._contract_file_infos

    @contract_file_infos.setter
    def contract_file_infos(self, value):
        if isinstance(value, list):
            self._contract_file_infos = list()
            for i in value:
                if isinstance(i, ContractFileInfo):
                    self._contract_file_infos.append(i)
                else:
                    self._contract_file_infos.append(ContractFileInfo.from_alipay_dict(i))
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
    def parse_participant_infos(self):
        return self._parse_participant_infos

    @parse_participant_infos.setter
    def parse_participant_infos(self, value):
        if isinstance(value, list):
            self._parse_participant_infos = list()
            for i in value:
                self._parse_participant_infos.append(i)
    @property
    def self_participant_infos(self):
        return self._self_participant_infos

    @self_participant_infos.setter
    def self_participant_infos(self, value):
        if isinstance(value, list):
            self._self_participant_infos = list()
            for i in value:
                self._self_participant_infos.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.contract_amount:
            if hasattr(self.contract_amount, 'to_alipay_dict'):
                params['contract_amount'] = self.contract_amount.to_alipay_dict()
            else:
                params['contract_amount'] = self.contract_amount
        if self.contract_file_infos:
            if isinstance(self.contract_file_infos, list):
                for i in range(0, len(self.contract_file_infos)):
                    element = self.contract_file_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_file_infos[i] = element.to_alipay_dict()
            if hasattr(self.contract_file_infos, 'to_alipay_dict'):
                params['contract_file_infos'] = self.contract_file_infos.to_alipay_dict()
            else:
                params['contract_file_infos'] = self.contract_file_infos
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
        if self.parse_participant_infos:
            if isinstance(self.parse_participant_infos, list):
                for i in range(0, len(self.parse_participant_infos)):
                    element = self.parse_participant_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.parse_participant_infos[i] = element.to_alipay_dict()
            if hasattr(self.parse_participant_infos, 'to_alipay_dict'):
                params['parse_participant_infos'] = self.parse_participant_infos.to_alipay_dict()
            else:
                params['parse_participant_infos'] = self.parse_participant_infos
        if self.self_participant_infos:
            if isinstance(self.self_participant_infos, list):
                for i in range(0, len(self.self_participant_infos)):
                    element = self.self_participant_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.self_participant_infos[i] = element.to_alipay_dict()
            if hasattr(self.self_participant_infos, 'to_alipay_dict'):
                params['self_participant_infos'] = self.self_participant_infos.to_alipay_dict()
            else:
                params['self_participant_infos'] = self.self_participant_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractInfo()
        if 'contract_amount' in d:
            o.contract_amount = d['contract_amount']
        if 'contract_file_infos' in d:
            o.contract_file_infos = d['contract_file_infos']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'currency' in d:
            o.currency = d['currency']
        if 'parse_participant_infos' in d:
            o.parse_participant_infos = d['parse_participant_infos']
        if 'self_participant_infos' in d:
            o.self_participant_infos = d['self_participant_infos']
        return o


