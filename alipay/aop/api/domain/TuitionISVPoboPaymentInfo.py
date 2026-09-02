#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO
from alipay.aop.api.domain.TuitionAddress import TuitionAddress


class TuitionISVPoboPaymentInfo(object):

    def __init__(self):
        self._additional_payment_info = None
        self._amount = None
        self._bank_address = None
        self._bank_name = None
        self._bank_region = None
        self._card_brand = None
        self._card_expiry_date = None
        self._card_holder_address = None
        self._card_holder_name = None
        self._card_no = None
        self._card_start_date = None
        self._cvv = None
        self._cvv_encrypted = None
        self._pre_order_id = None
        self._quote_price = None
        self._routing_number = None
        self._virtual_account_number = None

    @property
    def additional_payment_info(self):
        return self._additional_payment_info

    @additional_payment_info.setter
    def additional_payment_info(self, value):
        self._additional_payment_info = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, TuitionMoneyDTO):
            self._amount = value
        else:
            self._amount = TuitionMoneyDTO.from_alipay_dict(value)
    @property
    def bank_address(self):
        return self._bank_address

    @bank_address.setter
    def bank_address(self, value):
        self._bank_address = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def bank_region(self):
        return self._bank_region

    @bank_region.setter
    def bank_region(self, value):
        self._bank_region = value
    @property
    def card_brand(self):
        return self._card_brand

    @card_brand.setter
    def card_brand(self, value):
        self._card_brand = value
    @property
    def card_expiry_date(self):
        return self._card_expiry_date

    @card_expiry_date.setter
    def card_expiry_date(self, value):
        self._card_expiry_date = value
    @property
    def card_holder_address(self):
        return self._card_holder_address

    @card_holder_address.setter
    def card_holder_address(self, value):
        if isinstance(value, TuitionAddress):
            self._card_holder_address = value
        else:
            self._card_holder_address = TuitionAddress.from_alipay_dict(value)
    @property
    def card_holder_name(self):
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, value):
        self._card_holder_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_start_date(self):
        return self._card_start_date

    @card_start_date.setter
    def card_start_date(self, value):
        self._card_start_date = value
    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, value):
        self._cvv = value
    @property
    def cvv_encrypted(self):
        return self._cvv_encrypted

    @cvv_encrypted.setter
    def cvv_encrypted(self, value):
        self._cvv_encrypted = value
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def quote_price(self):
        return self._quote_price

    @quote_price.setter
    def quote_price(self, value):
        self._quote_price = value
    @property
    def routing_number(self):
        return self._routing_number

    @routing_number.setter
    def routing_number(self, value):
        self._routing_number = value
    @property
    def virtual_account_number(self):
        return self._virtual_account_number

    @virtual_account_number.setter
    def virtual_account_number(self, value):
        self._virtual_account_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_payment_info:
            if hasattr(self.additional_payment_info, 'to_alipay_dict'):
                params['additional_payment_info'] = self.additional_payment_info.to_alipay_dict()
            else:
                params['additional_payment_info'] = self.additional_payment_info
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
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
        if self.bank_region:
            if hasattr(self.bank_region, 'to_alipay_dict'):
                params['bank_region'] = self.bank_region.to_alipay_dict()
            else:
                params['bank_region'] = self.bank_region
        if self.card_brand:
            if hasattr(self.card_brand, 'to_alipay_dict'):
                params['card_brand'] = self.card_brand.to_alipay_dict()
            else:
                params['card_brand'] = self.card_brand
        if self.card_expiry_date:
            if hasattr(self.card_expiry_date, 'to_alipay_dict'):
                params['card_expiry_date'] = self.card_expiry_date.to_alipay_dict()
            else:
                params['card_expiry_date'] = self.card_expiry_date
        if self.card_holder_address:
            if hasattr(self.card_holder_address, 'to_alipay_dict'):
                params['card_holder_address'] = self.card_holder_address.to_alipay_dict()
            else:
                params['card_holder_address'] = self.card_holder_address
        if self.card_holder_name:
            if hasattr(self.card_holder_name, 'to_alipay_dict'):
                params['card_holder_name'] = self.card_holder_name.to_alipay_dict()
            else:
                params['card_holder_name'] = self.card_holder_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_start_date:
            if hasattr(self.card_start_date, 'to_alipay_dict'):
                params['card_start_date'] = self.card_start_date.to_alipay_dict()
            else:
                params['card_start_date'] = self.card_start_date
        if self.cvv:
            if hasattr(self.cvv, 'to_alipay_dict'):
                params['cvv'] = self.cvv.to_alipay_dict()
            else:
                params['cvv'] = self.cvv
        if self.cvv_encrypted:
            if hasattr(self.cvv_encrypted, 'to_alipay_dict'):
                params['cvv_encrypted'] = self.cvv_encrypted.to_alipay_dict()
            else:
                params['cvv_encrypted'] = self.cvv_encrypted
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        if self.quote_price:
            if hasattr(self.quote_price, 'to_alipay_dict'):
                params['quote_price'] = self.quote_price.to_alipay_dict()
            else:
                params['quote_price'] = self.quote_price
        if self.routing_number:
            if hasattr(self.routing_number, 'to_alipay_dict'):
                params['routing_number'] = self.routing_number.to_alipay_dict()
            else:
                params['routing_number'] = self.routing_number
        if self.virtual_account_number:
            if hasattr(self.virtual_account_number, 'to_alipay_dict'):
                params['virtual_account_number'] = self.virtual_account_number.to_alipay_dict()
            else:
                params['virtual_account_number'] = self.virtual_account_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVPoboPaymentInfo()
        if 'additional_payment_info' in d:
            o.additional_payment_info = d['additional_payment_info']
        if 'amount' in d:
            o.amount = d['amount']
        if 'bank_address' in d:
            o.bank_address = d['bank_address']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'bank_region' in d:
            o.bank_region = d['bank_region']
        if 'card_brand' in d:
            o.card_brand = d['card_brand']
        if 'card_expiry_date' in d:
            o.card_expiry_date = d['card_expiry_date']
        if 'card_holder_address' in d:
            o.card_holder_address = d['card_holder_address']
        if 'card_holder_name' in d:
            o.card_holder_name = d['card_holder_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_start_date' in d:
            o.card_start_date = d['card_start_date']
        if 'cvv' in d:
            o.cvv = d['cvv']
        if 'cvv_encrypted' in d:
            o.cvv_encrypted = d['cvv_encrypted']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'quote_price' in d:
            o.quote_price = d['quote_price']
        if 'routing_number' in d:
            o.routing_number = d['routing_number']
        if 'virtual_account_number' in d:
            o.virtual_account_number = d['virtual_account_number']
        return o


