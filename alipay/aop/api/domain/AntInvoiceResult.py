#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntInvoiceItem import AntInvoiceItem


class AntInvoiceResult(object):

    def __init__(self):
        self._anti_fake_code = None
        self._biz_error_code = None
        self._biz_error_msg = None
        self._ciphertext = None
        self._device_no = None
        self._file_data_type = None
        self._file_path = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_items = None
        self._invoice_kind = None
        self._invoice_no = None
        self._invoice_time = None
        self._invoice_type = None
        self._normal_invoice_code = None
        self._normal_invoice_no = None
        self._nvoice_amount = None
        self._payee_checker = None
        self._payee_name = None
        self._payee_operator = None
        self._payee_receive = None
        self._payee_register_no = None
        self._payer_address = None
        self._payer_bankaccount = None
        self._payer_name = None
        self._payer_phone = None
        self._payer_register_no = None
        self._platform_code = None
        self._platform_tid = None
        self._retrying = None
        self._serial_no = None
        self._status = None
        self._sum_price = None
        self._sum_tax = None

    @property
    def anti_fake_code(self):
        return self._anti_fake_code

    @anti_fake_code.setter
    def anti_fake_code(self, value):
        self._anti_fake_code = value
    @property
    def biz_error_code(self):
        return self._biz_error_code

    @biz_error_code.setter
    def biz_error_code(self, value):
        self._biz_error_code = value
    @property
    def biz_error_msg(self):
        return self._biz_error_msg

    @biz_error_msg.setter
    def biz_error_msg(self, value):
        self._biz_error_msg = value
    @property
    def ciphertext(self):
        return self._ciphertext

    @ciphertext.setter
    def ciphertext(self, value):
        self._ciphertext = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def file_data_type(self):
        return self._file_data_type

    @file_data_type.setter
    def file_data_type(self, value):
        self._file_data_type = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
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
    def invoice_items(self):
        return self._invoice_items

    @invoice_items.setter
    def invoice_items(self, value):
        if isinstance(value, list):
            self._invoice_items = list()
            for i in value:
                if isinstance(i, AntInvoiceItem):
                    self._invoice_items.append(i)
                else:
                    self._invoice_items.append(AntInvoiceItem.from_alipay_dict(i))
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_time(self):
        return self._invoice_time

    @invoice_time.setter
    def invoice_time(self, value):
        self._invoice_time = value
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
    def nvoice_amount(self):
        return self._nvoice_amount

    @nvoice_amount.setter
    def nvoice_amount(self, value):
        self._nvoice_amount = value
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
    def payee_receive(self):
        return self._payee_receive

    @payee_receive.setter
    def payee_receive(self, value):
        self._payee_receive = value
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
    def payer_bankaccount(self):
        return self._payer_bankaccount

    @payer_bankaccount.setter
    def payer_bankaccount(self, value):
        self._payer_bankaccount = value
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
    def platform_tid(self):
        return self._platform_tid

    @platform_tid.setter
    def platform_tid(self, value):
        self._platform_tid = value
    @property
    def retrying(self):
        return self._retrying

    @retrying.setter
    def retrying(self, value):
        self._retrying = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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
        if self.anti_fake_code:
            if hasattr(self.anti_fake_code, 'to_alipay_dict'):
                params['anti_fake_code'] = self.anti_fake_code.to_alipay_dict()
            else:
                params['anti_fake_code'] = self.anti_fake_code
        if self.biz_error_code:
            if hasattr(self.biz_error_code, 'to_alipay_dict'):
                params['biz_error_code'] = self.biz_error_code.to_alipay_dict()
            else:
                params['biz_error_code'] = self.biz_error_code
        if self.biz_error_msg:
            if hasattr(self.biz_error_msg, 'to_alipay_dict'):
                params['biz_error_msg'] = self.biz_error_msg.to_alipay_dict()
            else:
                params['biz_error_msg'] = self.biz_error_msg
        if self.ciphertext:
            if hasattr(self.ciphertext, 'to_alipay_dict'):
                params['ciphertext'] = self.ciphertext.to_alipay_dict()
            else:
                params['ciphertext'] = self.ciphertext
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.file_data_type:
            if hasattr(self.file_data_type, 'to_alipay_dict'):
                params['file_data_type'] = self.file_data_type.to_alipay_dict()
            else:
                params['file_data_type'] = self.file_data_type
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
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
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_time:
            if hasattr(self.invoice_time, 'to_alipay_dict'):
                params['invoice_time'] = self.invoice_time.to_alipay_dict()
            else:
                params['invoice_time'] = self.invoice_time
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
        if self.nvoice_amount:
            if hasattr(self.nvoice_amount, 'to_alipay_dict'):
                params['nvoice_amount'] = self.nvoice_amount.to_alipay_dict()
            else:
                params['nvoice_amount'] = self.nvoice_amount
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
        if self.payee_receive:
            if hasattr(self.payee_receive, 'to_alipay_dict'):
                params['payee_receive'] = self.payee_receive.to_alipay_dict()
            else:
                params['payee_receive'] = self.payee_receive
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
        if self.payer_bankaccount:
            if hasattr(self.payer_bankaccount, 'to_alipay_dict'):
                params['payer_bankaccount'] = self.payer_bankaccount.to_alipay_dict()
            else:
                params['payer_bankaccount'] = self.payer_bankaccount
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
        if self.platform_tid:
            if hasattr(self.platform_tid, 'to_alipay_dict'):
                params['platform_tid'] = self.platform_tid.to_alipay_dict()
            else:
                params['platform_tid'] = self.platform_tid
        if self.retrying:
            if hasattr(self.retrying, 'to_alipay_dict'):
                params['retrying'] = self.retrying.to_alipay_dict()
            else:
                params['retrying'] = self.retrying
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AntInvoiceResult()
        if 'anti_fake_code' in d:
            o.anti_fake_code = d['anti_fake_code']
        if 'biz_error_code' in d:
            o.biz_error_code = d['biz_error_code']
        if 'biz_error_msg' in d:
            o.biz_error_msg = d['biz_error_msg']
        if 'ciphertext' in d:
            o.ciphertext = d['ciphertext']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'file_data_type' in d:
            o.file_data_type = d['file_data_type']
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_items' in d:
            o.invoice_items = d['invoice_items']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_time' in d:
            o.invoice_time = d['invoice_time']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'normal_invoice_code' in d:
            o.normal_invoice_code = d['normal_invoice_code']
        if 'normal_invoice_no' in d:
            o.normal_invoice_no = d['normal_invoice_no']
        if 'nvoice_amount' in d:
            o.nvoice_amount = d['nvoice_amount']
        if 'payee_checker' in d:
            o.payee_checker = d['payee_checker']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payee_operator' in d:
            o.payee_operator = d['payee_operator']
        if 'payee_receive' in d:
            o.payee_receive = d['payee_receive']
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'payer_address' in d:
            o.payer_address = d['payer_address']
        if 'payer_bankaccount' in d:
            o.payer_bankaccount = d['payer_bankaccount']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'payer_phone' in d:
            o.payer_phone = d['payer_phone']
        if 'payer_register_no' in d:
            o.payer_register_no = d['payer_register_no']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'platform_tid' in d:
            o.platform_tid = d['platform_tid']
        if 'retrying' in d:
            o.retrying = d['retrying']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'status' in d:
            o.status = d['status']
        if 'sum_price' in d:
            o.sum_price = d['sum_price']
        if 'sum_tax' in d:
            o.sum_tax = d['sum_tax']
        return o


