#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxAdvancedCreateModel(object):

    def __init__(self):
        self._doc_id = None
        self._extend_param = None
        self._identify_account_no = None
        self._identify_account_type = None
        self._nationality = None
        self._out_merchant_id = None
        self._out_tax_refund_no = None
        self._passport_name = None
        self._passport_no = None
        self._pay_timeout = None
        self._tax_refund_amount = None
        self._tax_refund_country = None
        self._tax_refund_currency = None
        self._tax_refund_scene_type = None
        self._user_received_amount = None
        self._user_received_currency = None

    @property
    def doc_id(self):
        return self._doc_id

    @doc_id.setter
    def doc_id(self, value):
        self._doc_id = value
    @property
    def extend_param(self):
        return self._extend_param

    @extend_param.setter
    def extend_param(self, value):
        self._extend_param = value
    @property
    def identify_account_no(self):
        return self._identify_account_no

    @identify_account_no.setter
    def identify_account_no(self, value):
        self._identify_account_no = value
    @property
    def identify_account_type(self):
        return self._identify_account_type

    @identify_account_type.setter
    def identify_account_type(self, value):
        self._identify_account_type = value
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value
    @property
    def out_merchant_id(self):
        return self._out_merchant_id

    @out_merchant_id.setter
    def out_merchant_id(self, value):
        self._out_merchant_id = value
    @property
    def out_tax_refund_no(self):
        return self._out_tax_refund_no

    @out_tax_refund_no.setter
    def out_tax_refund_no(self, value):
        self._out_tax_refund_no = value
    @property
    def passport_name(self):
        return self._passport_name

    @passport_name.setter
    def passport_name(self, value):
        self._passport_name = value
    @property
    def passport_no(self):
        return self._passport_no

    @passport_no.setter
    def passport_no(self, value):
        self._passport_no = value
    @property
    def pay_timeout(self):
        return self._pay_timeout

    @pay_timeout.setter
    def pay_timeout(self, value):
        self._pay_timeout = value
    @property
    def tax_refund_amount(self):
        return self._tax_refund_amount

    @tax_refund_amount.setter
    def tax_refund_amount(self, value):
        self._tax_refund_amount = value
    @property
    def tax_refund_country(self):
        return self._tax_refund_country

    @tax_refund_country.setter
    def tax_refund_country(self, value):
        self._tax_refund_country = value
    @property
    def tax_refund_currency(self):
        return self._tax_refund_currency

    @tax_refund_currency.setter
    def tax_refund_currency(self, value):
        self._tax_refund_currency = value
    @property
    def tax_refund_scene_type(self):
        return self._tax_refund_scene_type

    @tax_refund_scene_type.setter
    def tax_refund_scene_type(self, value):
        self._tax_refund_scene_type = value
    @property
    def user_received_amount(self):
        return self._user_received_amount

    @user_received_amount.setter
    def user_received_amount(self, value):
        self._user_received_amount = value
    @property
    def user_received_currency(self):
        return self._user_received_currency

    @user_received_currency.setter
    def user_received_currency(self, value):
        self._user_received_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.doc_id:
            if hasattr(self.doc_id, 'to_alipay_dict'):
                params['doc_id'] = self.doc_id.to_alipay_dict()
            else:
                params['doc_id'] = self.doc_id
        if self.extend_param:
            if hasattr(self.extend_param, 'to_alipay_dict'):
                params['extend_param'] = self.extend_param.to_alipay_dict()
            else:
                params['extend_param'] = self.extend_param
        if self.identify_account_no:
            if hasattr(self.identify_account_no, 'to_alipay_dict'):
                params['identify_account_no'] = self.identify_account_no.to_alipay_dict()
            else:
                params['identify_account_no'] = self.identify_account_no
        if self.identify_account_type:
            if hasattr(self.identify_account_type, 'to_alipay_dict'):
                params['identify_account_type'] = self.identify_account_type.to_alipay_dict()
            else:
                params['identify_account_type'] = self.identify_account_type
        if self.nationality:
            if hasattr(self.nationality, 'to_alipay_dict'):
                params['nationality'] = self.nationality.to_alipay_dict()
            else:
                params['nationality'] = self.nationality
        if self.out_merchant_id:
            if hasattr(self.out_merchant_id, 'to_alipay_dict'):
                params['out_merchant_id'] = self.out_merchant_id.to_alipay_dict()
            else:
                params['out_merchant_id'] = self.out_merchant_id
        if self.out_tax_refund_no:
            if hasattr(self.out_tax_refund_no, 'to_alipay_dict'):
                params['out_tax_refund_no'] = self.out_tax_refund_no.to_alipay_dict()
            else:
                params['out_tax_refund_no'] = self.out_tax_refund_no
        if self.passport_name:
            if hasattr(self.passport_name, 'to_alipay_dict'):
                params['passport_name'] = self.passport_name.to_alipay_dict()
            else:
                params['passport_name'] = self.passport_name
        if self.passport_no:
            if hasattr(self.passport_no, 'to_alipay_dict'):
                params['passport_no'] = self.passport_no.to_alipay_dict()
            else:
                params['passport_no'] = self.passport_no
        if self.pay_timeout:
            if hasattr(self.pay_timeout, 'to_alipay_dict'):
                params['pay_timeout'] = self.pay_timeout.to_alipay_dict()
            else:
                params['pay_timeout'] = self.pay_timeout
        if self.tax_refund_amount:
            if hasattr(self.tax_refund_amount, 'to_alipay_dict'):
                params['tax_refund_amount'] = self.tax_refund_amount.to_alipay_dict()
            else:
                params['tax_refund_amount'] = self.tax_refund_amount
        if self.tax_refund_country:
            if hasattr(self.tax_refund_country, 'to_alipay_dict'):
                params['tax_refund_country'] = self.tax_refund_country.to_alipay_dict()
            else:
                params['tax_refund_country'] = self.tax_refund_country
        if self.tax_refund_currency:
            if hasattr(self.tax_refund_currency, 'to_alipay_dict'):
                params['tax_refund_currency'] = self.tax_refund_currency.to_alipay_dict()
            else:
                params['tax_refund_currency'] = self.tax_refund_currency
        if self.tax_refund_scene_type:
            if hasattr(self.tax_refund_scene_type, 'to_alipay_dict'):
                params['tax_refund_scene_type'] = self.tax_refund_scene_type.to_alipay_dict()
            else:
                params['tax_refund_scene_type'] = self.tax_refund_scene_type
        if self.user_received_amount:
            if hasattr(self.user_received_amount, 'to_alipay_dict'):
                params['user_received_amount'] = self.user_received_amount.to_alipay_dict()
            else:
                params['user_received_amount'] = self.user_received_amount
        if self.user_received_currency:
            if hasattr(self.user_received_currency, 'to_alipay_dict'):
                params['user_received_currency'] = self.user_received_currency.to_alipay_dict()
            else:
                params['user_received_currency'] = self.user_received_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTaxAdvancedCreateModel()
        if 'doc_id' in d:
            o.doc_id = d['doc_id']
        if 'extend_param' in d:
            o.extend_param = d['extend_param']
        if 'identify_account_no' in d:
            o.identify_account_no = d['identify_account_no']
        if 'identify_account_type' in d:
            o.identify_account_type = d['identify_account_type']
        if 'nationality' in d:
            o.nationality = d['nationality']
        if 'out_merchant_id' in d:
            o.out_merchant_id = d['out_merchant_id']
        if 'out_tax_refund_no' in d:
            o.out_tax_refund_no = d['out_tax_refund_no']
        if 'passport_name' in d:
            o.passport_name = d['passport_name']
        if 'passport_no' in d:
            o.passport_no = d['passport_no']
        if 'pay_timeout' in d:
            o.pay_timeout = d['pay_timeout']
        if 'tax_refund_amount' in d:
            o.tax_refund_amount = d['tax_refund_amount']
        if 'tax_refund_country' in d:
            o.tax_refund_country = d['tax_refund_country']
        if 'tax_refund_currency' in d:
            o.tax_refund_currency = d['tax_refund_currency']
        if 'tax_refund_scene_type' in d:
            o.tax_refund_scene_type = d['tax_refund_scene_type']
        if 'user_received_amount' in d:
            o.user_received_amount = d['user_received_amount']
        if 'user_received_currency' in d:
            o.user_received_currency = d['user_received_currency']
        return o


