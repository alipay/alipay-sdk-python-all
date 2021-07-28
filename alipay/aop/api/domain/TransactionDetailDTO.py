#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransactionAmountModifierDTO import TransactionAmountModifierDTO
from alipay.aop.api.domain.TransactionAuthenticationDetailDTO import TransactionAuthenticationDetailDTO


class TransactionDetailDTO(object):

    def __init__(self):
        self._amount = None
        self._amount_modifiers = None
        self._authentication_details = None
        self._barcode_identifier = None
        self._currency_code = None
        self._dpan_identifier = None
        self._identifier = None
        self._merchant_name = None
        self._nominal_amount = None
        self._primary_funding_source_description = None
        self._raw_merchant_name = None
        self._transaction_date = None
        self._transaction_identifier = None
        self._transaction_status = None
        self._transaction_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def amount_modifiers(self):
        return self._amount_modifiers

    @amount_modifiers.setter
    def amount_modifiers(self, value):
        if isinstance(value, list):
            self._amount_modifiers = list()
            for i in value:
                if isinstance(i, TransactionAmountModifierDTO):
                    self._amount_modifiers.append(i)
                else:
                    self._amount_modifiers.append(TransactionAmountModifierDTO.from_alipay_dict(i))
    @property
    def authentication_details(self):
        return self._authentication_details

    @authentication_details.setter
    def authentication_details(self, value):
        if isinstance(value, TransactionAuthenticationDetailDTO):
            self._authentication_details = value
        else:
            self._authentication_details = TransactionAuthenticationDetailDTO.from_alipay_dict(value)
    @property
    def barcode_identifier(self):
        return self._barcode_identifier

    @barcode_identifier.setter
    def barcode_identifier(self, value):
        self._barcode_identifier = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def dpan_identifier(self):
        return self._dpan_identifier

    @dpan_identifier.setter
    def dpan_identifier(self, value):
        self._dpan_identifier = value
    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        self._identifier = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def nominal_amount(self):
        return self._nominal_amount

    @nominal_amount.setter
    def nominal_amount(self, value):
        self._nominal_amount = value
    @property
    def primary_funding_source_description(self):
        return self._primary_funding_source_description

    @primary_funding_source_description.setter
    def primary_funding_source_description(self, value):
        self._primary_funding_source_description = value
    @property
    def raw_merchant_name(self):
        return self._raw_merchant_name

    @raw_merchant_name.setter
    def raw_merchant_name(self, value):
        self._raw_merchant_name = value
    @property
    def transaction_date(self):
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, value):
        self._transaction_date = value
    @property
    def transaction_identifier(self):
        return self._transaction_identifier

    @transaction_identifier.setter
    def transaction_identifier(self, value):
        self._transaction_identifier = value
    @property
    def transaction_status(self):
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, value):
        self._transaction_status = value
    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self._transaction_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.amount_modifiers:
            if isinstance(self.amount_modifiers, list):
                for i in range(0, len(self.amount_modifiers)):
                    element = self.amount_modifiers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.amount_modifiers[i] = element.to_alipay_dict()
            if hasattr(self.amount_modifiers, 'to_alipay_dict'):
                params['amount_modifiers'] = self.amount_modifiers.to_alipay_dict()
            else:
                params['amount_modifiers'] = self.amount_modifiers
        if self.authentication_details:
            if hasattr(self.authentication_details, 'to_alipay_dict'):
                params['authentication_details'] = self.authentication_details.to_alipay_dict()
            else:
                params['authentication_details'] = self.authentication_details
        if self.barcode_identifier:
            if hasattr(self.barcode_identifier, 'to_alipay_dict'):
                params['barcode_identifier'] = self.barcode_identifier.to_alipay_dict()
            else:
                params['barcode_identifier'] = self.barcode_identifier
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.dpan_identifier:
            if hasattr(self.dpan_identifier, 'to_alipay_dict'):
                params['dpan_identifier'] = self.dpan_identifier.to_alipay_dict()
            else:
                params['dpan_identifier'] = self.dpan_identifier
        if self.identifier:
            if hasattr(self.identifier, 'to_alipay_dict'):
                params['identifier'] = self.identifier.to_alipay_dict()
            else:
                params['identifier'] = self.identifier
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.nominal_amount:
            if hasattr(self.nominal_amount, 'to_alipay_dict'):
                params['nominal_amount'] = self.nominal_amount.to_alipay_dict()
            else:
                params['nominal_amount'] = self.nominal_amount
        if self.primary_funding_source_description:
            if hasattr(self.primary_funding_source_description, 'to_alipay_dict'):
                params['primary_funding_source_description'] = self.primary_funding_source_description.to_alipay_dict()
            else:
                params['primary_funding_source_description'] = self.primary_funding_source_description
        if self.raw_merchant_name:
            if hasattr(self.raw_merchant_name, 'to_alipay_dict'):
                params['raw_merchant_name'] = self.raw_merchant_name.to_alipay_dict()
            else:
                params['raw_merchant_name'] = self.raw_merchant_name
        if self.transaction_date:
            if hasattr(self.transaction_date, 'to_alipay_dict'):
                params['transaction_date'] = self.transaction_date.to_alipay_dict()
            else:
                params['transaction_date'] = self.transaction_date
        if self.transaction_identifier:
            if hasattr(self.transaction_identifier, 'to_alipay_dict'):
                params['transaction_identifier'] = self.transaction_identifier.to_alipay_dict()
            else:
                params['transaction_identifier'] = self.transaction_identifier
        if self.transaction_status:
            if hasattr(self.transaction_status, 'to_alipay_dict'):
                params['transaction_status'] = self.transaction_status.to_alipay_dict()
            else:
                params['transaction_status'] = self.transaction_status
        if self.transaction_type:
            if hasattr(self.transaction_type, 'to_alipay_dict'):
                params['transaction_type'] = self.transaction_type.to_alipay_dict()
            else:
                params['transaction_type'] = self.transaction_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransactionDetailDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'amount_modifiers' in d:
            o.amount_modifiers = d['amount_modifiers']
        if 'authentication_details' in d:
            o.authentication_details = d['authentication_details']
        if 'barcode_identifier' in d:
            o.barcode_identifier = d['barcode_identifier']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'dpan_identifier' in d:
            o.dpan_identifier = d['dpan_identifier']
        if 'identifier' in d:
            o.identifier = d['identifier']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'nominal_amount' in d:
            o.nominal_amount = d['nominal_amount']
        if 'primary_funding_source_description' in d:
            o.primary_funding_source_description = d['primary_funding_source_description']
        if 'raw_merchant_name' in d:
            o.raw_merchant_name = d['raw_merchant_name']
        if 'transaction_date' in d:
            o.transaction_date = d['transaction_date']
        if 'transaction_identifier' in d:
            o.transaction_identifier = d['transaction_identifier']
        if 'transaction_status' in d:
            o.transaction_status = d['transaction_status']
        if 'transaction_type' in d:
            o.transaction_type = d['transaction_type']
        return o


