#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceContentInfo import InvoiceContentInfo


class CompleteVoucherInfo(object):

    def __init__(self):
        self._anti_fake_code = None
        self._check_sum = None
        self._device_no = None
        self._file_download_url = None
        self._file_type = None
        self._invoice_amount = None
        self._invoice_code = None
        self._invoice_content_list = None
        self._invoice_date = None
        self._invoice_kind = None
        self._invoice_memo = None
        self._invoice_no = None
        self._invoice_title = None
        self._invoice_type = None
        self._payee_address = None
        self._payee_bank_account = None
        self._payee_bank_name = None
        self._payee_checker = None
        self._payee_mobile = None
        self._payee_name = None
        self._payee_operator = None
        self._payee_receiver = None
        self._payee_register_no = None
        self._payer_address = None
        self._payer_bank_account = None
        self._payer_bank_name = None
        self._payer_mobile = None
        self._payer_name = None
        self._payer_register_no = None
        self._sum_price = None
        self._sum_tax = None

    @property
    def anti_fake_code(self):
        return self._anti_fake_code

    @anti_fake_code.setter
    def anti_fake_code(self, value):
        self._anti_fake_code = value
    @property
    def check_sum(self):
        return self._check_sum

    @check_sum.setter
    def check_sum(self, value):
        self._check_sum = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
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
    def invoice_content_list(self):
        return self._invoice_content_list

    @invoice_content_list.setter
    def invoice_content_list(self, value):
        if isinstance(value, list):
            self._invoice_content_list = list()
            for i in value:
                if isinstance(i, InvoiceContentInfo):
                    self._invoice_content_list.append(i)
                else:
                    self._invoice_content_list.append(InvoiceContentInfo.from_alipay_dict(i))
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
        self._invoice_title = value
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
    def payee_checker(self):
        return self._payee_checker

    @payee_checker.setter
    def payee_checker(self, value):
        self._payee_checker = value
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
    def payee_operator(self):
        return self._payee_operator

    @payee_operator.setter
    def payee_operator(self, value):
        self._payee_operator = value
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
        if self.check_sum:
            if hasattr(self.check_sum, 'to_alipay_dict'):
                params['check_sum'] = self.check_sum.to_alipay_dict()
            else:
                params['check_sum'] = self.check_sum
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
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
        if self.invoice_content_list:
            if isinstance(self.invoice_content_list, list):
                for i in range(0, len(self.invoice_content_list)):
                    element = self.invoice_content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_content_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_content_list, 'to_alipay_dict'):
                params['invoice_content_list'] = self.invoice_content_list.to_alipay_dict()
            else:
                params['invoice_content_list'] = self.invoice_content_list
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
        if self.payee_checker:
            if hasattr(self.payee_checker, 'to_alipay_dict'):
                params['payee_checker'] = self.payee_checker.to_alipay_dict()
            else:
                params['payee_checker'] = self.payee_checker
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
        if self.payee_operator:
            if hasattr(self.payee_operator, 'to_alipay_dict'):
                params['payee_operator'] = self.payee_operator.to_alipay_dict()
            else:
                params['payee_operator'] = self.payee_operator
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
        o = CompleteVoucherInfo()
        if 'anti_fake_code' in d:
            o.anti_fake_code = d['anti_fake_code']
        if 'check_sum' in d:
            o.check_sum = d['check_sum']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'file_download_url' in d:
            o.file_download_url = d['file_download_url']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_content_list' in d:
            o.invoice_content_list = d['invoice_content_list']
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
        if 'payee_address' in d:
            o.payee_address = d['payee_address']
        if 'payee_bank_account' in d:
            o.payee_bank_account = d['payee_bank_account']
        if 'payee_bank_name' in d:
            o.payee_bank_name = d['payee_bank_name']
        if 'payee_checker' in d:
            o.payee_checker = d['payee_checker']
        if 'payee_mobile' in d:
            o.payee_mobile = d['payee_mobile']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payee_operator' in d:
            o.payee_operator = d['payee_operator']
        if 'payee_receiver' in d:
            o.payee_receiver = d['payee_receiver']
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
        if 'sum_price' in d:
            o.sum_price = d['sum_price']
        if 'sum_tax' in d:
            o.sum_tax = d['sum_tax']
        return o


