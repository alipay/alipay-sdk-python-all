#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceTitleInfo import InvoiceTitleInfo
from alipay.aop.api.domain.InvoiceUserMailInfoOrder import InvoiceUserMailInfoOrder


class InvoiceTitle(object):

    def __init__(self):
        self._biz_app_id = None
        self._invoice_title_info = None
        self._invoice_user_mail_info_orders = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def invoice_title_info(self):
        return self._invoice_title_info

    @invoice_title_info.setter
    def invoice_title_info(self, value):
        if isinstance(value, InvoiceTitleInfo):
            self._invoice_title_info = value
        else:
            self._invoice_title_info = InvoiceTitleInfo.from_alipay_dict(value)
    @property
    def invoice_user_mail_info_orders(self):
        return self._invoice_user_mail_info_orders

    @invoice_user_mail_info_orders.setter
    def invoice_user_mail_info_orders(self, value):
        if isinstance(value, list):
            self._invoice_user_mail_info_orders = list()
            for i in value:
                if isinstance(i, InvoiceUserMailInfoOrder):
                    self._invoice_user_mail_info_orders.append(i)
                else:
                    self._invoice_user_mail_info_orders.append(InvoiceUserMailInfoOrder.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.invoice_title_info:
            if hasattr(self.invoice_title_info, 'to_alipay_dict'):
                params['invoice_title_info'] = self.invoice_title_info.to_alipay_dict()
            else:
                params['invoice_title_info'] = self.invoice_title_info
        if self.invoice_user_mail_info_orders:
            if isinstance(self.invoice_user_mail_info_orders, list):
                for i in range(0, len(self.invoice_user_mail_info_orders)):
                    element = self.invoice_user_mail_info_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_user_mail_info_orders[i] = element.to_alipay_dict()
            if hasattr(self.invoice_user_mail_info_orders, 'to_alipay_dict'):
                params['invoice_user_mail_info_orders'] = self.invoice_user_mail_info_orders.to_alipay_dict()
            else:
                params['invoice_user_mail_info_orders'] = self.invoice_user_mail_info_orders
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceTitle()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'invoice_title_info' in d:
            o.invoice_title_info = d['invoice_title_info']
        if 'invoice_user_mail_info_orders' in d:
            o.invoice_user_mail_info_orders = d['invoice_user_mail_info_orders']
        return o


