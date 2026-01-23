#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiUserMailInfoOrder import OpenApiUserMailInfoOrder


class OpenApiBuyerInvoiceInfoOrder(object):

    def __init__(self):
        self._addressing = None
        self._auto = None
        self._exceed_invoice_handle_way = None
        self._invoice_title = None
        self._qualification = None
        self._registered_address = None
        self._registered_phone_no = None
        self._tax_no = None
        self._taxpayer_start_date = None
        self._taxpayer_type = None
        self._user_id = None
        self._user_mail_info_orders = None

    @property
    def addressing(self):
        return self._addressing

    @addressing.setter
    def addressing(self, value):
        self._addressing = value
    @property
    def auto(self):
        return self._auto

    @auto.setter
    def auto(self, value):
        self._auto = value
    @property
    def exceed_invoice_handle_way(self):
        return self._exceed_invoice_handle_way

    @exceed_invoice_handle_way.setter
    def exceed_invoice_handle_way(self, value):
        self._exceed_invoice_handle_way = value
    @property
    def invoice_title(self):
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, value):
        self._invoice_title = value
    @property
    def qualification(self):
        return self._qualification

    @qualification.setter
    def qualification(self, value):
        self._qualification = value
    @property
    def registered_address(self):
        return self._registered_address

    @registered_address.setter
    def registered_address(self, value):
        self._registered_address = value
    @property
    def registered_phone_no(self):
        return self._registered_phone_no

    @registered_phone_no.setter
    def registered_phone_no(self, value):
        self._registered_phone_no = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def taxpayer_start_date(self):
        return self._taxpayer_start_date

    @taxpayer_start_date.setter
    def taxpayer_start_date(self, value):
        self._taxpayer_start_date = value
    @property
    def taxpayer_type(self):
        return self._taxpayer_type

    @taxpayer_type.setter
    def taxpayer_type(self, value):
        self._taxpayer_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_mail_info_orders(self):
        return self._user_mail_info_orders

    @user_mail_info_orders.setter
    def user_mail_info_orders(self, value):
        if isinstance(value, list):
            self._user_mail_info_orders = list()
            for i in value:
                if isinstance(i, OpenApiUserMailInfoOrder):
                    self._user_mail_info_orders.append(i)
                else:
                    self._user_mail_info_orders.append(OpenApiUserMailInfoOrder.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.addressing:
            if hasattr(self.addressing, 'to_alipay_dict'):
                params['addressing'] = self.addressing.to_alipay_dict()
            else:
                params['addressing'] = self.addressing
        if self.auto:
            if hasattr(self.auto, 'to_alipay_dict'):
                params['auto'] = self.auto.to_alipay_dict()
            else:
                params['auto'] = self.auto
        if self.exceed_invoice_handle_way:
            if hasattr(self.exceed_invoice_handle_way, 'to_alipay_dict'):
                params['exceed_invoice_handle_way'] = self.exceed_invoice_handle_way.to_alipay_dict()
            else:
                params['exceed_invoice_handle_way'] = self.exceed_invoice_handle_way
        if self.invoice_title:
            if hasattr(self.invoice_title, 'to_alipay_dict'):
                params['invoice_title'] = self.invoice_title.to_alipay_dict()
            else:
                params['invoice_title'] = self.invoice_title
        if self.qualification:
            if hasattr(self.qualification, 'to_alipay_dict'):
                params['qualification'] = self.qualification.to_alipay_dict()
            else:
                params['qualification'] = self.qualification
        if self.registered_address:
            if hasattr(self.registered_address, 'to_alipay_dict'):
                params['registered_address'] = self.registered_address.to_alipay_dict()
            else:
                params['registered_address'] = self.registered_address
        if self.registered_phone_no:
            if hasattr(self.registered_phone_no, 'to_alipay_dict'):
                params['registered_phone_no'] = self.registered_phone_no.to_alipay_dict()
            else:
                params['registered_phone_no'] = self.registered_phone_no
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.taxpayer_start_date:
            if hasattr(self.taxpayer_start_date, 'to_alipay_dict'):
                params['taxpayer_start_date'] = self.taxpayer_start_date.to_alipay_dict()
            else:
                params['taxpayer_start_date'] = self.taxpayer_start_date
        if self.taxpayer_type:
            if hasattr(self.taxpayer_type, 'to_alipay_dict'):
                params['taxpayer_type'] = self.taxpayer_type.to_alipay_dict()
            else:
                params['taxpayer_type'] = self.taxpayer_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_mail_info_orders:
            if isinstance(self.user_mail_info_orders, list):
                for i in range(0, len(self.user_mail_info_orders)):
                    element = self.user_mail_info_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_mail_info_orders[i] = element.to_alipay_dict()
            if hasattr(self.user_mail_info_orders, 'to_alipay_dict'):
                params['user_mail_info_orders'] = self.user_mail_info_orders.to_alipay_dict()
            else:
                params['user_mail_info_orders'] = self.user_mail_info_orders
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiBuyerInvoiceInfoOrder()
        if 'addressing' in d:
            o.addressing = d['addressing']
        if 'auto' in d:
            o.auto = d['auto']
        if 'exceed_invoice_handle_way' in d:
            o.exceed_invoice_handle_way = d['exceed_invoice_handle_way']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'qualification' in d:
            o.qualification = d['qualification']
        if 'registered_address' in d:
            o.registered_address = d['registered_address']
        if 'registered_phone_no' in d:
            o.registered_phone_no = d['registered_phone_no']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'taxpayer_start_date' in d:
            o.taxpayer_start_date = d['taxpayer_start_date']
        if 'taxpayer_type' in d:
            o.taxpayer_type = d['taxpayer_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_mail_info_orders' in d:
            o.user_mail_info_orders = d['user_mail_info_orders']
        return o


