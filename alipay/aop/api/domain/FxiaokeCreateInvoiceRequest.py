#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FxiaoInvoiceDetail import FxiaoInvoiceDetail


class FxiaokeCreateInvoiceRequest(object):

    def __init__(self):
        self._email_attachments = None
        self._first_year_warranty_end_date = None
        self._first_year_warranty_start_date = None
        self._fxiao_invoice_detail = None
        self._general_agency_order_no = None
        self._invoice_owner = None
        self._name = None
        self._quotation_no = None

    @property
    def email_attachments(self):
        return self._email_attachments

    @email_attachments.setter
    def email_attachments(self, value):
        self._email_attachments = value
    @property
    def first_year_warranty_end_date(self):
        return self._first_year_warranty_end_date

    @first_year_warranty_end_date.setter
    def first_year_warranty_end_date(self, value):
        self._first_year_warranty_end_date = value
    @property
    def first_year_warranty_start_date(self):
        return self._first_year_warranty_start_date

    @first_year_warranty_start_date.setter
    def first_year_warranty_start_date(self, value):
        self._first_year_warranty_start_date = value
    @property
    def fxiao_invoice_detail(self):
        return self._fxiao_invoice_detail

    @fxiao_invoice_detail.setter
    def fxiao_invoice_detail(self, value):
        if isinstance(value, list):
            self._fxiao_invoice_detail = list()
            for i in value:
                if isinstance(i, FxiaoInvoiceDetail):
                    self._fxiao_invoice_detail.append(i)
                else:
                    self._fxiao_invoice_detail.append(FxiaoInvoiceDetail.from_alipay_dict(i))
    @property
    def general_agency_order_no(self):
        return self._general_agency_order_no

    @general_agency_order_no.setter
    def general_agency_order_no(self, value):
        self._general_agency_order_no = value
    @property
    def invoice_owner(self):
        return self._invoice_owner

    @invoice_owner.setter
    def invoice_owner(self, value):
        self._invoice_owner = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def quotation_no(self):
        return self._quotation_no

    @quotation_no.setter
    def quotation_no(self, value):
        self._quotation_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.email_attachments:
            if hasattr(self.email_attachments, 'to_alipay_dict'):
                params['email_attachments'] = self.email_attachments.to_alipay_dict()
            else:
                params['email_attachments'] = self.email_attachments
        if self.first_year_warranty_end_date:
            if hasattr(self.first_year_warranty_end_date, 'to_alipay_dict'):
                params['first_year_warranty_end_date'] = self.first_year_warranty_end_date.to_alipay_dict()
            else:
                params['first_year_warranty_end_date'] = self.first_year_warranty_end_date
        if self.first_year_warranty_start_date:
            if hasattr(self.first_year_warranty_start_date, 'to_alipay_dict'):
                params['first_year_warranty_start_date'] = self.first_year_warranty_start_date.to_alipay_dict()
            else:
                params['first_year_warranty_start_date'] = self.first_year_warranty_start_date
        if self.fxiao_invoice_detail:
            if isinstance(self.fxiao_invoice_detail, list):
                for i in range(0, len(self.fxiao_invoice_detail)):
                    element = self.fxiao_invoice_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fxiao_invoice_detail[i] = element.to_alipay_dict()
            if hasattr(self.fxiao_invoice_detail, 'to_alipay_dict'):
                params['fxiao_invoice_detail'] = self.fxiao_invoice_detail.to_alipay_dict()
            else:
                params['fxiao_invoice_detail'] = self.fxiao_invoice_detail
        if self.general_agency_order_no:
            if hasattr(self.general_agency_order_no, 'to_alipay_dict'):
                params['general_agency_order_no'] = self.general_agency_order_no.to_alipay_dict()
            else:
                params['general_agency_order_no'] = self.general_agency_order_no
        if self.invoice_owner:
            if hasattr(self.invoice_owner, 'to_alipay_dict'):
                params['invoice_owner'] = self.invoice_owner.to_alipay_dict()
            else:
                params['invoice_owner'] = self.invoice_owner
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.quotation_no:
            if hasattr(self.quotation_no, 'to_alipay_dict'):
                params['quotation_no'] = self.quotation_no.to_alipay_dict()
            else:
                params['quotation_no'] = self.quotation_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FxiaokeCreateInvoiceRequest()
        if 'email_attachments' in d:
            o.email_attachments = d['email_attachments']
        if 'first_year_warranty_end_date' in d:
            o.first_year_warranty_end_date = d['first_year_warranty_end_date']
        if 'first_year_warranty_start_date' in d:
            o.first_year_warranty_start_date = d['first_year_warranty_start_date']
        if 'fxiao_invoice_detail' in d:
            o.fxiao_invoice_detail = d['fxiao_invoice_detail']
        if 'general_agency_order_no' in d:
            o.general_agency_order_no = d['general_agency_order_no']
        if 'invoice_owner' in d:
            o.invoice_owner = d['invoice_owner']
        if 'name' in d:
            o.name = d['name']
        if 'quotation_no' in d:
            o.quotation_no = d['quotation_no']
        return o


