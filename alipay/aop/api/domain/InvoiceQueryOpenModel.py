#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceItemQueryOpenModel import InvoiceItemQueryOpenModel
from alipay.aop.api.domain.InvoiceTitleQueryOpenModel import InvoiceTitleQueryOpenModel


class InvoiceQueryOpenModel(object):

    def __init__(self):
        self._apply_from = None
        self._check_code = None
        self._checker = None
        self._clerk = None
        self._einv_code = None
        self._einv_no = None
        self._ex_tax_amount = None
        self._invoice_amount = None
        self._invoice_content = None
        self._invoice_date = None
        self._invoice_id = None
        self._invoice_kind = None
        self._invoice_memo = None
        self._invoice_title = None
        self._invoice_type = None
        self._m_short_name = None
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
        self._preview_image_url = None
        self._sub_m_short_name = None
        self._sum_tax_amount = None
        self._trade_date = None
        self._user_id = None

    @property
    def apply_from(self):
        return self._apply_from

    @apply_from.setter
    def apply_from(self, value):
        self._apply_from = value
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
    def einv_code(self):
        return self._einv_code

    @einv_code.setter
    def einv_code(self, value):
        self._einv_code = value
    @property
    def einv_no(self):
        return self._einv_no

    @einv_no.setter
    def einv_no(self, value):
        self._einv_no = value
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
                if isinstance(i, InvoiceItemQueryOpenModel):
                    self._invoice_content.append(i)
                else:
                    self._invoice_content.append(InvoiceItemQueryOpenModel.from_alipay_dict(i))
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
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
        if isinstance(value, InvoiceTitleQueryOpenModel):
            self._invoice_title = value
        else:
            self._invoice_title = InvoiceTitleQueryOpenModel.from_alipay_dict(value)
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value
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
    def preview_image_url(self):
        return self._preview_image_url

    @preview_image_url.setter
    def preview_image_url(self, value):
        self._preview_image_url = value
    @property
    def sub_m_short_name(self):
        return self._sub_m_short_name

    @sub_m_short_name.setter
    def sub_m_short_name(self, value):
        self._sub_m_short_name = value
    @property
    def sum_tax_amount(self):
        return self._sum_tax_amount

    @sum_tax_amount.setter
    def sum_tax_amount(self, value):
        self._sum_tax_amount = value
    @property
    def trade_date(self):
        return self._trade_date

    @trade_date.setter
    def trade_date(self, value):
        self._trade_date = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_from:
            if hasattr(self.apply_from, 'to_alipay_dict'):
                params['apply_from'] = self.apply_from.to_alipay_dict()
            else:
                params['apply_from'] = self.apply_from
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
        if self.einv_code:
            if hasattr(self.einv_code, 'to_alipay_dict'):
                params['einv_code'] = self.einv_code.to_alipay_dict()
            else:
                params['einv_code'] = self.einv_code
        if self.einv_no:
            if hasattr(self.einv_no, 'to_alipay_dict'):
                params['einv_no'] = self.einv_no.to_alipay_dict()
            else:
                params['einv_no'] = self.einv_no
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
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
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
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
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
        if self.preview_image_url:
            if hasattr(self.preview_image_url, 'to_alipay_dict'):
                params['preview_image_url'] = self.preview_image_url.to_alipay_dict()
            else:
                params['preview_image_url'] = self.preview_image_url
        if self.sub_m_short_name:
            if hasattr(self.sub_m_short_name, 'to_alipay_dict'):
                params['sub_m_short_name'] = self.sub_m_short_name.to_alipay_dict()
            else:
                params['sub_m_short_name'] = self.sub_m_short_name
        if self.sum_tax_amount:
            if hasattr(self.sum_tax_amount, 'to_alipay_dict'):
                params['sum_tax_amount'] = self.sum_tax_amount.to_alipay_dict()
            else:
                params['sum_tax_amount'] = self.sum_tax_amount
        if self.trade_date:
            if hasattr(self.trade_date, 'to_alipay_dict'):
                params['trade_date'] = self.trade_date.to_alipay_dict()
            else:
                params['trade_date'] = self.trade_date
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
        o = InvoiceQueryOpenModel()
        if 'apply_from' in d:
            o.apply_from = d['apply_from']
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'checker' in d:
            o.checker = d['checker']
        if 'clerk' in d:
            o.clerk = d['clerk']
        if 'einv_code' in d:
            o.einv_code = d['einv_code']
        if 'einv_no' in d:
            o.einv_no = d['einv_no']
        if 'ex_tax_amount' in d:
            o.ex_tax_amount = d['ex_tax_amount']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_content' in d:
            o.invoice_content = d['invoice_content']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_memo' in d:
            o.invoice_memo = d['invoice_memo']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
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
        if 'preview_image_url' in d:
            o.preview_image_url = d['preview_image_url']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        if 'sum_tax_amount' in d:
            o.sum_tax_amount = d['sum_tax_amount']
        if 'trade_date' in d:
            o.trade_date = d['trade_date']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


