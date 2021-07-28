#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GeneralInvoiceItem import GeneralInvoiceItem


class AlipayEbppInvoiceOpenRedCreateModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._auto_fill_info = None
        self._auto_preprocess = None
        self._invoice_amount = None
        self._invoice_items = None
        self._invoice_kind = None
        self._invoice_memo = None
        self._invoice_type = None
        self._normal_invoice_code = None
        self._normal_invoice_no = None
        self._outer_id = None
        self._payee_address = None
        self._payee_bank_account_id = None
        self._payee_bank_name = None
        self._payee_checker = None
        self._payee_name = None
        self._payee_operator = None
        self._payee_phone = None
        self._payee_receiver = None
        self._payee_register_no = None
        self._payer_address = None
        self._payer_bank_account_id = None
        self._payer_bank_name = None
        self._payer_name = None
        self._payer_phone = None
        self._payer_register_no = None
        self._platform_code = None
        self._platform_user_id = None
        self._product_code = None
        self._sum_price = None
        self._sum_tax = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def auto_fill_info(self):
        return self._auto_fill_info

    @auto_fill_info.setter
    def auto_fill_info(self, value):
        self._auto_fill_info = value
    @property
    def auto_preprocess(self):
        return self._auto_preprocess

    @auto_preprocess.setter
    def auto_preprocess(self, value):
        self._auto_preprocess = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def invoice_items(self):
        return self._invoice_items

    @invoice_items.setter
    def invoice_items(self, value):
        if isinstance(value, list):
            self._invoice_items = list()
            for i in value:
                if isinstance(i, GeneralInvoiceItem):
                    self._invoice_items.append(i)
                else:
                    self._invoice_items.append(GeneralInvoiceItem.from_alipay_dict(i))
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
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def normal_invoice_code(self):
        return self._normal_invoice_code

    @normal_invoice_code.setter
    def normal_invoice_code(self, value):
        self._normal_invoice_code = value
    @property
    def normal_invoice_no(self):
        return self._normal_invoice_no

    @normal_invoice_no.setter
    def normal_invoice_no(self, value):
        self._normal_invoice_no = value
    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, value):
        self._outer_id = value
    @property
    def payee_address(self):
        return self._payee_address

    @payee_address.setter
    def payee_address(self, value):
        self._payee_address = value
    @property
    def payee_bank_account_id(self):
        return self._payee_bank_account_id

    @payee_bank_account_id.setter
    def payee_bank_account_id(self, value):
        self._payee_bank_account_id = value
    @property
    def payee_bank_name(self):
        return self._payee_bank_name

    @payee_bank_name.setter
    def payee_bank_name(self, value):
        self._payee_bank_name = value
    @property
    def payee_checker(self):
        return self._payee_checker

    @payee_checker.setter
    def payee_checker(self, value):
        self._payee_checker = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payee_operator(self):
        return self._payee_operator

    @payee_operator.setter
    def payee_operator(self, value):
        self._payee_operator = value
    @property
    def payee_phone(self):
        return self._payee_phone

    @payee_phone.setter
    def payee_phone(self, value):
        self._payee_phone = value
    @property
    def payee_receiver(self):
        return self._payee_receiver

    @payee_receiver.setter
    def payee_receiver(self, value):
        self._payee_receiver = value
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
    def payer_bank_account_id(self):
        return self._payer_bank_account_id

    @payer_bank_account_id.setter
    def payer_bank_account_id(self, value):
        self._payer_bank_account_id = value
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
    def payer_register_no(self):
        return self._payer_register_no

    @payer_register_no.setter
    def payer_register_no(self, value):
        self._payer_register_no = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def platform_user_id(self):
        return self._platform_user_id

    @platform_user_id.setter
    def platform_user_id(self, value):
        self._platform_user_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sum_price(self):
        return self._sum_price

    @sum_price.setter
    def sum_price(self, value):
        self._sum_price = value
    @property
    def sum_tax(self):
        return self._sum_tax

    @sum_tax.setter
    def sum_tax(self, value):
        self._sum_tax = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.auto_fill_info:
            if hasattr(self.auto_fill_info, 'to_alipay_dict'):
                params['auto_fill_info'] = self.auto_fill_info.to_alipay_dict()
            else:
                params['auto_fill_info'] = self.auto_fill_info
        if self.auto_preprocess:
            if hasattr(self.auto_preprocess, 'to_alipay_dict'):
                params['auto_preprocess'] = self.auto_preprocess.to_alipay_dict()
            else:
                params['auto_preprocess'] = self.auto_preprocess
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.invoice_items:
            if isinstance(self.invoice_items, list):
                for i in range(0, len(self.invoice_items)):
                    element = self.invoice_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_items[i] = element.to_alipay_dict()
            if hasattr(self.invoice_items, 'to_alipay_dict'):
                params['invoice_items'] = self.invoice_items.to_alipay_dict()
            else:
                params['invoice_items'] = self.invoice_items
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
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.normal_invoice_code:
            if hasattr(self.normal_invoice_code, 'to_alipay_dict'):
                params['normal_invoice_code'] = self.normal_invoice_code.to_alipay_dict()
            else:
                params['normal_invoice_code'] = self.normal_invoice_code
        if self.normal_invoice_no:
            if hasattr(self.normal_invoice_no, 'to_alipay_dict'):
                params['normal_invoice_no'] = self.normal_invoice_no.to_alipay_dict()
            else:
                params['normal_invoice_no'] = self.normal_invoice_no
        if self.outer_id:
            if hasattr(self.outer_id, 'to_alipay_dict'):
                params['outer_id'] = self.outer_id.to_alipay_dict()
            else:
                params['outer_id'] = self.outer_id
        if self.payee_address:
            if hasattr(self.payee_address, 'to_alipay_dict'):
                params['payee_address'] = self.payee_address.to_alipay_dict()
            else:
                params['payee_address'] = self.payee_address
        if self.payee_bank_account_id:
            if hasattr(self.payee_bank_account_id, 'to_alipay_dict'):
                params['payee_bank_account_id'] = self.payee_bank_account_id.to_alipay_dict()
            else:
                params['payee_bank_account_id'] = self.payee_bank_account_id
        if self.payee_bank_name:
            if hasattr(self.payee_bank_name, 'to_alipay_dict'):
                params['payee_bank_name'] = self.payee_bank_name.to_alipay_dict()
            else:
                params['payee_bank_name'] = self.payee_bank_name
        if self.payee_checker:
            if hasattr(self.payee_checker, 'to_alipay_dict'):
                params['payee_checker'] = self.payee_checker.to_alipay_dict()
            else:
                params['payee_checker'] = self.payee_checker
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payee_operator:
            if hasattr(self.payee_operator, 'to_alipay_dict'):
                params['payee_operator'] = self.payee_operator.to_alipay_dict()
            else:
                params['payee_operator'] = self.payee_operator
        if self.payee_phone:
            if hasattr(self.payee_phone, 'to_alipay_dict'):
                params['payee_phone'] = self.payee_phone.to_alipay_dict()
            else:
                params['payee_phone'] = self.payee_phone
        if self.payee_receiver:
            if hasattr(self.payee_receiver, 'to_alipay_dict'):
                params['payee_receiver'] = self.payee_receiver.to_alipay_dict()
            else:
                params['payee_receiver'] = self.payee_receiver
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
        if self.payer_bank_account_id:
            if hasattr(self.payer_bank_account_id, 'to_alipay_dict'):
                params['payer_bank_account_id'] = self.payer_bank_account_id.to_alipay_dict()
            else:
                params['payer_bank_account_id'] = self.payer_bank_account_id
        if self.payer_bank_name:
            if hasattr(self.payer_bank_name, 'to_alipay_dict'):
                params['payer_bank_name'] = self.payer_bank_name.to_alipay_dict()
            else:
                params['payer_bank_name'] = self.payer_bank_name
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.payer_phone:
            if hasattr(self.payer_phone, 'to_alipay_dict'):
                params['payer_phone'] = self.payer_phone.to_alipay_dict()
            else:
                params['payer_phone'] = self.payer_phone
        if self.payer_register_no:
            if hasattr(self.payer_register_no, 'to_alipay_dict'):
                params['payer_register_no'] = self.payer_register_no.to_alipay_dict()
            else:
                params['payer_register_no'] = self.payer_register_no
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.platform_user_id:
            if hasattr(self.platform_user_id, 'to_alipay_dict'):
                params['platform_user_id'] = self.platform_user_id.to_alipay_dict()
            else:
                params['platform_user_id'] = self.platform_user_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sum_price:
            if hasattr(self.sum_price, 'to_alipay_dict'):
                params['sum_price'] = self.sum_price.to_alipay_dict()
            else:
                params['sum_price'] = self.sum_price
        if self.sum_tax:
            if hasattr(self.sum_tax, 'to_alipay_dict'):
                params['sum_tax'] = self.sum_tax.to_alipay_dict()
            else:
                params['sum_tax'] = self.sum_tax
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceOpenRedCreateModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'auto_fill_info' in d:
            o.auto_fill_info = d['auto_fill_info']
        if 'auto_preprocess' in d:
            o.auto_preprocess = d['auto_preprocess']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_items' in d:
            o.invoice_items = d['invoice_items']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_memo' in d:
            o.invoice_memo = d['invoice_memo']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'normal_invoice_code' in d:
            o.normal_invoice_code = d['normal_invoice_code']
        if 'normal_invoice_no' in d:
            o.normal_invoice_no = d['normal_invoice_no']
        if 'outer_id' in d:
            o.outer_id = d['outer_id']
        if 'payee_address' in d:
            o.payee_address = d['payee_address']
        if 'payee_bank_account_id' in d:
            o.payee_bank_account_id = d['payee_bank_account_id']
        if 'payee_bank_name' in d:
            o.payee_bank_name = d['payee_bank_name']
        if 'payee_checker' in d:
            o.payee_checker = d['payee_checker']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payee_operator' in d:
            o.payee_operator = d['payee_operator']
        if 'payee_phone' in d:
            o.payee_phone = d['payee_phone']
        if 'payee_receiver' in d:
            o.payee_receiver = d['payee_receiver']
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'payer_address' in d:
            o.payer_address = d['payer_address']
        if 'payer_bank_account_id' in d:
            o.payer_bank_account_id = d['payer_bank_account_id']
        if 'payer_bank_name' in d:
            o.payer_bank_name = d['payer_bank_name']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'payer_phone' in d:
            o.payer_phone = d['payer_phone']
        if 'payer_register_no' in d:
            o.payer_register_no = d['payer_register_no']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'platform_user_id' in d:
            o.platform_user_id = d['platform_user_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sum_price' in d:
            o.sum_price = d['sum_price']
        if 'sum_tax' in d:
            o.sum_tax = d['sum_tax']
        return o


