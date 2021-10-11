#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ArInvoiceReturnOrderDetailOpenApiResponse(object):

    def __init__(self):
        self._attach_urls = None
        self._auth = None
        self._creator = None
        self._gmt_create = None
        self._gmt_modified = None
        self._invoice_amt = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_id = None
        self._invoice_no = None
        self._invoice_status = None
        self._invoice_type = None
        self._last_moder = None
        self._order_no = None
        self._re_invoice_code = None
        self._re_invoice_id = None
        self._re_invoice_no = None
        self._red_notice_no = None
        self._return_order_detail_id = None

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
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self, value):
        self._auth = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_amt = value
        else:
            self._invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def last_moder(self):
        return self._last_moder

    @last_moder.setter
    def last_moder(self, value):
        self._last_moder = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def re_invoice_code(self):
        return self._re_invoice_code

    @re_invoice_code.setter
    def re_invoice_code(self, value):
        self._re_invoice_code = value
    @property
    def re_invoice_id(self):
        return self._re_invoice_id

    @re_invoice_id.setter
    def re_invoice_id(self, value):
        self._re_invoice_id = value
    @property
    def re_invoice_no(self):
        return self._re_invoice_no

    @re_invoice_no.setter
    def re_invoice_no(self, value):
        self._re_invoice_no = value
    @property
    def red_notice_no(self):
        return self._red_notice_no

    @red_notice_no.setter
    def red_notice_no(self, value):
        self._red_notice_no = value
    @property
    def return_order_detail_id(self):
        return self._return_order_detail_id

    @return_order_detail_id.setter
    def return_order_detail_id(self, value):
        self._return_order_detail_id = value


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
        if self.auth:
            if hasattr(self.auth, 'to_alipay_dict'):
                params['auth'] = self.auth.to_alipay_dict()
            else:
                params['auth'] = self.auth
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.last_moder:
            if hasattr(self.last_moder, 'to_alipay_dict'):
                params['last_moder'] = self.last_moder.to_alipay_dict()
            else:
                params['last_moder'] = self.last_moder
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.re_invoice_code:
            if hasattr(self.re_invoice_code, 'to_alipay_dict'):
                params['re_invoice_code'] = self.re_invoice_code.to_alipay_dict()
            else:
                params['re_invoice_code'] = self.re_invoice_code
        if self.re_invoice_id:
            if hasattr(self.re_invoice_id, 'to_alipay_dict'):
                params['re_invoice_id'] = self.re_invoice_id.to_alipay_dict()
            else:
                params['re_invoice_id'] = self.re_invoice_id
        if self.re_invoice_no:
            if hasattr(self.re_invoice_no, 'to_alipay_dict'):
                params['re_invoice_no'] = self.re_invoice_no.to_alipay_dict()
            else:
                params['re_invoice_no'] = self.re_invoice_no
        if self.red_notice_no:
            if hasattr(self.red_notice_no, 'to_alipay_dict'):
                params['red_notice_no'] = self.red_notice_no.to_alipay_dict()
            else:
                params['red_notice_no'] = self.red_notice_no
        if self.return_order_detail_id:
            if hasattr(self.return_order_detail_id, 'to_alipay_dict'):
                params['return_order_detail_id'] = self.return_order_detail_id.to_alipay_dict()
            else:
                params['return_order_detail_id'] = self.return_order_detail_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArInvoiceReturnOrderDetailOpenApiResponse()
        if 'attach_urls' in d:
            o.attach_urls = d['attach_urls']
        if 'auth' in d:
            o.auth = d['auth']
        if 'creator' in d:
            o.creator = d['creator']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'last_moder' in d:
            o.last_moder = d['last_moder']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 're_invoice_code' in d:
            o.re_invoice_code = d['re_invoice_code']
        if 're_invoice_id' in d:
            o.re_invoice_id = d['re_invoice_id']
        if 're_invoice_no' in d:
            o.re_invoice_no = d['re_invoice_no']
        if 'red_notice_no' in d:
            o.red_notice_no = d['red_notice_no']
        if 'return_order_detail_id' in d:
            o.return_order_detail_id = d['return_order_detail_id']
        return o


