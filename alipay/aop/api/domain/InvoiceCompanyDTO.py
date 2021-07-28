#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceCompanyDTO(object):

    def __init__(self):
        self._area = None
        self._bank_account_id = None
        self._bank_name = None
        self._business_license_img = None
        self._city = None
        self._company_name = None
        self._company_type = None
        self._default_item_name = None
        self._default_tax_code = None
        self._default_tax_rate = None
        self._detailed_address = None
        self._ext_json = None
        self._invoice_disks = None
        self._invoice_phone = None
        self._payee_checker = None
        self._payee_operator = None
        self._payee_receiver = None
        self._payee_register_no = None
        self._province = None
        self._tax_token = None
        self._zero_tax_rate_flag = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def bank_account_id(self):
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, value):
        self._bank_account_id = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def business_license_img(self):
        return self._business_license_img

    @business_license_img.setter
    def business_license_img(self, value):
        self._business_license_img = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def default_item_name(self):
        return self._default_item_name

    @default_item_name.setter
    def default_item_name(self, value):
        self._default_item_name = value
    @property
    def default_tax_code(self):
        return self._default_tax_code

    @default_tax_code.setter
    def default_tax_code(self, value):
        self._default_tax_code = value
    @property
    def default_tax_rate(self):
        return self._default_tax_rate

    @default_tax_rate.setter
    def default_tax_rate(self, value):
        self._default_tax_rate = value
    @property
    def detailed_address(self):
        return self._detailed_address

    @detailed_address.setter
    def detailed_address(self, value):
        self._detailed_address = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def invoice_disks(self):
        return self._invoice_disks

    @invoice_disks.setter
    def invoice_disks(self, value):
        if isinstance(value, list):
            self._invoice_disks = list()
            for i in value:
                self._invoice_disks.append(i)
    @property
    def invoice_phone(self):
        return self._invoice_phone

    @invoice_phone.setter
    def invoice_phone(self, value):
        self._invoice_phone = value
    @property
    def payee_checker(self):
        return self._payee_checker

    @payee_checker.setter
    def payee_checker(self, value):
        self._payee_checker = value
    @property
    def payee_operator(self):
        return self._payee_operator

    @payee_operator.setter
    def payee_operator(self, value):
        self._payee_operator = value
    @property
    def payee_receiver(self):
        return self._payee_receiver

    @payee_receiver.setter
    def payee_receiver(self, value):
        self._payee_receiver = value
    @property
    def payee_register_no(self):
        return self._payee_register_no

    @payee_register_no.setter
    def payee_register_no(self, value):
        self._payee_register_no = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def tax_token(self):
        return self._tax_token

    @tax_token.setter
    def tax_token(self, value):
        self._tax_token = value
    @property
    def zero_tax_rate_flag(self):
        return self._zero_tax_rate_flag

    @zero_tax_rate_flag.setter
    def zero_tax_rate_flag(self, value):
        self._zero_tax_rate_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.bank_account_id:
            if hasattr(self.bank_account_id, 'to_alipay_dict'):
                params['bank_account_id'] = self.bank_account_id.to_alipay_dict()
            else:
                params['bank_account_id'] = self.bank_account_id
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.business_license_img:
            if hasattr(self.business_license_img, 'to_alipay_dict'):
                params['business_license_img'] = self.business_license_img.to_alipay_dict()
            else:
                params['business_license_img'] = self.business_license_img
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.default_item_name:
            if hasattr(self.default_item_name, 'to_alipay_dict'):
                params['default_item_name'] = self.default_item_name.to_alipay_dict()
            else:
                params['default_item_name'] = self.default_item_name
        if self.default_tax_code:
            if hasattr(self.default_tax_code, 'to_alipay_dict'):
                params['default_tax_code'] = self.default_tax_code.to_alipay_dict()
            else:
                params['default_tax_code'] = self.default_tax_code
        if self.default_tax_rate:
            if hasattr(self.default_tax_rate, 'to_alipay_dict'):
                params['default_tax_rate'] = self.default_tax_rate.to_alipay_dict()
            else:
                params['default_tax_rate'] = self.default_tax_rate
        if self.detailed_address:
            if hasattr(self.detailed_address, 'to_alipay_dict'):
                params['detailed_address'] = self.detailed_address.to_alipay_dict()
            else:
                params['detailed_address'] = self.detailed_address
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
        if self.invoice_disks:
            if isinstance(self.invoice_disks, list):
                for i in range(0, len(self.invoice_disks)):
                    element = self.invoice_disks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_disks[i] = element.to_alipay_dict()
            if hasattr(self.invoice_disks, 'to_alipay_dict'):
                params['invoice_disks'] = self.invoice_disks.to_alipay_dict()
            else:
                params['invoice_disks'] = self.invoice_disks
        if self.invoice_phone:
            if hasattr(self.invoice_phone, 'to_alipay_dict'):
                params['invoice_phone'] = self.invoice_phone.to_alipay_dict()
            else:
                params['invoice_phone'] = self.invoice_phone
        if self.payee_checker:
            if hasattr(self.payee_checker, 'to_alipay_dict'):
                params['payee_checker'] = self.payee_checker.to_alipay_dict()
            else:
                params['payee_checker'] = self.payee_checker
        if self.payee_operator:
            if hasattr(self.payee_operator, 'to_alipay_dict'):
                params['payee_operator'] = self.payee_operator.to_alipay_dict()
            else:
                params['payee_operator'] = self.payee_operator
        if self.payee_receiver:
            if hasattr(self.payee_receiver, 'to_alipay_dict'):
                params['payee_receiver'] = self.payee_receiver.to_alipay_dict()
            else:
                params['payee_receiver'] = self.payee_receiver
        if self.payee_register_no:
            if hasattr(self.payee_register_no, 'to_alipay_dict'):
                params['payee_register_no'] = self.payee_register_no.to_alipay_dict()
            else:
                params['payee_register_no'] = self.payee_register_no
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.tax_token:
            if hasattr(self.tax_token, 'to_alipay_dict'):
                params['tax_token'] = self.tax_token.to_alipay_dict()
            else:
                params['tax_token'] = self.tax_token
        if self.zero_tax_rate_flag:
            if hasattr(self.zero_tax_rate_flag, 'to_alipay_dict'):
                params['zero_tax_rate_flag'] = self.zero_tax_rate_flag.to_alipay_dict()
            else:
                params['zero_tax_rate_flag'] = self.zero_tax_rate_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceCompanyDTO()
        if 'area' in d:
            o.area = d['area']
        if 'bank_account_id' in d:
            o.bank_account_id = d['bank_account_id']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'business_license_img' in d:
            o.business_license_img = d['business_license_img']
        if 'city' in d:
            o.city = d['city']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'default_item_name' in d:
            o.default_item_name = d['default_item_name']
        if 'default_tax_code' in d:
            o.default_tax_code = d['default_tax_code']
        if 'default_tax_rate' in d:
            o.default_tax_rate = d['default_tax_rate']
        if 'detailed_address' in d:
            o.detailed_address = d['detailed_address']
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'invoice_disks' in d:
            o.invoice_disks = d['invoice_disks']
        if 'invoice_phone' in d:
            o.invoice_phone = d['invoice_phone']
        if 'payee_checker' in d:
            o.payee_checker = d['payee_checker']
        if 'payee_operator' in d:
            o.payee_operator = d['payee_operator']
        if 'payee_receiver' in d:
            o.payee_receiver = d['payee_receiver']
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'province' in d:
            o.province = d['province']
        if 'tax_token' in d:
            o.tax_token = d['tax_token']
        if 'zero_tax_rate_flag' in d:
            o.zero_tax_rate_flag = d['zero_tax_rate_flag']
        return o


