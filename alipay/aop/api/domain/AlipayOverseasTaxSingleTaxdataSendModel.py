#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxSingleTaxdataSendModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._available_day = None
        self._barcode_no = None
        self._confirm_date = None
        self._country_code = None
        self._departure_point = None
        self._doc_expire_date = None
        self._doc_id = None
        self._final_refund_amount = None
        self._final_refund_currency = None
        self._memo = None
        self._merchant_notify_url = None
        self._nationality = None
        self._out_order_no = None
        self._passport_name = None
        self._passport_no = None
        self._phone_no = None
        self._refund_amount = None
        self._refund_company_name = None
        self._refund_currency = None
        self._refund_print_date = None
        self._refund_scene_type = None
        self._sales_amount = None
        self._sales_currency = None
        self._sales_date = None
        self._sub_trsp_id = None
        self._user_id_open_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def available_day(self):
        return self._available_day

    @available_day.setter
    def available_day(self, value):
        self._available_day = value
    @property
    def barcode_no(self):
        return self._barcode_no

    @barcode_no.setter
    def barcode_no(self, value):
        self._barcode_no = value
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
    def final_refund_amount(self):
        return self._final_refund_amount

    @final_refund_amount.setter
    def final_refund_amount(self, value):
        self._final_refund_amount = value
    @property
    def final_refund_currency(self):
        return self._final_refund_currency

    @final_refund_currency.setter
    def final_refund_currency(self, value):
        self._final_refund_currency = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_notify_url(self):
        return self._merchant_notify_url

    @merchant_notify_url.setter
    def merchant_notify_url(self, value):
        self._merchant_notify_url = value
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
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_company_name(self):
        return self._refund_company_name

    @refund_company_name.setter
    def refund_company_name(self, value):
        self._refund_company_name = value
    @property
    def refund_currency(self):
        return self._refund_currency

    @refund_currency.setter
    def refund_currency(self, value):
        self._refund_currency = value
    @property
    def refund_print_date(self):
        return self._refund_print_date

    @refund_print_date.setter
    def refund_print_date(self, value):
        self._refund_print_date = value
    @property
    def refund_scene_type(self):
        return self._refund_scene_type

    @refund_scene_type.setter
    def refund_scene_type(self, value):
        self._refund_scene_type = value
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
    def sub_trsp_id(self):
        return self._sub_trsp_id

    @sub_trsp_id.setter
    def sub_trsp_id(self, value):
        self._sub_trsp_id = value
    @property
    def user_id_open_id(self):
        return self._user_id_open_id

    @user_id_open_id.setter
    def user_id_open_id(self, value):
        self._user_id_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.available_day:
            if hasattr(self.available_day, 'to_alipay_dict'):
                params['available_day'] = self.available_day.to_alipay_dict()
            else:
                params['available_day'] = self.available_day
        if self.barcode_no:
            if hasattr(self.barcode_no, 'to_alipay_dict'):
                params['barcode_no'] = self.barcode_no.to_alipay_dict()
            else:
                params['barcode_no'] = self.barcode_no
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
        if self.final_refund_amount:
            if hasattr(self.final_refund_amount, 'to_alipay_dict'):
                params['final_refund_amount'] = self.final_refund_amount.to_alipay_dict()
            else:
                params['final_refund_amount'] = self.final_refund_amount
        if self.final_refund_currency:
            if hasattr(self.final_refund_currency, 'to_alipay_dict'):
                params['final_refund_currency'] = self.final_refund_currency.to_alipay_dict()
            else:
                params['final_refund_currency'] = self.final_refund_currency
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_notify_url:
            if hasattr(self.merchant_notify_url, 'to_alipay_dict'):
                params['merchant_notify_url'] = self.merchant_notify_url.to_alipay_dict()
            else:
                params['merchant_notify_url'] = self.merchant_notify_url
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
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_company_name:
            if hasattr(self.refund_company_name, 'to_alipay_dict'):
                params['refund_company_name'] = self.refund_company_name.to_alipay_dict()
            else:
                params['refund_company_name'] = self.refund_company_name
        if self.refund_currency:
            if hasattr(self.refund_currency, 'to_alipay_dict'):
                params['refund_currency'] = self.refund_currency.to_alipay_dict()
            else:
                params['refund_currency'] = self.refund_currency
        if self.refund_print_date:
            if hasattr(self.refund_print_date, 'to_alipay_dict'):
                params['refund_print_date'] = self.refund_print_date.to_alipay_dict()
            else:
                params['refund_print_date'] = self.refund_print_date
        if self.refund_scene_type:
            if hasattr(self.refund_scene_type, 'to_alipay_dict'):
                params['refund_scene_type'] = self.refund_scene_type.to_alipay_dict()
            else:
                params['refund_scene_type'] = self.refund_scene_type
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
        if self.sub_trsp_id:
            if hasattr(self.sub_trsp_id, 'to_alipay_dict'):
                params['sub_trsp_id'] = self.sub_trsp_id.to_alipay_dict()
            else:
                params['sub_trsp_id'] = self.sub_trsp_id
        if self.user_id_open_id:
            if hasattr(self.user_id_open_id, 'to_alipay_dict'):
                params['user_id_open_id'] = self.user_id_open_id.to_alipay_dict()
            else:
                params['user_id_open_id'] = self.user_id_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTaxSingleTaxdataSendModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'available_day' in d:
            o.available_day = d['available_day']
        if 'barcode_no' in d:
            o.barcode_no = d['barcode_no']
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
        if 'final_refund_amount' in d:
            o.final_refund_amount = d['final_refund_amount']
        if 'final_refund_currency' in d:
            o.final_refund_currency = d['final_refund_currency']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_notify_url' in d:
            o.merchant_notify_url = d['merchant_notify_url']
        if 'nationality' in d:
            o.nationality = d['nationality']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'passport_name' in d:
            o.passport_name = d['passport_name']
        if 'passport_no' in d:
            o.passport_no = d['passport_no']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_company_name' in d:
            o.refund_company_name = d['refund_company_name']
        if 'refund_currency' in d:
            o.refund_currency = d['refund_currency']
        if 'refund_print_date' in d:
            o.refund_print_date = d['refund_print_date']
        if 'refund_scene_type' in d:
            o.refund_scene_type = d['refund_scene_type']
        if 'sales_amount' in d:
            o.sales_amount = d['sales_amount']
        if 'sales_currency' in d:
            o.sales_currency = d['sales_currency']
        if 'sales_date' in d:
            o.sales_date = d['sales_date']
        if 'sub_trsp_id' in d:
            o.sub_trsp_id = d['sub_trsp_id']
        if 'user_id_open_id' in d:
            o.user_id_open_id = d['user_id_open_id']
        return o


