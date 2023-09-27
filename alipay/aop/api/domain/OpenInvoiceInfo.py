#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenInvoiceItem import OpenInvoiceItem
from alipay.aop.api.domain.OpenInvoiceTravelInfo import OpenInvoiceTravelInfo


class OpenInvoiceInfo(object):

    def __init__(self):
        self._apply_id = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._buyer_tel = None
        self._check_code = None
        self._checker = None
        self._clerk = None
        self._file_type = None
        self._file_url = None
        self._img_url = None
        self._invoice_amount = None
        self._invoice_amount_without_tax = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_item_list = None
        self._invoice_kind = None
        self._invoice_no = None
        self._invoice_tag = None
        self._invoice_tax_amount = None
        self._invoice_tax_rate = None
        self._invoice_type = None
        self._machine_code = None
        self._original_invoice_code = None
        self._original_invoice_no = None
        self._password_area = None
        self._payee = None
        self._qr_code_text = None
        self._red_remarks = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_name = None
        self._seller_tax_no = None
        self._seller_tel = None
        self._travel_info_list = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def buyer_address(self):
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, value):
        self._buyer_address = value
    @property
    def buyer_bank_account(self):
        return self._buyer_bank_account

    @buyer_bank_account.setter
    def buyer_bank_account(self, value):
        self._buyer_bank_account = value
    @property
    def buyer_bank_name(self):
        return self._buyer_bank_name

    @buyer_bank_name.setter
    def buyer_bank_name(self, value):
        self._buyer_bank_name = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def buyer_tel(self):
        return self._buyer_tel

    @buyer_tel.setter
    def buyer_tel(self, value):
        self._buyer_tel = value
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
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def invoice_amount_without_tax(self):
        return self._invoice_amount_without_tax

    @invoice_amount_without_tax.setter
    def invoice_amount_without_tax(self, value):
        self._invoice_amount_without_tax = value
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
    def invoice_item_list(self):
        return self._invoice_item_list

    @invoice_item_list.setter
    def invoice_item_list(self, value):
        if isinstance(value, list):
            self._invoice_item_list = list()
            for i in value:
                if isinstance(i, OpenInvoiceItem):
                    self._invoice_item_list.append(i)
                else:
                    self._invoice_item_list.append(OpenInvoiceItem.from_alipay_dict(i))
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
    def invoice_tag(self):
        return self._invoice_tag

    @invoice_tag.setter
    def invoice_tag(self, value):
        self._invoice_tag = value
    @property
    def invoice_tax_amount(self):
        return self._invoice_tax_amount

    @invoice_tax_amount.setter
    def invoice_tax_amount(self, value):
        self._invoice_tax_amount = value
    @property
    def invoice_tax_rate(self):
        return self._invoice_tax_rate

    @invoice_tax_rate.setter
    def invoice_tax_rate(self, value):
        self._invoice_tax_rate = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def machine_code(self):
        return self._machine_code

    @machine_code.setter
    def machine_code(self, value):
        self._machine_code = value
    @property
    def original_invoice_code(self):
        return self._original_invoice_code

    @original_invoice_code.setter
    def original_invoice_code(self, value):
        self._original_invoice_code = value
    @property
    def original_invoice_no(self):
        return self._original_invoice_no

    @original_invoice_no.setter
    def original_invoice_no(self, value):
        self._original_invoice_no = value
    @property
    def password_area(self):
        return self._password_area

    @password_area.setter
    def password_area(self, value):
        self._password_area = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
    @property
    def qr_code_text(self):
        return self._qr_code_text

    @qr_code_text.setter
    def qr_code_text(self, value):
        self._qr_code_text = value
    @property
    def red_remarks(self):
        return self._red_remarks

    @red_remarks.setter
    def red_remarks(self, value):
        self._red_remarks = value
    @property
    def seller_address(self):
        return self._seller_address

    @seller_address.setter
    def seller_address(self, value):
        self._seller_address = value
    @property
    def seller_bank_account(self):
        return self._seller_bank_account

    @seller_bank_account.setter
    def seller_bank_account(self, value):
        self._seller_bank_account = value
    @property
    def seller_bank_name(self):
        return self._seller_bank_name

    @seller_bank_name.setter
    def seller_bank_name(self, value):
        self._seller_bank_name = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value
    @property
    def seller_tel(self):
        return self._seller_tel

    @seller_tel.setter
    def seller_tel(self, value):
        self._seller_tel = value
    @property
    def travel_info_list(self):
        return self._travel_info_list

    @travel_info_list.setter
    def travel_info_list(self, value):
        if isinstance(value, list):
            self._travel_info_list = list()
            for i in value:
                if isinstance(i, OpenInvoiceTravelInfo):
                    self._travel_info_list.append(i)
                else:
                    self._travel_info_list.append(OpenInvoiceTravelInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.buyer_address:
            if hasattr(self.buyer_address, 'to_alipay_dict'):
                params['buyer_address'] = self.buyer_address.to_alipay_dict()
            else:
                params['buyer_address'] = self.buyer_address
        if self.buyer_bank_account:
            if hasattr(self.buyer_bank_account, 'to_alipay_dict'):
                params['buyer_bank_account'] = self.buyer_bank_account.to_alipay_dict()
            else:
                params['buyer_bank_account'] = self.buyer_bank_account
        if self.buyer_bank_name:
            if hasattr(self.buyer_bank_name, 'to_alipay_dict'):
                params['buyer_bank_name'] = self.buyer_bank_name.to_alipay_dict()
            else:
                params['buyer_bank_name'] = self.buyer_bank_name
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.buyer_tel:
            if hasattr(self.buyer_tel, 'to_alipay_dict'):
                params['buyer_tel'] = self.buyer_tel.to_alipay_dict()
            else:
                params['buyer_tel'] = self.buyer_tel
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
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.invoice_amount_without_tax:
            if hasattr(self.invoice_amount_without_tax, 'to_alipay_dict'):
                params['invoice_amount_without_tax'] = self.invoice_amount_without_tax.to_alipay_dict()
            else:
                params['invoice_amount_without_tax'] = self.invoice_amount_without_tax
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
        if self.invoice_item_list:
            if isinstance(self.invoice_item_list, list):
                for i in range(0, len(self.invoice_item_list)):
                    element = self.invoice_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_item_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_item_list, 'to_alipay_dict'):
                params['invoice_item_list'] = self.invoice_item_list.to_alipay_dict()
            else:
                params['invoice_item_list'] = self.invoice_item_list
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
        if self.invoice_tag:
            if hasattr(self.invoice_tag, 'to_alipay_dict'):
                params['invoice_tag'] = self.invoice_tag.to_alipay_dict()
            else:
                params['invoice_tag'] = self.invoice_tag
        if self.invoice_tax_amount:
            if hasattr(self.invoice_tax_amount, 'to_alipay_dict'):
                params['invoice_tax_amount'] = self.invoice_tax_amount.to_alipay_dict()
            else:
                params['invoice_tax_amount'] = self.invoice_tax_amount
        if self.invoice_tax_rate:
            if hasattr(self.invoice_tax_rate, 'to_alipay_dict'):
                params['invoice_tax_rate'] = self.invoice_tax_rate.to_alipay_dict()
            else:
                params['invoice_tax_rate'] = self.invoice_tax_rate
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.machine_code:
            if hasattr(self.machine_code, 'to_alipay_dict'):
                params['machine_code'] = self.machine_code.to_alipay_dict()
            else:
                params['machine_code'] = self.machine_code
        if self.original_invoice_code:
            if hasattr(self.original_invoice_code, 'to_alipay_dict'):
                params['original_invoice_code'] = self.original_invoice_code.to_alipay_dict()
            else:
                params['original_invoice_code'] = self.original_invoice_code
        if self.original_invoice_no:
            if hasattr(self.original_invoice_no, 'to_alipay_dict'):
                params['original_invoice_no'] = self.original_invoice_no.to_alipay_dict()
            else:
                params['original_invoice_no'] = self.original_invoice_no
        if self.password_area:
            if hasattr(self.password_area, 'to_alipay_dict'):
                params['password_area'] = self.password_area.to_alipay_dict()
            else:
                params['password_area'] = self.password_area
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.qr_code_text:
            if hasattr(self.qr_code_text, 'to_alipay_dict'):
                params['qr_code_text'] = self.qr_code_text.to_alipay_dict()
            else:
                params['qr_code_text'] = self.qr_code_text
        if self.red_remarks:
            if hasattr(self.red_remarks, 'to_alipay_dict'):
                params['red_remarks'] = self.red_remarks.to_alipay_dict()
            else:
                params['red_remarks'] = self.red_remarks
        if self.seller_address:
            if hasattr(self.seller_address, 'to_alipay_dict'):
                params['seller_address'] = self.seller_address.to_alipay_dict()
            else:
                params['seller_address'] = self.seller_address
        if self.seller_bank_account:
            if hasattr(self.seller_bank_account, 'to_alipay_dict'):
                params['seller_bank_account'] = self.seller_bank_account.to_alipay_dict()
            else:
                params['seller_bank_account'] = self.seller_bank_account
        if self.seller_bank_name:
            if hasattr(self.seller_bank_name, 'to_alipay_dict'):
                params['seller_bank_name'] = self.seller_bank_name.to_alipay_dict()
            else:
                params['seller_bank_name'] = self.seller_bank_name
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = self.seller_tax_no.to_alipay_dict()
            else:
                params['seller_tax_no'] = self.seller_tax_no
        if self.seller_tel:
            if hasattr(self.seller_tel, 'to_alipay_dict'):
                params['seller_tel'] = self.seller_tel.to_alipay_dict()
            else:
                params['seller_tel'] = self.seller_tel
        if self.travel_info_list:
            if isinstance(self.travel_info_list, list):
                for i in range(0, len(self.travel_info_list)):
                    element = self.travel_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.travel_info_list[i] = element.to_alipay_dict()
            if hasattr(self.travel_info_list, 'to_alipay_dict'):
                params['travel_info_list'] = self.travel_info_list.to_alipay_dict()
            else:
                params['travel_info_list'] = self.travel_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenInvoiceInfo()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'buyer_address' in d:
            o.buyer_address = d['buyer_address']
        if 'buyer_bank_account' in d:
            o.buyer_bank_account = d['buyer_bank_account']
        if 'buyer_bank_name' in d:
            o.buyer_bank_name = d['buyer_bank_name']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'buyer_tel' in d:
            o.buyer_tel = d['buyer_tel']
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'checker' in d:
            o.checker = d['checker']
        if 'clerk' in d:
            o.clerk = d['clerk']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_amount_without_tax' in d:
            o.invoice_amount_without_tax = d['invoice_amount_without_tax']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_item_list' in d:
            o.invoice_item_list = d['invoice_item_list']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_tag' in d:
            o.invoice_tag = d['invoice_tag']
        if 'invoice_tax_amount' in d:
            o.invoice_tax_amount = d['invoice_tax_amount']
        if 'invoice_tax_rate' in d:
            o.invoice_tax_rate = d['invoice_tax_rate']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'machine_code' in d:
            o.machine_code = d['machine_code']
        if 'original_invoice_code' in d:
            o.original_invoice_code = d['original_invoice_code']
        if 'original_invoice_no' in d:
            o.original_invoice_no = d['original_invoice_no']
        if 'password_area' in d:
            o.password_area = d['password_area']
        if 'payee' in d:
            o.payee = d['payee']
        if 'qr_code_text' in d:
            o.qr_code_text = d['qr_code_text']
        if 'red_remarks' in d:
            o.red_remarks = d['red_remarks']
        if 'seller_address' in d:
            o.seller_address = d['seller_address']
        if 'seller_bank_account' in d:
            o.seller_bank_account = d['seller_bank_account']
        if 'seller_bank_name' in d:
            o.seller_bank_name = d['seller_bank_name']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'seller_tel' in d:
            o.seller_tel = d['seller_tel']
        if 'travel_info_list' in d:
            o.travel_info_list = d['travel_info_list']
        return o


