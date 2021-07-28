#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApInvoiceLineOrderRequest import ApInvoiceLineOrderRequest
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ApInvoiceOrderRequest(object):

    def __init__(self):
        self._ap_invoice_line_orders = None
        self._attachment_name = None
        self._attachment_oss_key = None
        self._biz_type = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_inst_id = None
        self._buyer_invoice_title = None
        self._buyer_tax_no = None
        self._buyer_telephone = None
        self._invoice_amt = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_no = None
        self._invoice_note = None
        self._invoice_receive_date = None
        self._invoice_source = None
        self._invoice_type = None
        self._memo = None
        self._red = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_company_name = None
        self._seller_ip_role_id = None
        self._seller_mid = None
        self._seller_tax_no = None
        self._seller_telephone = None

    @property
    def ap_invoice_line_orders(self):
        return self._ap_invoice_line_orders

    @ap_invoice_line_orders.setter
    def ap_invoice_line_orders(self, value):
        if isinstance(value, list):
            self._ap_invoice_line_orders = list()
            for i in value:
                if isinstance(i, ApInvoiceLineOrderRequest):
                    self._ap_invoice_line_orders.append(i)
                else:
                    self._ap_invoice_line_orders.append(ApInvoiceLineOrderRequest.from_alipay_dict(i))
    @property
    def attachment_name(self):
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self._attachment_name = value
    @property
    def attachment_oss_key(self):
        return self._attachment_oss_key

    @attachment_oss_key.setter
    def attachment_oss_key(self, value):
        self._attachment_oss_key = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
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
    def buyer_inst_id(self):
        return self._buyer_inst_id

    @buyer_inst_id.setter
    def buyer_inst_id(self, value):
        self._buyer_inst_id = value
    @property
    def buyer_invoice_title(self):
        return self._buyer_invoice_title

    @buyer_invoice_title.setter
    def buyer_invoice_title(self, value):
        self._buyer_invoice_title = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def buyer_telephone(self):
        return self._buyer_telephone

    @buyer_telephone.setter
    def buyer_telephone(self, value):
        self._buyer_telephone = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_amt = value
        else:
            self._invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_note(self):
        return self._invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self._invoice_note = value
    @property
    def invoice_receive_date(self):
        return self._invoice_receive_date

    @invoice_receive_date.setter
    def invoice_receive_date(self, value):
        self._invoice_receive_date = value
    @property
    def invoice_source(self):
        return self._invoice_source

    @invoice_source.setter
    def invoice_source(self, value):
        self._invoice_source = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        self._red = value
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
    def seller_company_name(self):
        return self._seller_company_name

    @seller_company_name.setter
    def seller_company_name(self, value):
        self._seller_company_name = value
    @property
    def seller_ip_role_id(self):
        return self._seller_ip_role_id

    @seller_ip_role_id.setter
    def seller_ip_role_id(self, value):
        self._seller_ip_role_id = value
    @property
    def seller_mid(self):
        return self._seller_mid

    @seller_mid.setter
    def seller_mid(self, value):
        self._seller_mid = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value
    @property
    def seller_telephone(self):
        return self._seller_telephone

    @seller_telephone.setter
    def seller_telephone(self, value):
        self._seller_telephone = value


    def to_alipay_dict(self):
        params = dict()
        if self.ap_invoice_line_orders:
            if isinstance(self.ap_invoice_line_orders, list):
                for i in range(0, len(self.ap_invoice_line_orders)):
                    element = self.ap_invoice_line_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ap_invoice_line_orders[i] = element.to_alipay_dict()
            if hasattr(self.ap_invoice_line_orders, 'to_alipay_dict'):
                params['ap_invoice_line_orders'] = self.ap_invoice_line_orders.to_alipay_dict()
            else:
                params['ap_invoice_line_orders'] = self.ap_invoice_line_orders
        if self.attachment_name:
            if hasattr(self.attachment_name, 'to_alipay_dict'):
                params['attachment_name'] = self.attachment_name.to_alipay_dict()
            else:
                params['attachment_name'] = self.attachment_name
        if self.attachment_oss_key:
            if hasattr(self.attachment_oss_key, 'to_alipay_dict'):
                params['attachment_oss_key'] = self.attachment_oss_key.to_alipay_dict()
            else:
                params['attachment_oss_key'] = self.attachment_oss_key
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
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
        if self.buyer_inst_id:
            if hasattr(self.buyer_inst_id, 'to_alipay_dict'):
                params['buyer_inst_id'] = self.buyer_inst_id.to_alipay_dict()
            else:
                params['buyer_inst_id'] = self.buyer_inst_id
        if self.buyer_invoice_title:
            if hasattr(self.buyer_invoice_title, 'to_alipay_dict'):
                params['buyer_invoice_title'] = self.buyer_invoice_title.to_alipay_dict()
            else:
                params['buyer_invoice_title'] = self.buyer_invoice_title
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.buyer_telephone:
            if hasattr(self.buyer_telephone, 'to_alipay_dict'):
                params['buyer_telephone'] = self.buyer_telephone.to_alipay_dict()
            else:
                params['buyer_telephone'] = self.buyer_telephone
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
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
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_note:
            if hasattr(self.invoice_note, 'to_alipay_dict'):
                params['invoice_note'] = self.invoice_note.to_alipay_dict()
            else:
                params['invoice_note'] = self.invoice_note
        if self.invoice_receive_date:
            if hasattr(self.invoice_receive_date, 'to_alipay_dict'):
                params['invoice_receive_date'] = self.invoice_receive_date.to_alipay_dict()
            else:
                params['invoice_receive_date'] = self.invoice_receive_date
        if self.invoice_source:
            if hasattr(self.invoice_source, 'to_alipay_dict'):
                params['invoice_source'] = self.invoice_source.to_alipay_dict()
            else:
                params['invoice_source'] = self.invoice_source
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.red:
            if hasattr(self.red, 'to_alipay_dict'):
                params['red'] = self.red.to_alipay_dict()
            else:
                params['red'] = self.red
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
        if self.seller_company_name:
            if hasattr(self.seller_company_name, 'to_alipay_dict'):
                params['seller_company_name'] = self.seller_company_name.to_alipay_dict()
            else:
                params['seller_company_name'] = self.seller_company_name
        if self.seller_ip_role_id:
            if hasattr(self.seller_ip_role_id, 'to_alipay_dict'):
                params['seller_ip_role_id'] = self.seller_ip_role_id.to_alipay_dict()
            else:
                params['seller_ip_role_id'] = self.seller_ip_role_id
        if self.seller_mid:
            if hasattr(self.seller_mid, 'to_alipay_dict'):
                params['seller_mid'] = self.seller_mid.to_alipay_dict()
            else:
                params['seller_mid'] = self.seller_mid
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = self.seller_tax_no.to_alipay_dict()
            else:
                params['seller_tax_no'] = self.seller_tax_no
        if self.seller_telephone:
            if hasattr(self.seller_telephone, 'to_alipay_dict'):
                params['seller_telephone'] = self.seller_telephone.to_alipay_dict()
            else:
                params['seller_telephone'] = self.seller_telephone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApInvoiceOrderRequest()
        if 'ap_invoice_line_orders' in d:
            o.ap_invoice_line_orders = d['ap_invoice_line_orders']
        if 'attachment_name' in d:
            o.attachment_name = d['attachment_name']
        if 'attachment_oss_key' in d:
            o.attachment_oss_key = d['attachment_oss_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'buyer_address' in d:
            o.buyer_address = d['buyer_address']
        if 'buyer_bank_account' in d:
            o.buyer_bank_account = d['buyer_bank_account']
        if 'buyer_bank_name' in d:
            o.buyer_bank_name = d['buyer_bank_name']
        if 'buyer_inst_id' in d:
            o.buyer_inst_id = d['buyer_inst_id']
        if 'buyer_invoice_title' in d:
            o.buyer_invoice_title = d['buyer_invoice_title']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'buyer_telephone' in d:
            o.buyer_telephone = d['buyer_telephone']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'invoice_receive_date' in d:
            o.invoice_receive_date = d['invoice_receive_date']
        if 'invoice_source' in d:
            o.invoice_source = d['invoice_source']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'red' in d:
            o.red = d['red']
        if 'seller_address' in d:
            o.seller_address = d['seller_address']
        if 'seller_bank_account' in d:
            o.seller_bank_account = d['seller_bank_account']
        if 'seller_bank_name' in d:
            o.seller_bank_name = d['seller_bank_name']
        if 'seller_company_name' in d:
            o.seller_company_name = d['seller_company_name']
        if 'seller_ip_role_id' in d:
            o.seller_ip_role_id = d['seller_ip_role_id']
        if 'seller_mid' in d:
            o.seller_mid = d['seller_mid']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'seller_telephone' in d:
            o.seller_telephone = d['seller_telephone']
        return o


