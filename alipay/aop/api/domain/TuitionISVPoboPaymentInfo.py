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
        self._card_brand = None
        self._card_expiry_date = None
        self._card_holder_address = None
        self._card_holder_name = None
        self._card_no = None
        self._card_start_date = None
        self._cvv = None
        self._pre_order_id = None

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
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value


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
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
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
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        return o


