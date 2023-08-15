#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayCommerceEcTcnInvoiceapplyUploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._apply_id = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._buyer_tel = None
        self._check_code = None
        self._file_type = None
        self._invoice_amount = None
        self._invoice_amount_without_tax = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_kind = None
        self._invoice_no = None
        self._invoice_tax_amount = None
        self._invoice_tax_rate = None
        self._invoice_type = None
        self._original_invoice_code = None
        self._original_invoice_no = None
        self._red_remarks = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_name = None
        self._seller_tax_no = None
        self._seller_tel = None
        self._file_data = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

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
    def file_data(self):
        return self._file_data

    @file_data.setter
    def file_data(self, value):
        if not isinstance(value, FileItem):
            return
        self._file_data = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.commerce.ec.tcn.invoiceapply.upload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = json.dumps(obj=self.apply_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['apply_id'] = self.apply_id
        if self.buyer_address:
            if hasattr(self.buyer_address, 'to_alipay_dict'):
                params['buyer_address'] = json.dumps(obj=self.buyer_address.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_address'] = self.buyer_address
        if self.buyer_bank_account:
            if hasattr(self.buyer_bank_account, 'to_alipay_dict'):
                params['buyer_bank_account'] = json.dumps(obj=self.buyer_bank_account.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_bank_account'] = self.buyer_bank_account
        if self.buyer_bank_name:
            if hasattr(self.buyer_bank_name, 'to_alipay_dict'):
                params['buyer_bank_name'] = json.dumps(obj=self.buyer_bank_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_bank_name'] = self.buyer_bank_name
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = json.dumps(obj=self.buyer_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_name'] = self.buyer_name
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = json.dumps(obj=self.buyer_tax_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.buyer_tel:
            if hasattr(self.buyer_tel, 'to_alipay_dict'):
                params['buyer_tel'] = json.dumps(obj=self.buyer_tel.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_tel'] = self.buyer_tel
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = json.dumps(obj=self.check_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['check_code'] = self.check_code
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = json.dumps(obj=self.file_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['file_type'] = self.file_type
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = json.dumps(obj=self.invoice_amount.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.invoice_amount_without_tax:
            if hasattr(self.invoice_amount_without_tax, 'to_alipay_dict'):
                params['invoice_amount_without_tax'] = json.dumps(obj=self.invoice_amount_without_tax.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_amount_without_tax'] = self.invoice_amount_without_tax
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = json.dumps(obj=self.invoice_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = json.dumps(obj=self.invoice_date.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = json.dumps(obj=self.invoice_kind.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = json.dumps(obj=self.invoice_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_tax_amount:
            if hasattr(self.invoice_tax_amount, 'to_alipay_dict'):
                params['invoice_tax_amount'] = json.dumps(obj=self.invoice_tax_amount.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_tax_amount'] = self.invoice_tax_amount
        if self.invoice_tax_rate:
            if hasattr(self.invoice_tax_rate, 'to_alipay_dict'):
                params['invoice_tax_rate'] = json.dumps(obj=self.invoice_tax_rate.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_tax_rate'] = self.invoice_tax_rate
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = json.dumps(obj=self.invoice_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_type'] = self.invoice_type
        if self.original_invoice_code:
            if hasattr(self.original_invoice_code, 'to_alipay_dict'):
                params['original_invoice_code'] = json.dumps(obj=self.original_invoice_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['original_invoice_code'] = self.original_invoice_code
        if self.original_invoice_no:
            if hasattr(self.original_invoice_no, 'to_alipay_dict'):
                params['original_invoice_no'] = json.dumps(obj=self.original_invoice_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['original_invoice_no'] = self.original_invoice_no
        if self.red_remarks:
            if hasattr(self.red_remarks, 'to_alipay_dict'):
                params['red_remarks'] = json.dumps(obj=self.red_remarks.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['red_remarks'] = self.red_remarks
        if self.seller_address:
            if hasattr(self.seller_address, 'to_alipay_dict'):
                params['seller_address'] = json.dumps(obj=self.seller_address.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_address'] = self.seller_address
        if self.seller_bank_account:
            if hasattr(self.seller_bank_account, 'to_alipay_dict'):
                params['seller_bank_account'] = json.dumps(obj=self.seller_bank_account.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_bank_account'] = self.seller_bank_account
        if self.seller_bank_name:
            if hasattr(self.seller_bank_name, 'to_alipay_dict'):
                params['seller_bank_name'] = json.dumps(obj=self.seller_bank_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_bank_name'] = self.seller_bank_name
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = json.dumps(obj=self.seller_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_name'] = self.seller_name
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = json.dumps(obj=self.seller_tax_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_tax_no'] = self.seller_tax_no
        if self.seller_tel:
            if hasattr(self.seller_tel, 'to_alipay_dict'):
                params['seller_tel'] = json.dumps(obj=self.seller_tel.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_tel'] = self.seller_tel
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.file_data:
            multipart_params['file_data'] = self.file_data
        return multipart_params
