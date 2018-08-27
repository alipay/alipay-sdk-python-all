#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceItemContent import InvoiceItemContent


class AlipayEbppInvoiceDetailOutputQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceDetailOutputQueryResponse, self).__init__()
        self._anti_fake_code = None
        self._ex_tax_amount = None
        self._expense_status = None
        self._has_risk = None
        self._has_upload_pdf = None
        self._invoice_amount = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_img_url = None
        self._invoice_item_content_list = None
        self._invoice_no = None
        self._invoice_status = None
        self._invoice_type = None
        self._payee_address = None
        self._payee_bank_account = None
        self._payee_bank_name = None
        self._payee_phone = None
        self._payee_register_name = None
        self._payee_tax_no = None
        self._payer_address = None
        self._payer_bank_account = None
        self._payer_bank_name = None
        self._payer_name = None
        self._payer_phone = None
        self._payer_tax_no = None
        self._sum_tax_amount = None
        self._tax_type = None

    @property
    def anti_fake_code(self):
        return self._anti_fake_code

    @anti_fake_code.setter
    def anti_fake_code(self, value):
        self._anti_fake_code = value
    @property
    def ex_tax_amount(self):
        return self._ex_tax_amount

    @ex_tax_amount.setter
    def ex_tax_amount(self, value):
        self._ex_tax_amount = value
    @property
    def expense_status(self):
        return self._expense_status

    @expense_status.setter
    def expense_status(self, value):
        self._expense_status = value
    @property
    def has_risk(self):
        return self._has_risk

    @has_risk.setter
    def has_risk(self, value):
        self._has_risk = value
    @property
    def has_upload_pdf(self):
        return self._has_upload_pdf

    @has_upload_pdf.setter
    def has_upload_pdf(self, value):
        self._has_upload_pdf = value
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
    def invoice_item_content_list(self):
        return self._invoice_item_content_list

    @invoice_item_content_list.setter
    def invoice_item_content_list(self, value):
        if isinstance(value, list):
            self._invoice_item_content_list = list()
            for i in value:
                if isinstance(i, InvoiceItemContent):
                    self._invoice_item_content_list.append(i)
                else:
                    self._invoice_item_content_list.append(InvoiceItemContent.from_alipay_dict(i))
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
    def payee_address(self):
        return self._payee_address

    @payee_address.setter
    def payee_address(self, value):
        self._payee_address = value
    @property
    def payee_bank_account(self):
        return self._payee_bank_account

    @payee_bank_account.setter
    def payee_bank_account(self, value):
        self._payee_bank_account = value
    @property
    def payee_bank_name(self):
        return self._payee_bank_name

    @payee_bank_name.setter
    def payee_bank_name(self, value):
        self._payee_bank_name = value
    @property
    def payee_phone(self):
        return self._payee_phone

    @payee_phone.setter
    def payee_phone(self, value):
        self._payee_phone = value
    @property
    def payee_register_name(self):
        return self._payee_register_name

    @payee_register_name.setter
    def payee_register_name(self, value):
        self._payee_register_name = value
    @property
    def payee_tax_no(self):
        return self._payee_tax_no

    @payee_tax_no.setter
    def payee_tax_no(self, value):
        self._payee_tax_no = value
    @property
    def payer_address(self):
        return self._payer_address

    @payer_address.setter
    def payer_address(self, value):
        self._payer_address = value
    @property
    def payer_bank_account(self):
        return self._payer_bank_account

    @payer_bank_account.setter
    def payer_bank_account(self, value):
        self._payer_bank_account = value
    @property
    def payer_bank_name(self):
        return self._payer_bank_name

    @payer_bank_name.setter
    def payer_bank_name(self, value):
        self._payer_bank_name = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def payer_phone(self):
        return self._payer_phone

    @payer_phone.setter
    def payer_phone(self, value):
        self._payer_phone = value
    @property
    def payer_tax_no(self):
        return self._payer_tax_no

    @payer_tax_no.setter
    def payer_tax_no(self, value):
        self._payer_tax_no = value
    @property
    def sum_tax_amount(self):
        return self._sum_tax_amount

    @sum_tax_amount.setter
    def sum_tax_amount(self, value):
        self._sum_tax_amount = value
    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, value):
        self._tax_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceDetailOutputQueryResponse, self).parse_response_content(response_content)
        if 'anti_fake_code' in response:
            self.anti_fake_code = response['anti_fake_code']
        if 'ex_tax_amount' in response:
            self.ex_tax_amount = response['ex_tax_amount']
        if 'expense_status' in response:
            self.expense_status = response['expense_status']
        if 'has_risk' in response:
            self.has_risk = response['has_risk']
        if 'has_upload_pdf' in response:
            self.has_upload_pdf = response['has_upload_pdf']
        if 'invoice_amount' in response:
            self.invoice_amount = response['invoice_amount']
        if 'invoice_code' in response:
            self.invoice_code = response['invoice_code']
        if 'invoice_date' in response:
            self.invoice_date = response['invoice_date']
        if 'invoice_img_url' in response:
            self.invoice_img_url = response['invoice_img_url']
        if 'invoice_item_content_list' in response:
            self.invoice_item_content_list = response['invoice_item_content_list']
        if 'invoice_no' in response:
            self.invoice_no = response['invoice_no']
        if 'invoice_status' in response:
            self.invoice_status = response['invoice_status']
        if 'invoice_type' in response:
            self.invoice_type = response['invoice_type']
        if 'payee_address' in response:
            self.payee_address = response['payee_address']
        if 'payee_bank_account' in response:
            self.payee_bank_account = response['payee_bank_account']
        if 'payee_bank_name' in response:
            self.payee_bank_name = response['payee_bank_name']
        if 'payee_phone' in response:
            self.payee_phone = response['payee_phone']
        if 'payee_register_name' in response:
            self.payee_register_name = response['payee_register_name']
        if 'payee_tax_no' in response:
            self.payee_tax_no = response['payee_tax_no']
        if 'payer_address' in response:
            self.payer_address = response['payer_address']
        if 'payer_bank_account' in response:
            self.payer_bank_account = response['payer_bank_account']
        if 'payer_bank_name' in response:
            self.payer_bank_name = response['payer_bank_name']
        if 'payer_name' in response:
            self.payer_name = response['payer_name']
        if 'payer_phone' in response:
            self.payer_phone = response['payer_phone']
        if 'payer_tax_no' in response:
            self.payer_tax_no = response['payer_tax_no']
        if 'sum_tax_amount' in response:
            self.sum_tax_amount = response['sum_tax_amount']
        if 'tax_type' in response:
            self.tax_type = response['tax_type']
