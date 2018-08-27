#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsAddressee import InsAddressee
from alipay.aop.api.domain.InsInvoiceApplyItem import InsInvoiceApplyItem


class AlipayInsSceneInvoiceApplyModel(object):

    def __init__(self):
        self._delivery_type = None
        self._invoice_addressee = None
        self._invoice_apply_item = None
        self._invoice_date = None
        self._invoice_title = None
        self._invoice_type = None
        self._out_biz_no = None
        self._out_request_no = None

    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def invoice_addressee(self):
        return self._invoice_addressee

    @invoice_addressee.setter
    def invoice_addressee(self, value):
        if isinstance(value, InsAddressee):
            self._invoice_addressee = value
        else:
            self._invoice_addressee = InsAddressee.from_alipay_dict(value)
    @property
    def invoice_apply_item(self):
        return self._invoice_apply_item

    @invoice_apply_item.setter
    def invoice_apply_item(self, value):
        if isinstance(value, InsInvoiceApplyItem):
            self._invoice_apply_item = value
        else:
            self._invoice_apply_item = InsInvoiceApplyItem.from_alipay_dict(value)
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_title(self):
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, value):
        self._invoice_title = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.invoice_addressee:
            if hasattr(self.invoice_addressee, 'to_alipay_dict'):
                params['invoice_addressee'] = self.invoice_addressee.to_alipay_dict()
            else:
                params['invoice_addressee'] = self.invoice_addressee
        if self.invoice_apply_item:
            if hasattr(self.invoice_apply_item, 'to_alipay_dict'):
                params['invoice_apply_item'] = self.invoice_apply_item.to_alipay_dict()
            else:
                params['invoice_apply_item'] = self.invoice_apply_item
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_title:
            if hasattr(self.invoice_title, 'to_alipay_dict'):
                params['invoice_title'] = self.invoice_title.to_alipay_dict()
            else:
                params['invoice_title'] = self.invoice_title
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInvoiceApplyModel()
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'invoice_addressee' in d:
            o.invoice_addressee = d['invoice_addressee']
        if 'invoice_apply_item' in d:
            o.invoice_apply_item = d['invoice_apply_item']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


