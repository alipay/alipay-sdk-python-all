#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EmployeeTitleInfoDTO(object):

    def __init__(self):
        self._address = None
        self._name = None
        self._open_bank_account = None
        self._open_bank_name = None
        self._tax_register_no = None
        self._telephone = None
        self._title_id = None
        self._title_tag = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_bank_account(self):
        return self._open_bank_account

    @open_bank_account.setter
    def open_bank_account(self, value):
        self._open_bank_account = value
    @property
    def open_bank_name(self):
        return self._open_bank_name

    @open_bank_name.setter
    def open_bank_name(self, value):
        self._open_bank_name = value
    @property
    def tax_register_no(self):
        return self._tax_register_no

    @tax_register_no.setter
    def tax_register_no(self, value):
        self._tax_register_no = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def title_id(self):
        return self._title_id

    @title_id.setter
    def title_id(self, value):
        self._title_id = value
    @property
    def title_tag(self):
        return self._title_tag

    @title_tag.setter
    def title_tag(self, value):
        self._title_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_bank_account:
            if hasattr(self.open_bank_account, 'to_alipay_dict'):
                params['open_bank_account'] = self.open_bank_account.to_alipay_dict()
            else:
                params['open_bank_account'] = self.open_bank_account
        if self.open_bank_name:
            if hasattr(self.open_bank_name, 'to_alipay_dict'):
                params['open_bank_name'] = self.open_bank_name.to_alipay_dict()
            else:
                params['open_bank_name'] = self.open_bank_name
        if self.tax_register_no:
            if hasattr(self.tax_register_no, 'to_alipay_dict'):
                params['tax_register_no'] = self.tax_register_no.to_alipay_dict()
            else:
                params['tax_register_no'] = self.tax_register_no
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.title_id:
            if hasattr(self.title_id, 'to_alipay_dict'):
                params['title_id'] = self.title_id.to_alipay_dict()
            else:
                params['title_id'] = self.title_id
        if self.title_tag:
            if hasattr(self.title_tag, 'to_alipay_dict'):
                params['title_tag'] = self.title_tag.to_alipay_dict()
            else:
                params['title_tag'] = self.title_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EmployeeTitleInfoDTO()
        if 'address' in d:
            o.address = d['address']
        if 'name' in d:
            o.name = d['name']
        if 'open_bank_account' in d:
            o.open_bank_account = d['open_bank_account']
        if 'open_bank_name' in d:
            o.open_bank_name = d['open_bank_name']
        if 'tax_register_no' in d:
            o.tax_register_no = d['tax_register_no']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'title_id' in d:
            o.title_id = d['title_id']
        if 'title_tag' in d:
            o.title_tag = d['title_tag']
        return o


