#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceBuyerInfo(object):

    def __init__(self):
        self._buyer_address = None
        self._buyer_bank = None
        self._buyer_bank_account = None
        self._buyer_name = None
        self._buyer_personal_id_number = None
        self._buyer_personal_id_type = None
        self._buyer_personal_name_flag = None
        self._buyer_personal_nationality_code = None
        self._buyer_phone = None
        self._buyer_tax_no = None

    @property
    def buyer_address(self):
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, value):
        self._buyer_address = value
    @property
    def buyer_bank(self):
        return self._buyer_bank

    @buyer_bank.setter
    def buyer_bank(self, value):
        self._buyer_bank = value
    @property
    def buyer_bank_account(self):
        return self._buyer_bank_account

    @buyer_bank_account.setter
    def buyer_bank_account(self, value):
        self._buyer_bank_account = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_personal_id_number(self):
        return self._buyer_personal_id_number

    @buyer_personal_id_number.setter
    def buyer_personal_id_number(self, value):
        self._buyer_personal_id_number = value
    @property
    def buyer_personal_id_type(self):
        return self._buyer_personal_id_type

    @buyer_personal_id_type.setter
    def buyer_personal_id_type(self, value):
        self._buyer_personal_id_type = value
    @property
    def buyer_personal_name_flag(self):
        return self._buyer_personal_name_flag

    @buyer_personal_name_flag.setter
    def buyer_personal_name_flag(self, value):
        self._buyer_personal_name_flag = value
    @property
    def buyer_personal_nationality_code(self):
        return self._buyer_personal_nationality_code

    @buyer_personal_nationality_code.setter
    def buyer_personal_nationality_code(self, value):
        self._buyer_personal_nationality_code = value
    @property
    def buyer_phone(self):
        return self._buyer_phone

    @buyer_phone.setter
    def buyer_phone(self, value):
        self._buyer_phone = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_address:
            if hasattr(self.buyer_address, 'to_alipay_dict'):
                params['buyer_address'] = self.buyer_address.to_alipay_dict()
            else:
                params['buyer_address'] = self.buyer_address
        if self.buyer_bank:
            if hasattr(self.buyer_bank, 'to_alipay_dict'):
                params['buyer_bank'] = self.buyer_bank.to_alipay_dict()
            else:
                params['buyer_bank'] = self.buyer_bank
        if self.buyer_bank_account:
            if hasattr(self.buyer_bank_account, 'to_alipay_dict'):
                params['buyer_bank_account'] = self.buyer_bank_account.to_alipay_dict()
            else:
                params['buyer_bank_account'] = self.buyer_bank_account
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.buyer_personal_id_number:
            if hasattr(self.buyer_personal_id_number, 'to_alipay_dict'):
                params['buyer_personal_id_number'] = self.buyer_personal_id_number.to_alipay_dict()
            else:
                params['buyer_personal_id_number'] = self.buyer_personal_id_number
        if self.buyer_personal_id_type:
            if hasattr(self.buyer_personal_id_type, 'to_alipay_dict'):
                params['buyer_personal_id_type'] = self.buyer_personal_id_type.to_alipay_dict()
            else:
                params['buyer_personal_id_type'] = self.buyer_personal_id_type
        if self.buyer_personal_name_flag:
            if hasattr(self.buyer_personal_name_flag, 'to_alipay_dict'):
                params['buyer_personal_name_flag'] = self.buyer_personal_name_flag.to_alipay_dict()
            else:
                params['buyer_personal_name_flag'] = self.buyer_personal_name_flag
        if self.buyer_personal_nationality_code:
            if hasattr(self.buyer_personal_nationality_code, 'to_alipay_dict'):
                params['buyer_personal_nationality_code'] = self.buyer_personal_nationality_code.to_alipay_dict()
            else:
                params['buyer_personal_nationality_code'] = self.buyer_personal_nationality_code
        if self.buyer_phone:
            if hasattr(self.buyer_phone, 'to_alipay_dict'):
                params['buyer_phone'] = self.buyer_phone.to_alipay_dict()
            else:
                params['buyer_phone'] = self.buyer_phone
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceBuyerInfo()
        if 'buyer_address' in d:
            o.buyer_address = d['buyer_address']
        if 'buyer_bank' in d:
            o.buyer_bank = d['buyer_bank']
        if 'buyer_bank_account' in d:
            o.buyer_bank_account = d['buyer_bank_account']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'buyer_personal_id_number' in d:
            o.buyer_personal_id_number = d['buyer_personal_id_number']
        if 'buyer_personal_id_type' in d:
            o.buyer_personal_id_type = d['buyer_personal_id_type']
        if 'buyer_personal_name_flag' in d:
            o.buyer_personal_name_flag = d['buyer_personal_name_flag']
        if 'buyer_personal_nationality_code' in d:
            o.buyer_personal_nationality_code = d['buyer_personal_nationality_code']
        if 'buyer_phone' in d:
            o.buyer_phone = d['buyer_phone']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        return o


