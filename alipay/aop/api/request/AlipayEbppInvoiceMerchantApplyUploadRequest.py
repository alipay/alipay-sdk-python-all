#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayEbppInvoiceMerchantApplyUploadRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._apply_id = None
        self._batch_id = None
        self._invoice_amount = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_file_type = None
        self._invoice_kind = None
        self._invoice_no = None
        self._invoice_type = None
        self._normal_invoice_code = None
        self._normal_invoice_no = None
        self._payee_address = None
        self._payee_bank_account_id = None
        self._payee_bank_name = None
        self._payee_name = None
        self._payee_phone = None
        self._payee_register_no = None
        self._payer_name = None
        self._payer_register_no = None
        self._sum_price = None
        self._sum_tax = None
        self._invoice_file_data = None
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
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
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
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_file_type(self):
        return self._invoice_file_type

    @invoice_file_type.setter
    def invoice_file_type(self, value):
        self._invoice_file_type = value
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
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payee_phone(self):
        return self._payee_phone

    @payee_phone.setter
    def payee_phone(self, value):
        self._payee_phone = value
    @property
    def payee_register_no(self):
        return self._payee_register_no

    @payee_register_no.setter
    def payee_register_no(self, value):
        self._payee_register_no = value
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

    @property
    def invoice_file_data(self):
        return self._invoice_file_data

    @invoice_file_data.setter
    def invoice_file_data(self, value):
        if not isinstance(value, FileItem):
            return
        self._invoice_file_data = value

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
        params[P_METHOD] = 'alipay.ebpp.invoice.merchant.apply.upload'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = json.dumps(obj=self.apply_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['apply_id'] = self.apply_id
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = json.dumps(obj=self.batch_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['batch_id'] = self.batch_id
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = json.dumps(obj=self.invoice_amount.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_amount'] = self.invoice_amount
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
        if self.invoice_file_type:
            if hasattr(self.invoice_file_type, 'to_alipay_dict'):
                params['invoice_file_type'] = json.dumps(obj=self.invoice_file_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_file_type'] = self.invoice_file_type
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
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = json.dumps(obj=self.invoice_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['invoice_type'] = self.invoice_type
        if self.normal_invoice_code:
            if hasattr(self.normal_invoice_code, 'to_alipay_dict'):
                params['normal_invoice_code'] = json.dumps(obj=self.normal_invoice_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['normal_invoice_code'] = self.normal_invoice_code
        if self.normal_invoice_no:
            if hasattr(self.normal_invoice_no, 'to_alipay_dict'):
                params['normal_invoice_no'] = json.dumps(obj=self.normal_invoice_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['normal_invoice_no'] = self.normal_invoice_no
        if self.payee_address:
            if hasattr(self.payee_address, 'to_alipay_dict'):
                params['payee_address'] = json.dumps(obj=self.payee_address.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payee_address'] = self.payee_address
        if self.payee_bank_account_id:
            if hasattr(self.payee_bank_account_id, 'to_alipay_dict'):
                params['payee_bank_account_id'] = json.dumps(obj=self.payee_bank_account_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payee_bank_account_id'] = self.payee_bank_account_id
        if self.payee_bank_name:
            if hasattr(self.payee_bank_name, 'to_alipay_dict'):
                params['payee_bank_name'] = json.dumps(obj=self.payee_bank_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payee_bank_name'] = self.payee_bank_name
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = json.dumps(obj=self.payee_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payee_name'] = self.payee_name
        if self.payee_phone:
            if hasattr(self.payee_phone, 'to_alipay_dict'):
                params['payee_phone'] = json.dumps(obj=self.payee_phone.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payee_phone'] = self.payee_phone
        if self.payee_register_no:
            if hasattr(self.payee_register_no, 'to_alipay_dict'):
                params['payee_register_no'] = json.dumps(obj=self.payee_register_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payee_register_no'] = self.payee_register_no
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = json.dumps(obj=self.payer_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payer_name'] = self.payer_name
        if self.payer_register_no:
            if hasattr(self.payer_register_no, 'to_alipay_dict'):
                params['payer_register_no'] = json.dumps(obj=self.payer_register_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['payer_register_no'] = self.payer_register_no
        if self.sum_price:
            if hasattr(self.sum_price, 'to_alipay_dict'):
                params['sum_price'] = json.dumps(obj=self.sum_price.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['sum_price'] = self.sum_price
        if self.sum_tax:
            if hasattr(self.sum_tax, 'to_alipay_dict'):
                params['sum_tax'] = json.dumps(obj=self.sum_tax.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['sum_tax'] = self.sum_tax
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
        if self.invoice_file_data:
            multipart_params['invoice_file_data'] = self.invoice_file_data
        return multipart_params
