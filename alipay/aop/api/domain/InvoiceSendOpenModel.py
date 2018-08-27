#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceItemOpenModel import InvoiceItemOpenModel
from alipay.aop.api.domain.InvoiceTitleOpenModel import InvoiceTitleOpenModel


class InvoiceSendOpenModel(object):

    def __init__(self):
        self._apply_id = None
        self._check_code = None
        self._checker = None
        self._clerk = None
        self._ex_tax_amount = None
        self._extend_fields = None
        self._file_download_type = None
        self._file_download_url = None
        self._invoice_code = None
        self._invoice_content = None
        self._invoice_date = None
        self._invoice_kind = None
        self._invoice_memo = None
        self._invoice_no = None
        self._invoice_title = None
        self._invoice_type = None
        self._ori_blue_inv_code = None
        self._ori_blue_inv_no = None
        self._out_invoice_id = None
        self._out_trade_no = None
        self._payee = None
        self._payee_address_tel = None
        self._payee_bank_name_account = None
        self._payee_register_name = None
        self._payee_register_no = None
        self._sum_amount = None
        self._tax_amount = None
        self._user_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def checker(self):
        return self._checker

    @checker.setter
    def checker(self, value):
        self._checker = value
    @property
    def clerk(self):
        return self._clerk

    @clerk.setter
    def clerk(self, value):
        self._clerk = value
    @property
    def ex_tax_amount(self):
        return self._ex_tax_amount

    @ex_tax_amount.setter
    def ex_tax_amount(self, value):
        self._ex_tax_amount = value
    @property
    def extend_fields(self):
        return self._extend_fields

    @extend_fields.setter
    def extend_fields(self, value):
        self._extend_fields = value
    @property
    def file_download_type(self):
        return self._file_download_type

    @file_download_type.setter
    def file_download_type(self, value):
        self._file_download_type = value
    @property
    def file_download_url(self):
        return self._file_download_url

    @file_download_url.setter
    def file_download_url(self, value):
        self._file_download_url = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_content(self):
        return self._invoice_content

    @invoice_content.setter
    def invoice_content(self, value):
        if isinstance(value, list):
            self._invoice_content = list()
            for i in value:
                if isinstance(i, InvoiceItemOpenModel):
                    self._invoice_content.append(i)
                else:
                    self._invoice_content.append(InvoiceItemOpenModel.from_alipay_dict(i))
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
    def invoice_title(self):
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, value):
        if isinstance(value, InvoiceTitleOpenModel):
            self._invoice_title = value
        else:
            self._invoice_title = InvoiceTitleOpenModel.from_alipay_dict(value)
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def ori_blue_inv_code(self):
        return self._ori_blue_inv_code

    @ori_blue_inv_code.setter
    def ori_blue_inv_code(self, value):
        self._ori_blue_inv_code = value
    @property
    def ori_blue_inv_no(self):
        return self._ori_blue_inv_no

    @ori_blue_inv_no.setter
    def ori_blue_inv_no(self, value):
        self._ori_blue_inv_no = value
    @property
    def out_invoice_id(self):
        return self._out_invoice_id

    @out_invoice_id.setter
    def out_invoice_id(self, value):
        self._out_invoice_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
    @property
    def payee_address_tel(self):
        return self._payee_address_tel

    @payee_address_tel.setter
    def payee_address_tel(self, value):
        self._payee_address_tel = value
    @property
    def payee_bank_name_account(self):
        return self._payee_bank_name_account

    @payee_bank_name_account.setter
    def payee_bank_name_account(self, value):
        self._payee_bank_name_account = value
    @property
    def payee_register_name(self):
        return self._payee_register_name

    @payee_register_name.setter
    def payee_register_name(self, value):
        self._payee_register_name = value
    @property
    def payee_register_no(self):
        return self._payee_register_no

    @payee_register_no.setter
    def payee_register_no(self, value):
        self._payee_register_no = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.checker:
            if hasattr(self.checker, 'to_alipay_dict'):
                params['checker'] = self.checker.to_alipay_dict()
            else:
                params['checker'] = self.checker
        if self.clerk:
            if hasattr(self.clerk, 'to_alipay_dict'):
                params['clerk'] = self.clerk.to_alipay_dict()
            else:
                params['clerk'] = self.clerk
        if self.ex_tax_amount:
            if hasattr(self.ex_tax_amount, 'to_alipay_dict'):
                params['ex_tax_amount'] = self.ex_tax_amount.to_alipay_dict()
            else:
                params['ex_tax_amount'] = self.ex_tax_amount
        if self.extend_fields:
            if hasattr(self.extend_fields, 'to_alipay_dict'):
                params['extend_fields'] = self.extend_fields.to_alipay_dict()
            else:
                params['extend_fields'] = self.extend_fields
        if self.file_download_type:
            if hasattr(self.file_download_type, 'to_alipay_dict'):
                params['file_download_type'] = self.file_download_type.to_alipay_dict()
            else:
                params['file_download_type'] = self.file_download_type
        if self.file_download_url:
            if hasattr(self.file_download_url, 'to_alipay_dict'):
                params['file_download_url'] = self.file_download_url.to_alipay_dict()
            else:
                params['file_download_url'] = self.file_download_url
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_content:
            if isinstance(self.invoice_content, list):
                for i in range(0, len(self.invoice_content)):
                    element = self.invoice_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_content[i] = element.to_alipay_dict()
            if hasattr(self.invoice_content, 'to_alipay_dict'):
                params['invoice_content'] = self.invoice_content.to_alipay_dict()
            else:
                params['invoice_content'] = self.invoice_content
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
        if self.ori_blue_inv_code:
            if hasattr(self.ori_blue_inv_code, 'to_alipay_dict'):
                params['ori_blue_inv_code'] = self.ori_blue_inv_code.to_alipay_dict()
            else:
                params['ori_blue_inv_code'] = self.ori_blue_inv_code
        if self.ori_blue_inv_no:
            if hasattr(self.ori_blue_inv_no, 'to_alipay_dict'):
                params['ori_blue_inv_no'] = self.ori_blue_inv_no.to_alipay_dict()
            else:
                params['ori_blue_inv_no'] = self.ori_blue_inv_no
        if self.out_invoice_id:
            if hasattr(self.out_invoice_id, 'to_alipay_dict'):
                params['out_invoice_id'] = self.out_invoice_id.to_alipay_dict()
            else:
                params['out_invoice_id'] = self.out_invoice_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.payee_address_tel:
            if hasattr(self.payee_address_tel, 'to_alipay_dict'):
                params['payee_address_tel'] = self.payee_address_tel.to_alipay_dict()
            else:
                params['payee_address_tel'] = self.payee_address_tel
        if self.payee_bank_name_account:
            if hasattr(self.payee_bank_name_account, 'to_alipay_dict'):
                params['payee_bank_name_account'] = self.payee_bank_name_account.to_alipay_dict()
            else:
                params['payee_bank_name_account'] = self.payee_bank_name_account
        if self.payee_register_name:
            if hasattr(self.payee_register_name, 'to_alipay_dict'):
                params['payee_register_name'] = self.payee_register_name.to_alipay_dict()
            else:
                params['payee_register_name'] = self.payee_register_name
        if self.payee_register_no:
            if hasattr(self.payee_register_no, 'to_alipay_dict'):
                params['payee_register_no'] = self.payee_register_no.to_alipay_dict()
            else:
                params['payee_register_no'] = self.payee_register_no
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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceSendOpenModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'checker' in d:
            o.checker = d['checker']
        if 'clerk' in d:
            o.clerk = d['clerk']
        if 'ex_tax_amount' in d:
            o.ex_tax_amount = d['ex_tax_amount']
        if 'extend_fields' in d:
            o.extend_fields = d['extend_fields']
        if 'file_download_type' in d:
            o.file_download_type = d['file_download_type']
        if 'file_download_url' in d:
            o.file_download_url = d['file_download_url']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_content' in d:
            o.invoice_content = d['invoice_content']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_memo' in d:
            o.invoice_memo = d['invoice_memo']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'ori_blue_inv_code' in d:
            o.ori_blue_inv_code = d['ori_blue_inv_code']
        if 'ori_blue_inv_no' in d:
            o.ori_blue_inv_no = d['ori_blue_inv_no']
        if 'out_invoice_id' in d:
            o.out_invoice_id = d['out_invoice_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'payee' in d:
            o.payee = d['payee']
        if 'payee_address_tel' in d:
            o.payee_address_tel = d['payee_address_tel']
        if 'payee_bank_name_account' in d:
            o.payee_bank_name_account = d['payee_bank_name_account']
        if 'payee_register_name' in d:
            o.payee_register_name = d['payee_register_name']
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'sum_amount' in d:
            o.sum_amount = d['sum_amount']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


