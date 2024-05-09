#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceEnterpriseInvoiceinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseInvoiceinfoQueryResponse, self).__init__()
        self._anti_fake_code = None
        self._batch_id = None
        self._checker = None
        self._employee_id = None
        self._enterprise_id = None
        self._file_download_url = None
        self._file_type = None
        self._invoice_check_result = None
        self._invoice_check_time = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_kind = None
        self._invoice_memo = None
        self._invoice_no = None
        self._invoice_type = None
        self._operator = None
        self._payee = None
        self._payee_address = None
        self._payee_bank_account = None
        self._payee_bank_name = None
        self._payee_mobile = None
        self._payee_name = None
        self._payee_register_no = None
        self._payer_address = None
        self._payer_bank_account = None
        self._payer_bank_name = None
        self._payer_mobile = None
        self._payer_name = None
        self._payer_register_no = None
        self._related_to_consume = None
        self._sum_amount = None
        self._tax_amount = None
        self._without_tax_amount = None

    @property
    def anti_fake_code(self):
        return self._anti_fake_code

    @anti_fake_code.setter
    def anti_fake_code(self, value):
        self._anti_fake_code = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def checker(self):
        return self._checker

    @checker.setter
    def checker(self, value):
        self._checker = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def file_download_url(self):
        return self._file_download_url

    @file_download_url.setter
    def file_download_url(self, value):
        self._file_download_url = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def invoice_check_result(self):
        return self._invoice_check_result

    @invoice_check_result.setter
    def invoice_check_result(self, value):
        self._invoice_check_result = value
    @property
    def invoice_check_time(self):
        return self._invoice_check_time

    @invoice_check_time.setter
    def invoice_check_time(self, value):
        self._invoice_check_time = value
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
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def invoice_memo(self):
        return self._invoice_memo

    @invoice_memo.setter
    def invoice_memo(self, value):
        self._invoice_memo = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
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
    def payee_mobile(self):
        return self._payee_mobile

    @payee_mobile.setter
    def payee_mobile(self, value):
        self._payee_mobile = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payee_register_no(self):
        return self._payee_register_no

    @payee_register_no.setter
    def payee_register_no(self, value):
        self._payee_register_no = value
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
    def payer_mobile(self):
        return self._payer_mobile

    @payer_mobile.setter
    def payer_mobile(self, value):
        self._payer_mobile = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def payer_register_no(self):
        return self._payer_register_no

    @payer_register_no.setter
    def payer_register_no(self, value):
        self._payer_register_no = value
    @property
    def related_to_consume(self):
        return self._related_to_consume

    @related_to_consume.setter
    def related_to_consume(self, value):
        self._related_to_consume = value
    @property
    def sum_amount(self):
        return self._sum_amount

    @sum_amount.setter
    def sum_amount(self, value):
        self._sum_amount = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def without_tax_amount(self):
        return self._without_tax_amount

    @without_tax_amount.setter
    def without_tax_amount(self, value):
        self._without_tax_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseInvoiceinfoQueryResponse, self).parse_response_content(response_content)
        if 'anti_fake_code' in response:
            self.anti_fake_code = response['anti_fake_code']
        if 'batch_id' in response:
            self.batch_id = response['batch_id']
        if 'checker' in response:
            self.checker = response['checker']
        if 'employee_id' in response:
            self.employee_id = response['employee_id']
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'file_download_url' in response:
            self.file_download_url = response['file_download_url']
        if 'file_type' in response:
            self.file_type = response['file_type']
        if 'invoice_check_result' in response:
            self.invoice_check_result = response['invoice_check_result']
        if 'invoice_check_time' in response:
            self.invoice_check_time = response['invoice_check_time']
        if 'invoice_code' in response:
            self.invoice_code = response['invoice_code']
        if 'invoice_date' in response:
            self.invoice_date = response['invoice_date']
        if 'invoice_kind' in response:
            self.invoice_kind = response['invoice_kind']
        if 'invoice_memo' in response:
            self.invoice_memo = response['invoice_memo']
        if 'invoice_no' in response:
            self.invoice_no = response['invoice_no']
        if 'invoice_type' in response:
            self.invoice_type = response['invoice_type']
        if 'operator' in response:
            self.operator = response['operator']
        if 'payee' in response:
            self.payee = response['payee']
        if 'payee_address' in response:
            self.payee_address = response['payee_address']
        if 'payee_bank_account' in response:
            self.payee_bank_account = response['payee_bank_account']
        if 'payee_bank_name' in response:
            self.payee_bank_name = response['payee_bank_name']
        if 'payee_mobile' in response:
            self.payee_mobile = response['payee_mobile']
        if 'payee_name' in response:
            self.payee_name = response['payee_name']
        if 'payee_register_no' in response:
            self.payee_register_no = response['payee_register_no']
        if 'payer_address' in response:
            self.payer_address = response['payer_address']
        if 'payer_bank_account' in response:
            self.payer_bank_account = response['payer_bank_account']
        if 'payer_bank_name' in response:
            self.payer_bank_name = response['payer_bank_name']
        if 'payer_mobile' in response:
            self.payer_mobile = response['payer_mobile']
        if 'payer_name' in response:
            self.payer_name = response['payer_name']
        if 'payer_register_no' in response:
            self.payer_register_no = response['payer_register_no']
        if 'related_to_consume' in response:
            self.related_to_consume = response['related_to_consume']
        if 'sum_amount' in response:
            self.sum_amount = response['sum_amount']
        if 'tax_amount' in response:
            self.tax_amount = response['tax_amount']
        if 'without_tax_amount' in response:
            self.without_tax_amount = response['without_tax_amount']
