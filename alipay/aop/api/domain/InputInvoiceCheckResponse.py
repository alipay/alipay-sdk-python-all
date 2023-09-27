#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InputInvoiceCheckLine import InputInvoiceCheckLine


class InputInvoiceCheckResponse(object):

    def __init__(self):
        self._buyer_address_phone = None
        self._buyer_bank_info = None
        self._buyer_company_name = None
        self._buyer_ou_code = None
        self._buyer_tax_no = None
        self._cancellation_mark = None
        self._check_code = None
        self._currency = None
        self._drawer = None
        self._full_electronic_flag = None
        self._input_invoice_check_line = None
        self._invoice_amount = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_no = None
        self._invoice_remark = None
        self._invoice_type = None
        self._ofd_url = None
        self._payee = None
        self._pdf_url = None
        self._reviewer = None
        self._seller_address_phone = None
        self._seller_bank_info = None
        self._seller_company_name = None
        self._seller_tax_no = None
        self._task_id = None
        self._tax_amount = None

    @property
    def buyer_address_phone(self):
        return self._buyer_address_phone

    @buyer_address_phone.setter
    def buyer_address_phone(self, value):
        self._buyer_address_phone = value
    @property
    def buyer_bank_info(self):
        return self._buyer_bank_info

    @buyer_bank_info.setter
    def buyer_bank_info(self, value):
        self._buyer_bank_info = value
    @property
    def buyer_company_name(self):
        return self._buyer_company_name

    @buyer_company_name.setter
    def buyer_company_name(self, value):
        self._buyer_company_name = value
    @property
    def buyer_ou_code(self):
        return self._buyer_ou_code

    @buyer_ou_code.setter
    def buyer_ou_code(self, value):
        self._buyer_ou_code = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def cancellation_mark(self):
        return self._cancellation_mark

    @cancellation_mark.setter
    def cancellation_mark(self, value):
        self._cancellation_mark = value
    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def drawer(self):
        return self._drawer

    @drawer.setter
    def drawer(self, value):
        self._drawer = value
    @property
    def full_electronic_flag(self):
        return self._full_electronic_flag

    @full_electronic_flag.setter
    def full_electronic_flag(self, value):
        self._full_electronic_flag = value
    @property
    def input_invoice_check_line(self):
        return self._input_invoice_check_line

    @input_invoice_check_line.setter
    def input_invoice_check_line(self, value):
        if isinstance(value, list):
            self._input_invoice_check_line = list()
            for i in value:
                if isinstance(i, InputInvoiceCheckLine):
                    self._input_invoice_check_line.append(i)
                else:
                    self._input_invoice_check_line.append(InputInvoiceCheckLine.from_alipay_dict(i))
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
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_remark(self):
        return self._invoice_remark

    @invoice_remark.setter
    def invoice_remark(self, value):
        self._invoice_remark = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def ofd_url(self):
        return self._ofd_url

    @ofd_url.setter
    def ofd_url(self, value):
        self._ofd_url = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
    @property
    def pdf_url(self):
        return self._pdf_url

    @pdf_url.setter
    def pdf_url(self, value):
        self._pdf_url = value
    @property
    def reviewer(self):
        return self._reviewer

    @reviewer.setter
    def reviewer(self, value):
        self._reviewer = value
    @property
    def seller_address_phone(self):
        return self._seller_address_phone

    @seller_address_phone.setter
    def seller_address_phone(self, value):
        self._seller_address_phone = value
    @property
    def seller_bank_info(self):
        return self._seller_bank_info

    @seller_bank_info.setter
    def seller_bank_info(self, value):
        self._seller_bank_info = value
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
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_address_phone:
            if hasattr(self.buyer_address_phone, 'to_alipay_dict'):
                params['buyer_address_phone'] = self.buyer_address_phone.to_alipay_dict()
            else:
                params['buyer_address_phone'] = self.buyer_address_phone
        if self.buyer_bank_info:
            if hasattr(self.buyer_bank_info, 'to_alipay_dict'):
                params['buyer_bank_info'] = self.buyer_bank_info.to_alipay_dict()
            else:
                params['buyer_bank_info'] = self.buyer_bank_info
        if self.buyer_company_name:
            if hasattr(self.buyer_company_name, 'to_alipay_dict'):
                params['buyer_company_name'] = self.buyer_company_name.to_alipay_dict()
            else:
                params['buyer_company_name'] = self.buyer_company_name
        if self.buyer_ou_code:
            if hasattr(self.buyer_ou_code, 'to_alipay_dict'):
                params['buyer_ou_code'] = self.buyer_ou_code.to_alipay_dict()
            else:
                params['buyer_ou_code'] = self.buyer_ou_code
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.cancellation_mark:
            if hasattr(self.cancellation_mark, 'to_alipay_dict'):
                params['cancellation_mark'] = self.cancellation_mark.to_alipay_dict()
            else:
                params['cancellation_mark'] = self.cancellation_mark
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.drawer:
            if hasattr(self.drawer, 'to_alipay_dict'):
                params['drawer'] = self.drawer.to_alipay_dict()
            else:
                params['drawer'] = self.drawer
        if self.full_electronic_flag:
            if hasattr(self.full_electronic_flag, 'to_alipay_dict'):
                params['full_electronic_flag'] = self.full_electronic_flag.to_alipay_dict()
            else:
                params['full_electronic_flag'] = self.full_electronic_flag
        if self.input_invoice_check_line:
            if isinstance(self.input_invoice_check_line, list):
                for i in range(0, len(self.input_invoice_check_line)):
                    element = self.input_invoice_check_line[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.input_invoice_check_line[i] = element.to_alipay_dict()
            if hasattr(self.input_invoice_check_line, 'to_alipay_dict'):
                params['input_invoice_check_line'] = self.input_invoice_check_line.to_alipay_dict()
            else:
                params['input_invoice_check_line'] = self.input_invoice_check_line
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
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_remark:
            if hasattr(self.invoice_remark, 'to_alipay_dict'):
                params['invoice_remark'] = self.invoice_remark.to_alipay_dict()
            else:
                params['invoice_remark'] = self.invoice_remark
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.ofd_url:
            if hasattr(self.ofd_url, 'to_alipay_dict'):
                params['ofd_url'] = self.ofd_url.to_alipay_dict()
            else:
                params['ofd_url'] = self.ofd_url
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.pdf_url:
            if hasattr(self.pdf_url, 'to_alipay_dict'):
                params['pdf_url'] = self.pdf_url.to_alipay_dict()
            else:
                params['pdf_url'] = self.pdf_url
        if self.reviewer:
            if hasattr(self.reviewer, 'to_alipay_dict'):
                params['reviewer'] = self.reviewer.to_alipay_dict()
            else:
                params['reviewer'] = self.reviewer
        if self.seller_address_phone:
            if hasattr(self.seller_address_phone, 'to_alipay_dict'):
                params['seller_address_phone'] = self.seller_address_phone.to_alipay_dict()
            else:
                params['seller_address_phone'] = self.seller_address_phone
        if self.seller_bank_info:
            if hasattr(self.seller_bank_info, 'to_alipay_dict'):
                params['seller_bank_info'] = self.seller_bank_info.to_alipay_dict()
            else:
                params['seller_bank_info'] = self.seller_bank_info
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
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceCheckResponse()
        if 'buyer_address_phone' in d:
            o.buyer_address_phone = d['buyer_address_phone']
        if 'buyer_bank_info' in d:
            o.buyer_bank_info = d['buyer_bank_info']
        if 'buyer_company_name' in d:
            o.buyer_company_name = d['buyer_company_name']
        if 'buyer_ou_code' in d:
            o.buyer_ou_code = d['buyer_ou_code']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'cancellation_mark' in d:
            o.cancellation_mark = d['cancellation_mark']
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'currency' in d:
            o.currency = d['currency']
        if 'drawer' in d:
            o.drawer = d['drawer']
        if 'full_electronic_flag' in d:
            o.full_electronic_flag = d['full_electronic_flag']
        if 'input_invoice_check_line' in d:
            o.input_invoice_check_line = d['input_invoice_check_line']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_remark' in d:
            o.invoice_remark = d['invoice_remark']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'ofd_url' in d:
            o.ofd_url = d['ofd_url']
        if 'payee' in d:
            o.payee = d['payee']
        if 'pdf_url' in d:
            o.pdf_url = d['pdf_url']
        if 'reviewer' in d:
            o.reviewer = d['reviewer']
        if 'seller_address_phone' in d:
            o.seller_address_phone = d['seller_address_phone']
        if 'seller_bank_info' in d:
            o.seller_bank_info = d['seller_bank_info']
        if 'seller_company_name' in d:
            o.seller_company_name = d['seller_company_name']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        return o


