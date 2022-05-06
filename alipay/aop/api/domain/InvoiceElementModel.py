#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EinvTrade import EinvTrade


class InvoiceElementModel(object):

    def __init__(self):
        self._expense_status = None
        self._extend_fields = None
        self._fake_code = None
        self._has_pdf_file = None
        self._has_risk = None
        self._invoice_amount = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_img_url = None
        self._invoice_kind = None
        self._invoice_no = None
        self._invoice_status = None
        self._isv_contact = None
        self._isv_name = None
        self._logo_url = None
        self._m_name = None
        self._out_tax_amount = None
        self._payee_name = None
        self._payee_tax_no = None
        self._payer_name = None
        self._payer_tax_no = None
        self._pdf_url = None
        self._source = None
        self._trade_list = None
        self._trade_match_result = None

    @property
    def expense_status(self):
        return self._expense_status

    @expense_status.setter
    def expense_status(self, value):
        self._expense_status = value
    @property
    def extend_fields(self):
        return self._extend_fields

    @extend_fields.setter
    def extend_fields(self, value):
        self._extend_fields = value
    @property
    def fake_code(self):
        return self._fake_code

    @fake_code.setter
    def fake_code(self, value):
        self._fake_code = value
    @property
    def has_pdf_file(self):
        return self._has_pdf_file

    @has_pdf_file.setter
    def has_pdf_file(self, value):
        self._has_pdf_file = value
    @property
    def has_risk(self):
        return self._has_risk

    @has_risk.setter
    def has_risk(self, value):
        self._has_risk = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
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
    def invoice_img_url(self):
        return self._invoice_img_url

    @invoice_img_url.setter
    def invoice_img_url(self, value):
        self._invoice_img_url = value
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
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
    def isv_contact(self):
        return self._isv_contact

    @isv_contact.setter
    def isv_contact(self, value):
        self._isv_contact = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def m_name(self):
        return self._m_name

    @m_name.setter
    def m_name(self, value):
        self._m_name = value
    @property
    def out_tax_amount(self):
        return self._out_tax_amount

    @out_tax_amount.setter
    def out_tax_amount(self, value):
        self._out_tax_amount = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payee_tax_no(self):
        return self._payee_tax_no

    @payee_tax_no.setter
    def payee_tax_no(self, value):
        self._payee_tax_no = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def payer_tax_no(self):
        return self._payer_tax_no

    @payer_tax_no.setter
    def payer_tax_no(self, value):
        self._payer_tax_no = value
    @property
    def pdf_url(self):
        return self._pdf_url

    @pdf_url.setter
    def pdf_url(self, value):
        self._pdf_url = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def trade_list(self):
        return self._trade_list

    @trade_list.setter
    def trade_list(self, value):
        if isinstance(value, list):
            self._trade_list = list()
            for i in value:
                if isinstance(i, EinvTrade):
                    self._trade_list.append(i)
                else:
                    self._trade_list.append(EinvTrade.from_alipay_dict(i))
    @property
    def trade_match_result(self):
        return self._trade_match_result

    @trade_match_result.setter
    def trade_match_result(self, value):
        self._trade_match_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.expense_status:
            if hasattr(self.expense_status, 'to_alipay_dict'):
                params['expense_status'] = self.expense_status.to_alipay_dict()
            else:
                params['expense_status'] = self.expense_status
        if self.extend_fields:
            if hasattr(self.extend_fields, 'to_alipay_dict'):
                params['extend_fields'] = self.extend_fields.to_alipay_dict()
            else:
                params['extend_fields'] = self.extend_fields
        if self.fake_code:
            if hasattr(self.fake_code, 'to_alipay_dict'):
                params['fake_code'] = self.fake_code.to_alipay_dict()
            else:
                params['fake_code'] = self.fake_code
        if self.has_pdf_file:
            if hasattr(self.has_pdf_file, 'to_alipay_dict'):
                params['has_pdf_file'] = self.has_pdf_file.to_alipay_dict()
            else:
                params['has_pdf_file'] = self.has_pdf_file
        if self.has_risk:
            if hasattr(self.has_risk, 'to_alipay_dict'):
                params['has_risk'] = self.has_risk.to_alipay_dict()
            else:
                params['has_risk'] = self.has_risk
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
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
        if self.invoice_img_url:
            if hasattr(self.invoice_img_url, 'to_alipay_dict'):
                params['invoice_img_url'] = self.invoice_img_url.to_alipay_dict()
            else:
                params['invoice_img_url'] = self.invoice_img_url
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
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
        if self.isv_contact:
            if hasattr(self.isv_contact, 'to_alipay_dict'):
                params['isv_contact'] = self.isv_contact.to_alipay_dict()
            else:
                params['isv_contact'] = self.isv_contact
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.m_name:
            if hasattr(self.m_name, 'to_alipay_dict'):
                params['m_name'] = self.m_name.to_alipay_dict()
            else:
                params['m_name'] = self.m_name
        if self.out_tax_amount:
            if hasattr(self.out_tax_amount, 'to_alipay_dict'):
                params['out_tax_amount'] = self.out_tax_amount.to_alipay_dict()
            else:
                params['out_tax_amount'] = self.out_tax_amount
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payee_tax_no:
            if hasattr(self.payee_tax_no, 'to_alipay_dict'):
                params['payee_tax_no'] = self.payee_tax_no.to_alipay_dict()
            else:
                params['payee_tax_no'] = self.payee_tax_no
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.payer_tax_no:
            if hasattr(self.payer_tax_no, 'to_alipay_dict'):
                params['payer_tax_no'] = self.payer_tax_no.to_alipay_dict()
            else:
                params['payer_tax_no'] = self.payer_tax_no
        if self.pdf_url:
            if hasattr(self.pdf_url, 'to_alipay_dict'):
                params['pdf_url'] = self.pdf_url.to_alipay_dict()
            else:
                params['pdf_url'] = self.pdf_url
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.trade_list:
            if isinstance(self.trade_list, list):
                for i in range(0, len(self.trade_list)):
                    element = self.trade_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_list, 'to_alipay_dict'):
                params['trade_list'] = self.trade_list.to_alipay_dict()
            else:
                params['trade_list'] = self.trade_list
        if self.trade_match_result:
            if hasattr(self.trade_match_result, 'to_alipay_dict'):
                params['trade_match_result'] = self.trade_match_result.to_alipay_dict()
            else:
                params['trade_match_result'] = self.trade_match_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceElementModel()
        if 'expense_status' in d:
            o.expense_status = d['expense_status']
        if 'extend_fields' in d:
            o.extend_fields = d['extend_fields']
        if 'fake_code' in d:
            o.fake_code = d['fake_code']
        if 'has_pdf_file' in d:
            o.has_pdf_file = d['has_pdf_file']
        if 'has_risk' in d:
            o.has_risk = d['has_risk']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_img_url' in d:
            o.invoice_img_url = d['invoice_img_url']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'isv_contact' in d:
            o.isv_contact = d['isv_contact']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'm_name' in d:
            o.m_name = d['m_name']
        if 'out_tax_amount' in d:
            o.out_tax_amount = d['out_tax_amount']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payee_tax_no' in d:
            o.payee_tax_no = d['payee_tax_no']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'payer_tax_no' in d:
            o.payer_tax_no = d['payer_tax_no']
        if 'pdf_url' in d:
            o.pdf_url = d['pdf_url']
        if 'source' in d:
            o.source = d['source']
        if 'trade_list' in d:
            o.trade_list = d['trade_list']
        if 'trade_match_result' in d:
            o.trade_match_result = d['trade_match_result']
        return o


