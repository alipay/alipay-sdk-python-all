#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterpriseInvoiceInfoDTO(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.anti_fake_code:
            if hasattr(self.anti_fake_code, 'to_alipay_dict'):
                params['anti_fake_code'] = self.anti_fake_code.to_alipay_dict()
            else:
                params['anti_fake_code'] = self.anti_fake_code
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.checker:
            if hasattr(self.checker, 'to_alipay_dict'):
                params['checker'] = self.checker.to_alipay_dict()
            else:
                params['checker'] = self.checker
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.file_download_url:
            if hasattr(self.file_download_url, 'to_alipay_dict'):
                params['file_download_url'] = self.file_download_url.to_alipay_dict()
            else:
                params['file_download_url'] = self.file_download_url
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.invoice_check_result:
            if hasattr(self.invoice_check_result, 'to_alipay_dict'):
                params['invoice_check_result'] = self.invoice_check_result.to_alipay_dict()
            else:
                params['invoice_check_result'] = self.invoice_check_result
        if self.invoice_check_time:
            if hasattr(self.invoice_check_time, 'to_alipay_dict'):
                params['invoice_check_time'] = self.invoice_check_time.to_alipay_dict()
            else:
                params['invoice_check_time'] = self.invoice_check_time
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
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.invoice_memo:
            if hasattr(self.invoice_memo, 'to_alipay_dict'):
                params['invoice_memo'] = self.invoice_memo.to_alipay_dict()
            else:
                params['invoice_memo'] = self.invoice_memo
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.payee_address:
            if hasattr(self.payee_address, 'to_alipay_dict'):
                params['payee_address'] = self.payee_address.to_alipay_dict()
            else:
                params['payee_address'] = self.payee_address
        if self.payee_bank_account:
            if hasattr(self.payee_bank_account, 'to_alipay_dict'):
                params['payee_bank_account'] = self.payee_bank_account.to_alipay_dict()
            else:
                params['payee_bank_account'] = self.payee_bank_account
        if self.payee_bank_name:
            if hasattr(self.payee_bank_name, 'to_alipay_dict'):
                params['payee_bank_name'] = self.payee_bank_name.to_alipay_dict()
            else:
                params['payee_bank_name'] = self.payee_bank_name
        if self.payee_mobile:
            if hasattr(self.payee_mobile, 'to_alipay_dict'):
                params['payee_mobile'] = self.payee_mobile.to_alipay_dict()
            else:
                params['payee_mobile'] = self.payee_mobile
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payee_register_no:
            if hasattr(self.payee_register_no, 'to_alipay_dict'):
                params['payee_register_no'] = self.payee_register_no.to_alipay_dict()
            else:
                params['payee_register_no'] = self.payee_register_no
        if self.payer_address:
            if hasattr(self.payer_address, 'to_alipay_dict'):
                params['payer_address'] = self.payer_address.to_alipay_dict()
            else:
                params['payer_address'] = self.payer_address
        if self.payer_bank_account:
            if hasattr(self.payer_bank_account, 'to_alipay_dict'):
                params['payer_bank_account'] = self.payer_bank_account.to_alipay_dict()
            else:
                params['payer_bank_account'] = self.payer_bank_account
        if self.payer_bank_name:
            if hasattr(self.payer_bank_name, 'to_alipay_dict'):
                params['payer_bank_name'] = self.payer_bank_name.to_alipay_dict()
            else:
                params['payer_bank_name'] = self.payer_bank_name
        if self.payer_mobile:
            if hasattr(self.payer_mobile, 'to_alipay_dict'):
                params['payer_mobile'] = self.payer_mobile.to_alipay_dict()
            else:
                params['payer_mobile'] = self.payer_mobile
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.payer_register_no:
            if hasattr(self.payer_register_no, 'to_alipay_dict'):
                params['payer_register_no'] = self.payer_register_no.to_alipay_dict()
            else:
                params['payer_register_no'] = self.payer_register_no
        if self.related_to_consume:
            if hasattr(self.related_to_consume, 'to_alipay_dict'):
                params['related_to_consume'] = self.related_to_consume.to_alipay_dict()
            else:
                params['related_to_consume'] = self.related_to_consume
        if self.sum_amount:
            if hasattr(self.sum_amount, 'to_alipay_dict'):
                params['sum_amount'] = self.sum_amount.to_alipay_dict()
            else:
                params['sum_amount'] = self.sum_amount
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.without_tax_amount:
            if hasattr(self.without_tax_amount, 'to_alipay_dict'):
                params['without_tax_amount'] = self.without_tax_amount.to_alipay_dict()
            else:
                params['without_tax_amount'] = self.without_tax_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriseInvoiceInfoDTO()
        if 'anti_fake_code' in d:
            o.anti_fake_code = d['anti_fake_code']
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'checker' in d:
            o.checker = d['checker']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'file_download_url' in d:
            o.file_download_url = d['file_download_url']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'invoice_check_result' in d:
            o.invoice_check_result = d['invoice_check_result']
        if 'invoice_check_time' in d:
            o.invoice_check_time = d['invoice_check_time']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_memo' in d:
            o.invoice_memo = d['invoice_memo']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'operator' in d:
            o.operator = d['operator']
        if 'payee' in d:
            o.payee = d['payee']
        if 'payee_address' in d:
            o.payee_address = d['payee_address']
        if 'payee_bank_account' in d:
            o.payee_bank_account = d['payee_bank_account']
        if 'payee_bank_name' in d:
            o.payee_bank_name = d['payee_bank_name']
        if 'payee_mobile' in d:
            o.payee_mobile = d['payee_mobile']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'payer_address' in d:
            o.payer_address = d['payer_address']
        if 'payer_bank_account' in d:
            o.payer_bank_account = d['payer_bank_account']
        if 'payer_bank_name' in d:
            o.payer_bank_name = d['payer_bank_name']
        if 'payer_mobile' in d:
            o.payer_mobile = d['payer_mobile']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'payer_register_no' in d:
            o.payer_register_no = d['payer_register_no']
        if 'related_to_consume' in d:
            o.related_to_consume = d['related_to_consume']
        if 'sum_amount' in d:
            o.sum_amount = d['sum_amount']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'without_tax_amount' in d:
            o.without_tax_amount = d['without_tax_amount']
        return o


