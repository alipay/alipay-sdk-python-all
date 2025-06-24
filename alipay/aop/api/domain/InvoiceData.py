#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceData(object):

    def __init__(self):
        self._buyer_invoice_title = None
        self._inst_id = None
        self._invoice_amount = None
        self._invoice_amount_currency = None
        self._invoice_apply_date = None
        self._invoice_id = None
        self._invoice_material = None
        self._invoice_no = None
        self._invoice_open_date = None
        self._invoice_status = None
        self._mail_status = None
        self._open_api_id = None
        self._out_side_download_url = None

    @property
    def buyer_invoice_title(self):
        return self._buyer_invoice_title

    @buyer_invoice_title.setter
    def buyer_invoice_title(self, value):
        self._buyer_invoice_title = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def invoice_amount_currency(self):
        return self._invoice_amount_currency

    @invoice_amount_currency.setter
    def invoice_amount_currency(self, value):
        self._invoice_amount_currency = value
    @property
    def invoice_apply_date(self):
        return self._invoice_apply_date

    @invoice_apply_date.setter
    def invoice_apply_date(self, value):
        self._invoice_apply_date = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_open_date(self):
        return self._invoice_open_date

    @invoice_open_date.setter
    def invoice_open_date(self, value):
        self._invoice_open_date = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def mail_status(self):
        return self._mail_status

    @mail_status.setter
    def mail_status(self, value):
        self._mail_status = value
    @property
    def open_api_id(self):
        return self._open_api_id

    @open_api_id.setter
    def open_api_id(self, value):
        self._open_api_id = value
    @property
    def out_side_download_url(self):
        return self._out_side_download_url

    @out_side_download_url.setter
    def out_side_download_url(self, value):
        self._out_side_download_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_invoice_title:
            if hasattr(self.buyer_invoice_title, 'to_alipay_dict'):
                params['buyer_invoice_title'] = self.buyer_invoice_title.to_alipay_dict()
            else:
                params['buyer_invoice_title'] = self.buyer_invoice_title
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.invoice_amount_currency:
            if hasattr(self.invoice_amount_currency, 'to_alipay_dict'):
                params['invoice_amount_currency'] = self.invoice_amount_currency.to_alipay_dict()
            else:
                params['invoice_amount_currency'] = self.invoice_amount_currency
        if self.invoice_apply_date:
            if hasattr(self.invoice_apply_date, 'to_alipay_dict'):
                params['invoice_apply_date'] = self.invoice_apply_date.to_alipay_dict()
            else:
                params['invoice_apply_date'] = self.invoice_apply_date
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_open_date:
            if hasattr(self.invoice_open_date, 'to_alipay_dict'):
                params['invoice_open_date'] = self.invoice_open_date.to_alipay_dict()
            else:
                params['invoice_open_date'] = self.invoice_open_date
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.mail_status:
            if hasattr(self.mail_status, 'to_alipay_dict'):
                params['mail_status'] = self.mail_status.to_alipay_dict()
            else:
                params['mail_status'] = self.mail_status
        if self.open_api_id:
            if hasattr(self.open_api_id, 'to_alipay_dict'):
                params['open_api_id'] = self.open_api_id.to_alipay_dict()
            else:
                params['open_api_id'] = self.open_api_id
        if self.out_side_download_url:
            if hasattr(self.out_side_download_url, 'to_alipay_dict'):
                params['out_side_download_url'] = self.out_side_download_url.to_alipay_dict()
            else:
                params['out_side_download_url'] = self.out_side_download_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceData()
        if 'buyer_invoice_title' in d:
            o.buyer_invoice_title = d['buyer_invoice_title']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_amount_currency' in d:
            o.invoice_amount_currency = d['invoice_amount_currency']
        if 'invoice_apply_date' in d:
            o.invoice_apply_date = d['invoice_apply_date']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_open_date' in d:
            o.invoice_open_date = d['invoice_open_date']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'mail_status' in d:
            o.mail_status = d['mail_status']
        if 'open_api_id' in d:
            o.open_api_id = d['open_api_id']
        if 'out_side_download_url' in d:
            o.out_side_download_url = d['out_side_download_url']
        return o


