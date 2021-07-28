#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceItemApplyOpenModel import InvoiceItemApplyOpenModel
from alipay.aop.api.domain.InvoiceTitleApplyOpenModel import InvoiceTitleApplyOpenModel


class InvoiceApplyOpenModel(object):

    def __init__(self):
        self._checker = None
        self._clerk = None
        self._ex_tax_amount = None
        self._invoice_amount = None
        self._invoice_content = None
        self._invoice_kind = None
        self._invoice_memo = None
        self._invoice_title = None
        self._ori_blue_inv_code = None
        self._ori_blue_inv_no = None
        self._out_apply_id = None
        self._out_extends = None
        self._out_trade_no = None
        self._payee = None
        self._payee_address = None
        self._payee_bank_account = None
        self._payee_bank_name = None
        self._payee_register_name = None
        self._payee_register_no = None
        self._payee_tel = None
        self._payer_contact_email = None
        self._payer_contact_mobile = None
        self._sum_tax_amount = None
        self._tax_token = None
        self._trade_date = None

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
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def invoice_content(self):
        return self._invoice_content

    @invoice_content.setter
    def invoice_content(self, value):
        if isinstance(value, list):
            self._invoice_content = list()
            for i in value:
                if isinstance(i, InvoiceItemApplyOpenModel):
                    self._invoice_content.append(i)
                else:
                    self._invoice_content.append(InvoiceItemApplyOpenModel.from_alipay_dict(i))
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
    def invoice_title(self):
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, value):
        if isinstance(value, InvoiceTitleApplyOpenModel):
            self._invoice_title = value
        else:
            self._invoice_title = InvoiceTitleApplyOpenModel.from_alipay_dict(value)
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
    def out_apply_id(self):
        return self._out_apply_id

    @out_apply_id.setter
    def out_apply_id(self, value):
        self._out_apply_id = value
    @property
    def out_extends(self):
        return self._out_extends

    @out_extends.setter
    def out_extends(self, value):
        self._out_extends = value
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
    def payee_tel(self):
        return self._payee_tel

    @payee_tel.setter
    def payee_tel(self, value):
        self._payee_tel = value
    @property
    def payer_contact_email(self):
        return self._payer_contact_email

    @payer_contact_email.setter
    def payer_contact_email(self, value):
        self._payer_contact_email = value
    @property
    def payer_contact_mobile(self):
        return self._payer_contact_mobile

    @payer_contact_mobile.setter
    def payer_contact_mobile(self, value):
        self._payer_contact_mobile = value
    @property
    def sum_tax_amount(self):
        return self._sum_tax_amount

    @sum_tax_amount.setter
    def sum_tax_amount(self, value):
        self._sum_tax_amount = value
    @property
    def tax_token(self):
        return self._tax_token

    @tax_token.setter
    def tax_token(self, value):
        self._tax_token = value
    @property
    def trade_date(self):
        return self._trade_date

    @trade_date.setter
    def trade_date(self, value):
        self._trade_date = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
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
        if self.invoice_title:
            if hasattr(self.invoice_title, 'to_alipay_dict'):
                params['invoice_title'] = self.invoice_title.to_alipay_dict()
            else:
                params['invoice_title'] = self.invoice_title
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
        if self.out_apply_id:
            if hasattr(self.out_apply_id, 'to_alipay_dict'):
                params['out_apply_id'] = self.out_apply_id.to_alipay_dict()
            else:
                params['out_apply_id'] = self.out_apply_id
        if self.out_extends:
            if hasattr(self.out_extends, 'to_alipay_dict'):
                params['out_extends'] = self.out_extends.to_alipay_dict()
            else:
                params['out_extends'] = self.out_extends
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
        if self.payee_tel:
            if hasattr(self.payee_tel, 'to_alipay_dict'):
                params['payee_tel'] = self.payee_tel.to_alipay_dict()
            else:
                params['payee_tel'] = self.payee_tel
        if self.payer_contact_email:
            if hasattr(self.payer_contact_email, 'to_alipay_dict'):
                params['payer_contact_email'] = self.payer_contact_email.to_alipay_dict()
            else:
                params['payer_contact_email'] = self.payer_contact_email
        if self.payer_contact_mobile:
            if hasattr(self.payer_contact_mobile, 'to_alipay_dict'):
                params['payer_contact_mobile'] = self.payer_contact_mobile.to_alipay_dict()
            else:
                params['payer_contact_mobile'] = self.payer_contact_mobile
        if self.sum_tax_amount:
            if hasattr(self.sum_tax_amount, 'to_alipay_dict'):
                params['sum_tax_amount'] = self.sum_tax_amount.to_alipay_dict()
            else:
                params['sum_tax_amount'] = self.sum_tax_amount
        if self.tax_token:
            if hasattr(self.tax_token, 'to_alipay_dict'):
                params['tax_token'] = self.tax_token.to_alipay_dict()
            else:
                params['tax_token'] = self.tax_token
        if self.trade_date:
            if hasattr(self.trade_date, 'to_alipay_dict'):
                params['trade_date'] = self.trade_date.to_alipay_dict()
            else:
                params['trade_date'] = self.trade_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceApplyOpenModel()
        if 'checker' in d:
            o.checker = d['checker']
        if 'clerk' in d:
            o.clerk = d['clerk']
        if 'ex_tax_amount' in d:
            o.ex_tax_amount = d['ex_tax_amount']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_content' in d:
            o.invoice_content = d['invoice_content']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_memo' in d:
            o.invoice_memo = d['invoice_memo']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'ori_blue_inv_code' in d:
            o.ori_blue_inv_code = d['ori_blue_inv_code']
        if 'ori_blue_inv_no' in d:
            o.ori_blue_inv_no = d['ori_blue_inv_no']
        if 'out_apply_id' in d:
            o.out_apply_id = d['out_apply_id']
        if 'out_extends' in d:
            o.out_extends = d['out_extends']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'payee' in d:
            o.payee = d['payee']
        if 'payee_address' in d:
            o.payee_address = d['payee_address']
        if 'payee_bank_account' in d:
            o.payee_bank_account = d['payee_bank_account']
        if 'payee_bank_name' in d:
            o.payee_bank_name = d['payee_bank_name']
        if 'payee_register_name' in d:
            o.payee_register_name = d['payee_register_name']
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'payee_tel' in d:
            o.payee_tel = d['payee_tel']
        if 'payer_contact_email' in d:
            o.payer_contact_email = d['payer_contact_email']
        if 'payer_contact_mobile' in d:
            o.payer_contact_mobile = d['payer_contact_mobile']
        if 'sum_tax_amount' in d:
            o.sum_tax_amount = d['sum_tax_amount']
        if 'tax_token' in d:
            o.tax_token = d['tax_token']
        if 'trade_date' in d:
            o.trade_date = d['trade_date']
        return o


