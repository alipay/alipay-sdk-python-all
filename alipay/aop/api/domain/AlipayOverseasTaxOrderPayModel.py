#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxOrderPayModel(object):

    def __init__(self):
        self._available_day = None
        self._biz_mode = None
        self._company_name = None
        self._confirm_date = None
        self._country_code = None
        self._departure_point = None
        self._doc_expire_date = None
        self._doc_id = None
        self._extend_param = None
        self._identify_account_no = None
        self._identify_account_type = None
        self._nationality = None
        self._out_order_no = None
        self._passport_name = None
        self._passport_no = None
        self._sales_amount = None
        self._sales_currency = None
        self._sales_date = None
        self._tax_refund_amount = None
        self._tax_refund_currency = None
        self._tax_refund_print_date = None
        self._tax_refund_scene_type = None
        self._user_received_amount = None
        self._user_received_currency = None

    @property
    def available_day(self):
        return self._available_day

    @available_day.setter
    def available_day(self, value):
        self._available_day = value
    @property
    def biz_mode(self):
        return self._biz_mode

    @biz_mode.setter
    def biz_mode(self, value):
        self._biz_mode = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def confirm_date(self):
        return self._confirm_date

    @confirm_date.setter
    def confirm_date(self, value):
        self._confirm_date = value
    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
    @property
    def departure_point(self):
        return self._departure_point

    @departure_point.setter
    def departure_point(self, value):
        self._departure_point = value
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
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
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
    def sales_amount(self):
        return self._sales_amount

    @sales_amount.setter
    def sales_amount(self, value):
        self._sales_amount = value
    @property
    def sales_currency(self):
        return self._sales_currency

    @sales_currency.setter
    def sales_currency(self, value):
        self._sales_currency = value
    @property
    def sales_date(self):
        return self._sales_date

    @sales_date.setter
    def sales_date(self, value):
        self._sales_date = value
    @property
    def tax_refund_amount(self):
        return self._tax_refund_amount

    @tax_refund_amount.setter
    def tax_refund_amount(self, value):
        self._tax_refund_amount = value
    @property
    def tax_refund_currency(self):
        return self._tax_refund_currency

    @tax_refund_currency.setter
    def tax_refund_currency(self, value):
        self._tax_refund_currency = value
    @property
    def tax_refund_print_date(self):
        return self._tax_refund_print_date

    @tax_refund_print_date.setter
    def tax_refund_print_date(self, value):
        self._tax_refund_print_date = value
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
        if self.available_day:
            if hasattr(self.available_day, 'to_alipay_dict'):
                params['available_day'] = self.available_day.to_alipay_dict()
            else:
                params['available_day'] = self.available_day
        if self.biz_mode:
            if hasattr(self.biz_mode, 'to_alipay_dict'):
                params['biz_mode'] = self.biz_mode.to_alipay_dict()
            else:
                params['biz_mode'] = self.biz_mode
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.confirm_date:
            if hasattr(self.confirm_date, 'to_alipay_dict'):
                params['confirm_date'] = self.confirm_date.to_alipay_dict()
            else:
                params['confirm_date'] = self.confirm_date
        if self.country_code:
            if hasattr(self.country_code, 'to_alipay_dict'):
                params['country_code'] = self.country_code.to_alipay_dict()
            else:
                params['country_code'] = self.country_code
        if self.departure_point:
            if hasattr(self.departure_point, 'to_alipay_dict'):
                params['departure_point'] = self.departure_point.to_alipay_dict()
            else:
                params['departure_point'] = self.departure_point
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
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
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
        if self.sales_amount:
            if hasattr(self.sales_amount, 'to_alipay_dict'):
                params['sales_amount'] = self.sales_amount.to_alipay_dict()
            else:
                params['sales_amount'] = self.sales_amount
        if self.sales_currency:
            if hasattr(self.sales_currency, 'to_alipay_dict'):
                params['sales_currency'] = self.sales_currency.to_alipay_dict()
            else:
                params['sales_currency'] = self.sales_currency
        if self.sales_date:
            if hasattr(self.sales_date, 'to_alipay_dict'):
                params['sales_date'] = self.sales_date.to_alipay_dict()
            else:
                params['sales_date'] = self.sales_date
        if self.tax_refund_amount:
            if hasattr(self.tax_refund_amount, 'to_alipay_dict'):
                params['tax_refund_amount'] = self.tax_refund_amount.to_alipay_dict()
            else:
                params['tax_refund_amount'] = self.tax_refund_amount
        if self.tax_refund_currency:
            if hasattr(self.tax_refund_currency, 'to_alipay_dict'):
                params['tax_refund_currency'] = self.tax_refund_currency.to_alipay_dict()
            else:
                params['tax_refund_currency'] = self.tax_refund_currency
        if self.tax_refund_print_date:
            if hasattr(self.tax_refund_print_date, 'to_alipay_dict'):
                params['tax_refund_print_date'] = self.tax_refund_print_date.to_alipay_dict()
            else:
                params['tax_refund_print_date'] = self.tax_refund_print_date
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
        o = AlipayOverseasTaxOrderPayModel()
        if 'available_day' in d:
            o.available_day = d['available_day']
        if 'biz_mode' in d:
            o.biz_mode = d['biz_mode']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'confirm_date' in d:
            o.confirm_date = d['confirm_date']
        if 'country_code' in d:
            o.country_code = d['country_code']
        if 'departure_point' in d:
            o.departure_point = d['departure_point']
        if 'doc_expire_date' in d:
            o.doc_expire_date = d['doc_expire_date']
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
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'passport_name' in d:
            o.passport_name = d['passport_name']
        if 'passport_no' in d:
            o.passport_no = d['passport_no']
        if 'sales_amount' in d:
            o.sales_amount = d['sales_amount']
        if 'sales_currency' in d:
            o.sales_currency = d['sales_currency']
        if 'sales_date' in d:
            o.sales_date = d['sales_date']
        if 'tax_refund_amount' in d:
            o.tax_refund_amount = d['tax_refund_amount']
        if 'tax_refund_currency' in d:
            o.tax_refund_currency = d['tax_refund_currency']
        if 'tax_refund_print_date' in d:
            o.tax_refund_print_date = d['tax_refund_print_date']
        if 'tax_refund_scene_type' in d:
            o.tax_refund_scene_type = d['tax_refund_scene_type']
        if 'user_received_amount' in d:
            o.user_received_amount = d['user_received_amount']
        if 'user_received_currency' in d:
            o.user_received_currency = d['user_received_currency']
        return o


