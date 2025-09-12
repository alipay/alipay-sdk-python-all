#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderInvoiceItem import OrderInvoiceItem


class OrderInvoice(object):

    def __init__(self):
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._buyer_tel = None
        self._checker = None
        self._clerk = None
        self._clerk_cert_no = None
        self._clerk_cert_type = None
        self._img_file_url = None
        self._invoice_amount = None
        self._invoice_amount_without_tax = None
        self._invoice_date = None
        self._invoice_kind = None
        self._invoice_no = None
        self._invoice_status = None
        self._invoice_status_message = None
        self._invoice_tax_amount = None
        self._invoice_type = None
        self._order_invoice_item_list = None
        self._payee = None
        self._pdf_file_url = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_name = None
        self._seller_tax_no = None
        self._seller_tel = None

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
    def clerk_cert_no(self):
        return self._clerk_cert_no

    @clerk_cert_no.setter
    def clerk_cert_no(self, value):
        self._clerk_cert_no = value
    @property
    def clerk_cert_type(self):
        return self._clerk_cert_type

    @clerk_cert_type.setter
    def clerk_cert_type(self, value):
        self._clerk_cert_type = value
    @property
    def img_file_url(self):
        return self._img_file_url

    @img_file_url.setter
    def img_file_url(self, value):
        self._img_file_url = value
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
    def invoice_status_message(self):
        return self._invoice_status_message

    @invoice_status_message.setter
    def invoice_status_message(self, value):
        self._invoice_status_message = value
    @property
    def invoice_tax_amount(self):
        return self._invoice_tax_amount

    @invoice_tax_amount.setter
    def invoice_tax_amount(self, value):
        self._invoice_tax_amount = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def order_invoice_item_list(self):
        return self._order_invoice_item_list

    @order_invoice_item_list.setter
    def order_invoice_item_list(self, value):
        if isinstance(value, list):
            self._order_invoice_item_list = list()
            for i in value:
                if isinstance(i, OrderInvoiceItem):
                    self._order_invoice_item_list.append(i)
                else:
                    self._order_invoice_item_list.append(OrderInvoiceItem.from_alipay_dict(i))
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
    @property
    def pdf_file_url(self):
        return self._pdf_file_url

    @pdf_file_url.setter
    def pdf_file_url(self, value):
        self._pdf_file_url = value
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


    def to_alipay_dict(self):
        params = dict()
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
        if self.clerk_cert_no:
            if hasattr(self.clerk_cert_no, 'to_alipay_dict'):
                params['clerk_cert_no'] = self.clerk_cert_no.to_alipay_dict()
            else:
                params['clerk_cert_no'] = self.clerk_cert_no
        if self.clerk_cert_type:
            if hasattr(self.clerk_cert_type, 'to_alipay_dict'):
                params['clerk_cert_type'] = self.clerk_cert_type.to_alipay_dict()
            else:
                params['clerk_cert_type'] = self.clerk_cert_type
        if self.img_file_url:
            if hasattr(self.img_file_url, 'to_alipay_dict'):
                params['img_file_url'] = self.img_file_url.to_alipay_dict()
            else:
                params['img_file_url'] = self.img_file_url
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
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_status_message:
            if hasattr(self.invoice_status_message, 'to_alipay_dict'):
                params['invoice_status_message'] = self.invoice_status_message.to_alipay_dict()
            else:
                params['invoice_status_message'] = self.invoice_status_message
        if self.invoice_tax_amount:
            if hasattr(self.invoice_tax_amount, 'to_alipay_dict'):
                params['invoice_tax_amount'] = self.invoice_tax_amount.to_alipay_dict()
            else:
                params['invoice_tax_amount'] = self.invoice_tax_amount
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.order_invoice_item_list:
            if isinstance(self.order_invoice_item_list, list):
                for i in range(0, len(self.order_invoice_item_list)):
                    element = self.order_invoice_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_invoice_item_list[i] = element.to_alipay_dict()
            if hasattr(self.order_invoice_item_list, 'to_alipay_dict'):
                params['order_invoice_item_list'] = self.order_invoice_item_list.to_alipay_dict()
            else:
                params['order_invoice_item_list'] = self.order_invoice_item_list
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.pdf_file_url:
            if hasattr(self.pdf_file_url, 'to_alipay_dict'):
                params['pdf_file_url'] = self.pdf_file_url.to_alipay_dict()
            else:
                params['pdf_file_url'] = self.pdf_file_url
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderInvoice()
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
        if 'checker' in d:
            o.checker = d['checker']
        if 'clerk' in d:
            o.clerk = d['clerk']
        if 'clerk_cert_no' in d:
            o.clerk_cert_no = d['clerk_cert_no']
        if 'clerk_cert_type' in d:
            o.clerk_cert_type = d['clerk_cert_type']
        if 'img_file_url' in d:
            o.img_file_url = d['img_file_url']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_amount_without_tax' in d:
            o.invoice_amount_without_tax = d['invoice_amount_without_tax']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_status_message' in d:
            o.invoice_status_message = d['invoice_status_message']
        if 'invoice_tax_amount' in d:
            o.invoice_tax_amount = d['invoice_tax_amount']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'order_invoice_item_list' in d:
            o.order_invoice_item_list = d['order_invoice_item_list']
        if 'payee' in d:
            o.payee = d['payee']
        if 'pdf_file_url' in d:
            o.pdf_file_url = d['pdf_file_url']
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
        return o


