#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyInformation(object):

    def __init__(self):
        self._business_category_code = None
        self._company_cert_effective_date = None
        self._company_cert_expiration_date = None
        self._company_cert_no = None
        self._company_cert_type = None
        self._company_english_name = None
        self._company_name = None
        self._company_registered_address = None
        self._company_registered_capital_amount = None
        self._company_registered_capital_amount_currency = None
        self._company_registered_country = None
        self._company_size = None
        self._economic_category_code = None

    @property
    def business_category_code(self):
        return self._business_category_code

    @business_category_code.setter
    def business_category_code(self, value):
        self._business_category_code = value
    @property
    def company_cert_effective_date(self):
        return self._company_cert_effective_date

    @company_cert_effective_date.setter
    def company_cert_effective_date(self, value):
        self._company_cert_effective_date = value
    @property
    def company_cert_expiration_date(self):
        return self._company_cert_expiration_date

    @company_cert_expiration_date.setter
    def company_cert_expiration_date(self, value):
        self._company_cert_expiration_date = value
    @property
    def company_cert_no(self):
        return self._company_cert_no

    @company_cert_no.setter
    def company_cert_no(self, value):
        self._company_cert_no = value
    @property
    def company_cert_type(self):
        return self._company_cert_type

    @company_cert_type.setter
    def company_cert_type(self, value):
        self._company_cert_type = value
    @property
    def company_english_name(self):
        return self._company_english_name

    @company_english_name.setter
    def company_english_name(self, value):
        self._company_english_name = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_registered_address(self):
        return self._company_registered_address

    @company_registered_address.setter
    def company_registered_address(self, value):
        self._company_registered_address = value
    @property
    def company_registered_capital_amount(self):
        return self._company_registered_capital_amount

    @company_registered_capital_amount.setter
    def company_registered_capital_amount(self, value):
        self._company_registered_capital_amount = value
    @property
    def company_registered_capital_amount_currency(self):
        return self._company_registered_capital_amount_currency

    @company_registered_capital_amount_currency.setter
    def company_registered_capital_amount_currency(self, value):
        self._company_registered_capital_amount_currency = value
    @property
    def company_registered_country(self):
        return self._company_registered_country

    @company_registered_country.setter
    def company_registered_country(self, value):
        self._company_registered_country = value
    @property
    def company_size(self):
        return self._company_size

    @company_size.setter
    def company_size(self, value):
        self._company_size = value
    @property
    def economic_category_code(self):
        return self._economic_category_code

    @economic_category_code.setter
    def economic_category_code(self, value):
        self._economic_category_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_category_code:
            if hasattr(self.business_category_code, 'to_alipay_dict'):
                params['business_category_code'] = self.business_category_code.to_alipay_dict()
            else:
                params['business_category_code'] = self.business_category_code
        if self.company_cert_effective_date:
            if hasattr(self.company_cert_effective_date, 'to_alipay_dict'):
                params['company_cert_effective_date'] = self.company_cert_effective_date.to_alipay_dict()
            else:
                params['company_cert_effective_date'] = self.company_cert_effective_date
        if self.company_cert_expiration_date:
            if hasattr(self.company_cert_expiration_date, 'to_alipay_dict'):
                params['company_cert_expiration_date'] = self.company_cert_expiration_date.to_alipay_dict()
            else:
                params['company_cert_expiration_date'] = self.company_cert_expiration_date
        if self.company_cert_no:
            if hasattr(self.company_cert_no, 'to_alipay_dict'):
                params['company_cert_no'] = self.company_cert_no.to_alipay_dict()
            else:
                params['company_cert_no'] = self.company_cert_no
        if self.company_cert_type:
            if hasattr(self.company_cert_type, 'to_alipay_dict'):
                params['company_cert_type'] = self.company_cert_type.to_alipay_dict()
            else:
                params['company_cert_type'] = self.company_cert_type
        if self.company_english_name:
            if hasattr(self.company_english_name, 'to_alipay_dict'):
                params['company_english_name'] = self.company_english_name.to_alipay_dict()
            else:
                params['company_english_name'] = self.company_english_name
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.company_registered_address:
            if hasattr(self.company_registered_address, 'to_alipay_dict'):
                params['company_registered_address'] = self.company_registered_address.to_alipay_dict()
            else:
                params['company_registered_address'] = self.company_registered_address
        if self.company_registered_capital_amount:
            if hasattr(self.company_registered_capital_amount, 'to_alipay_dict'):
                params['company_registered_capital_amount'] = self.company_registered_capital_amount.to_alipay_dict()
            else:
                params['company_registered_capital_amount'] = self.company_registered_capital_amount
        if self.company_registered_capital_amount_currency:
            if hasattr(self.company_registered_capital_amount_currency, 'to_alipay_dict'):
                params['company_registered_capital_amount_currency'] = self.company_registered_capital_amount_currency.to_alipay_dict()
            else:
                params['company_registered_capital_amount_currency'] = self.company_registered_capital_amount_currency
        if self.company_registered_country:
            if hasattr(self.company_registered_country, 'to_alipay_dict'):
                params['company_registered_country'] = self.company_registered_country.to_alipay_dict()
            else:
                params['company_registered_country'] = self.company_registered_country
        if self.company_size:
            if hasattr(self.company_size, 'to_alipay_dict'):
                params['company_size'] = self.company_size.to_alipay_dict()
            else:
                params['company_size'] = self.company_size
        if self.economic_category_code:
            if hasattr(self.economic_category_code, 'to_alipay_dict'):
                params['economic_category_code'] = self.economic_category_code.to_alipay_dict()
            else:
                params['economic_category_code'] = self.economic_category_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyInformation()
        if 'business_category_code' in d:
            o.business_category_code = d['business_category_code']
        if 'company_cert_effective_date' in d:
            o.company_cert_effective_date = d['company_cert_effective_date']
        if 'company_cert_expiration_date' in d:
            o.company_cert_expiration_date = d['company_cert_expiration_date']
        if 'company_cert_no' in d:
            o.company_cert_no = d['company_cert_no']
        if 'company_cert_type' in d:
            o.company_cert_type = d['company_cert_type']
        if 'company_english_name' in d:
            o.company_english_name = d['company_english_name']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'company_registered_address' in d:
            o.company_registered_address = d['company_registered_address']
        if 'company_registered_capital_amount' in d:
            o.company_registered_capital_amount = d['company_registered_capital_amount']
        if 'company_registered_capital_amount_currency' in d:
            o.company_registered_capital_amount_currency = d['company_registered_capital_amount_currency']
        if 'company_registered_country' in d:
            o.company_registered_country = d['company_registered_country']
        if 'company_size' in d:
            o.company_size = d['company_size']
        if 'economic_category_code' in d:
            o.economic_category_code = d['economic_category_code']
        return o


