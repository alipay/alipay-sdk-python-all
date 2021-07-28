#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxNeworderCreateModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._doc_expire_date = None
        self._doc_id = None
        self._doc_print_date = None
        self._extend_param = None
        self._nationality = None
        self._out_merchant_id = None
        self._passport_name = None
        self._passport_no = None
        self._status = None
        self._status_change_time = None
        self._tax_payment_no = None
        self._tax_refund_amount = None
        self._tax_refund_country = None
        self._tax_refund_currency = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def doc_expire_date(self):
        return self._doc_expire_date

    @doc_expire_date.setter
    def doc_expire_date(self, value):
        self._doc_expire_date = value
    @property
    def doc_id(self):
        return self._doc_id

    @doc_id.setter
    def doc_id(self, value):
        self._doc_id = value
    @property
    def doc_print_date(self):
        return self._doc_print_date

    @doc_print_date.setter
    def doc_print_date(self, value):
        self._doc_print_date = value
    @property
    def extend_param(self):
        return self._extend_param

    @extend_param.setter
    def extend_param(self, value):
        self._extend_param = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_change_time(self):
        return self._status_change_time

    @status_change_time.setter
    def status_change_time(self, value):
        self._status_change_time = value
    @property
    def tax_payment_no(self):
        return self._tax_payment_no

    @tax_payment_no.setter
    def tax_payment_no(self, value):
        self._tax_payment_no = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.doc_expire_date:
            if hasattr(self.doc_expire_date, 'to_alipay_dict'):
                params['doc_expire_date'] = self.doc_expire_date.to_alipay_dict()
            else:
                params['doc_expire_date'] = self.doc_expire_date
        if self.doc_id:
            if hasattr(self.doc_id, 'to_alipay_dict'):
                params['doc_id'] = self.doc_id.to_alipay_dict()
            else:
                params['doc_id'] = self.doc_id
        if self.doc_print_date:
            if hasattr(self.doc_print_date, 'to_alipay_dict'):
                params['doc_print_date'] = self.doc_print_date.to_alipay_dict()
            else:
                params['doc_print_date'] = self.doc_print_date
        if self.extend_param:
            if hasattr(self.extend_param, 'to_alipay_dict'):
                params['extend_param'] = self.extend_param.to_alipay_dict()
            else:
                params['extend_param'] = self.extend_param
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_change_time:
            if hasattr(self.status_change_time, 'to_alipay_dict'):
                params['status_change_time'] = self.status_change_time.to_alipay_dict()
            else:
                params['status_change_time'] = self.status_change_time
        if self.tax_payment_no:
            if hasattr(self.tax_payment_no, 'to_alipay_dict'):
                params['tax_payment_no'] = self.tax_payment_no.to_alipay_dict()
            else:
                params['tax_payment_no'] = self.tax_payment_no
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTaxNeworderCreateModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'doc_expire_date' in d:
            o.doc_expire_date = d['doc_expire_date']
        if 'doc_id' in d:
            o.doc_id = d['doc_id']
        if 'doc_print_date' in d:
            o.doc_print_date = d['doc_print_date']
        if 'extend_param' in d:
            o.extend_param = d['extend_param']
        if 'nationality' in d:
            o.nationality = d['nationality']
        if 'out_merchant_id' in d:
            o.out_merchant_id = d['out_merchant_id']
        if 'passport_name' in d:
            o.passport_name = d['passport_name']
        if 'passport_no' in d:
            o.passport_no = d['passport_no']
        if 'status' in d:
            o.status = d['status']
        if 'status_change_time' in d:
            o.status_change_time = d['status_change_time']
        if 'tax_payment_no' in d:
            o.tax_payment_no = d['tax_payment_no']
        if 'tax_refund_amount' in d:
            o.tax_refund_amount = d['tax_refund_amount']
        if 'tax_refund_country' in d:
            o.tax_refund_country = d['tax_refund_country']
        if 'tax_refund_currency' in d:
            o.tax_refund_currency = d['tax_refund_currency']
        return o


