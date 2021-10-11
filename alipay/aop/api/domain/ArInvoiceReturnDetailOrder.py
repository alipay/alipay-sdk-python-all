#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArInvoiceReturnDetailOrder(object):

    def __init__(self):
        self._attach_urls = None
        self._attch_type = None
        self._auth = None
        self._invoice_id = None
        self._red_notice_no = None

    @property
    def attach_urls(self):
        return self._attach_urls

    @attach_urls.setter
    def attach_urls(self, value):
        if isinstance(value, list):
            self._attach_urls = list()
            for i in value:
                self._attach_urls.append(i)
    @property
    def attch_type(self):
        return self._attch_type

    @attch_type.setter
    def attch_type(self, value):
        self._attch_type = value
    @property
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self, value):
        self._auth = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def red_notice_no(self):
        return self._red_notice_no

    @red_notice_no.setter
    def red_notice_no(self, value):
        self._red_notice_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.attach_urls:
            if isinstance(self.attach_urls, list):
                for i in range(0, len(self.attach_urls)):
                    element = self.attach_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attach_urls[i] = element.to_alipay_dict()
            if hasattr(self.attach_urls, 'to_alipay_dict'):
                params['attach_urls'] = self.attach_urls.to_alipay_dict()
            else:
                params['attach_urls'] = self.attach_urls
        if self.attch_type:
            if hasattr(self.attch_type, 'to_alipay_dict'):
                params['attch_type'] = self.attch_type.to_alipay_dict()
            else:
                params['attch_type'] = self.attch_type
        if self.auth:
            if hasattr(self.auth, 'to_alipay_dict'):
                params['auth'] = self.auth.to_alipay_dict()
            else:
                params['auth'] = self.auth
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.red_notice_no:
            if hasattr(self.red_notice_no, 'to_alipay_dict'):
                params['red_notice_no'] = self.red_notice_no.to_alipay_dict()
            else:
                params['red_notice_no'] = self.red_notice_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArInvoiceReturnDetailOrder()
        if 'attach_urls' in d:
            o.attach_urls = d['attach_urls']
        if 'attch_type' in d:
            o.attch_type = d['attch_type']
        if 'auth' in d:
            o.auth = d['auth']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'red_notice_no' in d:
            o.red_notice_no = d['red_notice_no']
        return o


