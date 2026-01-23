#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrAddress import IndrAddress
from alipay.aop.api.domain.IndrAddress import IndrAddress
from alipay.aop.api.domain.IndrFileInfo import IndrFileInfo


class AlipayOverseasOpenIndraccountApplyModel(object):

    def __init__(self):
        self._account_abb_name = None
        self._account_address = None
        self._account_name = None
        self._account_type = None
        self._bank_address = None
        self._bank_name = None
        self._beneficiary_id = None
        self._currency = None
        self._file_list = None
        self._iban = None
        self._number = None
        self._remark = None
        self._scene_type = None
        self._sort_code = None
        self._swift_code = None
        self._websites = None

    @property
    def account_abb_name(self):
        return self._account_abb_name

    @account_abb_name.setter
    def account_abb_name(self, value):
        self._account_abb_name = value
    @property
    def account_address(self):
        return self._account_address

    @account_address.setter
    def account_address(self, value):
        if isinstance(value, IndrAddress):
            self._account_address = value
        else:
            self._account_address = IndrAddress.from_alipay_dict(value)
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def bank_address(self):
        return self._bank_address

    @bank_address.setter
    def bank_address(self, value):
        if isinstance(value, IndrAddress):
            self._bank_address = value
        else:
            self._bank_address = IndrAddress.from_alipay_dict(value)
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def beneficiary_id(self):
        return self._beneficiary_id

    @beneficiary_id.setter
    def beneficiary_id(self, value):
        self._beneficiary_id = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, IndrFileInfo):
                    self._file_list.append(i)
                else:
                    self._file_list.append(IndrFileInfo.from_alipay_dict(i))
    @property
    def iban(self):
        return self._iban

    @iban.setter
    def iban(self, value):
        self._iban = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def sort_code(self):
        return self._sort_code

    @sort_code.setter
    def sort_code(self, value):
        self._sort_code = value
    @property
    def swift_code(self):
        return self._swift_code

    @swift_code.setter
    def swift_code(self, value):
        self._swift_code = value
    @property
    def websites(self):
        return self._websites

    @websites.setter
    def websites(self, value):
        self._websites = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_abb_name:
            if hasattr(self.account_abb_name, 'to_alipay_dict'):
                params['account_abb_name'] = self.account_abb_name.to_alipay_dict()
            else:
                params['account_abb_name'] = self.account_abb_name
        if self.account_address:
            if hasattr(self.account_address, 'to_alipay_dict'):
                params['account_address'] = self.account_address.to_alipay_dict()
            else:
                params['account_address'] = self.account_address
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.bank_address:
            if hasattr(self.bank_address, 'to_alipay_dict'):
                params['bank_address'] = self.bank_address.to_alipay_dict()
            else:
                params['bank_address'] = self.bank_address
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.beneficiary_id:
            if hasattr(self.beneficiary_id, 'to_alipay_dict'):
                params['beneficiary_id'] = self.beneficiary_id.to_alipay_dict()
            else:
                params['beneficiary_id'] = self.beneficiary_id
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        if self.iban:
            if hasattr(self.iban, 'to_alipay_dict'):
                params['iban'] = self.iban.to_alipay_dict()
            else:
                params['iban'] = self.iban
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.sort_code:
            if hasattr(self.sort_code, 'to_alipay_dict'):
                params['sort_code'] = self.sort_code.to_alipay_dict()
            else:
                params['sort_code'] = self.sort_code
        if self.swift_code:
            if hasattr(self.swift_code, 'to_alipay_dict'):
                params['swift_code'] = self.swift_code.to_alipay_dict()
            else:
                params['swift_code'] = self.swift_code
        if self.websites:
            if hasattr(self.websites, 'to_alipay_dict'):
                params['websites'] = self.websites.to_alipay_dict()
            else:
                params['websites'] = self.websites
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenIndraccountApplyModel()
        if 'account_abb_name' in d:
            o.account_abb_name = d['account_abb_name']
        if 'account_address' in d:
            o.account_address = d['account_address']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'bank_address' in d:
            o.bank_address = d['bank_address']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'beneficiary_id' in d:
            o.beneficiary_id = d['beneficiary_id']
        if 'currency' in d:
            o.currency = d['currency']
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'iban' in d:
            o.iban = d['iban']
        if 'number' in d:
            o.number = d['number']
        if 'remark' in d:
            o.remark = d['remark']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'sort_code' in d:
            o.sort_code = d['sort_code']
        if 'swift_code' in d:
            o.swift_code = d['swift_code']
        if 'websites' in d:
            o.websites = d['websites']
        return o


