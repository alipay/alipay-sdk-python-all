#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceDetail import InvoiceDetail


class PreInvoiceData(object):

    def __init__(self):
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_invoice_title = None
        self._buyer_tax_no = None
        self._buyer_telephone = None
        self._invoice_amount = None
        self._invoice_amount_currency = None
        self._invoice_details = None
        self._invoice_note = None
        self._memo = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_company_name = None
        self._seller_tax_no = None
        self._seller_telephone = None

    @property
    def buyer_address(self):
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, value):
        self._buyer_address = value
    @property
    def buyer_bank_account(self):
        return self._buyer_bank_account

    @buyer_bank_account.setter
    def buyer_bank_account(self, value):
        self._buyer_bank_account = value
    @property
    def buyer_bank_name(self):
        return self._buyer_bank_name

    @buyer_bank_name.setter
    def buyer_bank_name(self, value):
        self._buyer_bank_name = value
    @property
    def buyer_invoice_title(self):
        return self._buyer_invoice_title

    @buyer_invoice_title.setter
    def buyer_invoice_title(self, value):
        self._buyer_invoice_title = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def buyer_telephone(self):
        return self._buyer_telephone

    @buyer_telephone.setter
    def buyer_telephone(self, value):
        self._buyer_telephone = value
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
    def invoice_details(self):
        return self._invoice_details

    @invoice_details.setter
    def invoice_details(self, value):
        if isinstance(value, list):
            self._invoice_details = list()
            for i in value:
                if isinstance(i, InvoiceDetail):
                    self._invoice_details.append(i)
                else:
                    self._invoice_details.append(InvoiceDetail.from_alipay_dict(i))
    @property
    def invoice_note(self):
        return self._invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self._invoice_note = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def seller_address(self):
        return self._seller_address

    @seller_address.setter
    def seller_address(self, value):
        self._seller_address = value
    @property
    def seller_bank_account(self):
        return self._seller_bank_account

    @seller_bank_account.setter
    def seller_bank_account(self, value):
        self._seller_bank_account = value
    @property
    def seller_bank_name(self):
        return self._seller_bank_name

    @seller_bank_name.setter
    def seller_bank_name(self, value):
        self._seller_bank_name = value
    @property
    def seller_company_name(self):
        return self._seller_company_name

    @seller_company_name.setter
    def seller_company_name(self, value):
        self._seller_company_name = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value
    @property
    def seller_telephone(self):
        return self._seller_telephone

    @seller_telephone.setter
    def seller_telephone(self, value):
        self._seller_telephone = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_address:
            if hasattr(self.buyer_address, 'to_alipay_dict'):
                params['buyer_address'] = self.buyer_address.to_alipay_dict()
            else:
                params['buyer_address'] = self.buyer_address
        if self.buyer_bank_account:
            if hasattr(self.buyer_bank_account, 'to_alipay_dict'):
                params['buyer_bank_account'] = self.buyer_bank_account.to_alipay_dict()
            else:
                params['buyer_bank_account'] = self.buyer_bank_account
        if self.buyer_bank_name:
            if hasattr(self.buyer_bank_name, 'to_alipay_dict'):
                params['buyer_bank_name'] = self.buyer_bank_name.to_alipay_dict()
            else:
                params['buyer_bank_name'] = self.buyer_bank_name
        if self.buyer_invoice_title:
            if hasattr(self.buyer_invoice_title, 'to_alipay_dict'):
                params['buyer_invoice_title'] = self.buyer_invoice_title.to_alipay_dict()
            else:
                params['buyer_invoice_title'] = self.buyer_invoice_title
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.buyer_telephone:
            if hasattr(self.buyer_telephone, 'to_alipay_dict'):
                params['buyer_telephone'] = self.buyer_telephone.to_alipay_dict()
            else:
                params['buyer_telephone'] = self.buyer_telephone
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
        if self.invoice_details:
            if isinstance(self.invoice_details, list):
                for i in range(0, len(self.invoice_details)):
                    element = self.invoice_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_details[i] = element.to_alipay_dict()
            if hasattr(self.invoice_details, 'to_alipay_dict'):
                params['invoice_details'] = self.invoice_details.to_alipay_dict()
            else:
                params['invoice_details'] = self.invoice_details
        if self.invoice_note:
            if hasattr(self.invoice_note, 'to_alipay_dict'):
                params['invoice_note'] = self.invoice_note.to_alipay_dict()
            else:
                params['invoice_note'] = self.invoice_note
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.seller_address:
            if hasattr(self.seller_address, 'to_alipay_dict'):
                params['seller_address'] = self.seller_address.to_alipay_dict()
            else:
                params['seller_address'] = self.seller_address
        if self.seller_bank_account:
            if hasattr(self.seller_bank_account, 'to_alipay_dict'):
                params['seller_bank_account'] = self.seller_bank_account.to_alipay_dict()
            else:
                params['seller_bank_account'] = self.seller_bank_account
        if self.seller_bank_name:
            if hasattr(self.seller_bank_name, 'to_alipay_dict'):
                params['seller_bank_name'] = self.seller_bank_name.to_alipay_dict()
            else:
                params['seller_bank_name'] = self.seller_bank_name
        if self.seller_company_name:
            if hasattr(self.seller_company_name, 'to_alipay_dict'):
                params['seller_company_name'] = self.seller_company_name.to_alipay_dict()
            else:
                params['seller_company_name'] = self.seller_company_name
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = self.seller_tax_no.to_alipay_dict()
            else:
                params['seller_tax_no'] = self.seller_tax_no
        if self.seller_telephone:
            if hasattr(self.seller_telephone, 'to_alipay_dict'):
                params['seller_telephone'] = self.seller_telephone.to_alipay_dict()
            else:
                params['seller_telephone'] = self.seller_telephone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PreInvoiceData()
        if 'buyer_address' in d:
            o.buyer_address = d['buyer_address']
        if 'buyer_bank_account' in d:
            o.buyer_bank_account = d['buyer_bank_account']
        if 'buyer_bank_name' in d:
            o.buyer_bank_name = d['buyer_bank_name']
        if 'buyer_invoice_title' in d:
            o.buyer_invoice_title = d['buyer_invoice_title']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'buyer_telephone' in d:
            o.buyer_telephone = d['buyer_telephone']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_amount_currency' in d:
            o.invoice_amount_currency = d['invoice_amount_currency']
        if 'invoice_details' in d:
            o.invoice_details = d['invoice_details']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'memo' in d:
            o.memo = d['memo']
        if 'seller_address' in d:
            o.seller_address = d['seller_address']
        if 'seller_bank_account' in d:
            o.seller_bank_account = d['seller_bank_account']
        if 'seller_bank_name' in d:
            o.seller_bank_name = d['seller_bank_name']
        if 'seller_company_name' in d:
            o.seller_company_name = d['seller_company_name']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'seller_telephone' in d:
            o.seller_telephone = d['seller_telephone']
        return o


