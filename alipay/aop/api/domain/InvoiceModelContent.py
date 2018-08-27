#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceItemContent import InvoiceItemContent
from alipay.aop.api.domain.InvoiceTitleModel import InvoiceTitleModel


class InvoiceModelContent(object):

    def __init__(self):
        self._extend_fields = None
        self._file_download_type = None
        self._file_download_url = None
        self._invoice_amount = None
        self._invoice_code = None
        self._invoice_content = None
        self._invoice_date = None
        self._invoice_fake_code = None
        self._invoice_file_data = None
        self._invoice_img_url = None
        self._invoice_no = None
        self._invoice_operator = None
        self._invoice_title = None
        self._invoice_type = None
        self._original_blue_invoice_code = None
        self._original_blue_invoice_no = None
        self._out_biz_no = None
        self._out_invoice_id = None
        self._register_address = None
        self._register_bank_account = None
        self._register_bank_name = None
        self._register_name = None
        self._register_no = None
        self._register_phone_no = None
        self._sum_amount = None
        self._tax_amount = None
        self._tax_type = None
        self._user_id = None

    @property
    def extend_fields(self):
        return self._extend_fields

    @extend_fields.setter
    def extend_fields(self, value):
        self._extend_fields = value
    @property
    def file_download_type(self):
        return self._file_download_type

    @file_download_type.setter
    def file_download_type(self, value):
        self._file_download_type = value
    @property
    def file_download_url(self):
        return self._file_download_url

    @file_download_url.setter
    def file_download_url(self, value):
        self._file_download_url = value
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
    def invoice_content(self):
        return self._invoice_content

    @invoice_content.setter
    def invoice_content(self, value):
        if isinstance(value, list):
            self._invoice_content = list()
            for i in value:
                if isinstance(i, InvoiceItemContent):
                    self._invoice_content.append(i)
                else:
                    self._invoice_content.append(InvoiceItemContent.from_alipay_dict(i))
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_fake_code(self):
        return self._invoice_fake_code

    @invoice_fake_code.setter
    def invoice_fake_code(self, value):
        self._invoice_fake_code = value
    @property
    def invoice_file_data(self):
        return self._invoice_file_data

    @invoice_file_data.setter
    def invoice_file_data(self, value):
        self._invoice_file_data = value
    @property
    def invoice_img_url(self):
        return self._invoice_img_url

    @invoice_img_url.setter
    def invoice_img_url(self, value):
        self._invoice_img_url = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_operator(self):
        return self._invoice_operator

    @invoice_operator.setter
    def invoice_operator(self, value):
        self._invoice_operator = value
    @property
    def invoice_title(self):
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, value):
        if isinstance(value, InvoiceTitleModel):
            self._invoice_title = value
        else:
            self._invoice_title = InvoiceTitleModel.from_alipay_dict(value)
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def original_blue_invoice_code(self):
        return self._original_blue_invoice_code

    @original_blue_invoice_code.setter
    def original_blue_invoice_code(self, value):
        self._original_blue_invoice_code = value
    @property
    def original_blue_invoice_no(self):
        return self._original_blue_invoice_no

    @original_blue_invoice_no.setter
    def original_blue_invoice_no(self, value):
        self._original_blue_invoice_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_invoice_id(self):
        return self._out_invoice_id

    @out_invoice_id.setter
    def out_invoice_id(self, value):
        self._out_invoice_id = value
    @property
    def register_address(self):
        return self._register_address

    @register_address.setter
    def register_address(self, value):
        self._register_address = value
    @property
    def register_bank_account(self):
        return self._register_bank_account

    @register_bank_account.setter
    def register_bank_account(self, value):
        self._register_bank_account = value
    @property
    def register_bank_name(self):
        return self._register_bank_name

    @register_bank_name.setter
    def register_bank_name(self, value):
        self._register_bank_name = value
    @property
    def register_name(self):
        return self._register_name

    @register_name.setter
    def register_name(self, value):
        self._register_name = value
    @property
    def register_no(self):
        return self._register_no

    @register_no.setter
    def register_no(self, value):
        self._register_no = value
    @property
    def register_phone_no(self):
        return self._register_phone_no

    @register_phone_no.setter
    def register_phone_no(self, value):
        self._register_phone_no = value
    @property
    def sum_amount(self):
        return self._sum_amount

    @sum_amount.setter
    def sum_amount(self, value):
        self._sum_amount = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, value):
        self._tax_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend_fields:
            if hasattr(self.extend_fields, 'to_alipay_dict'):
                params['extend_fields'] = self.extend_fields.to_alipay_dict()
            else:
                params['extend_fields'] = self.extend_fields
        if self.file_download_type:
            if hasattr(self.file_download_type, 'to_alipay_dict'):
                params['file_download_type'] = self.file_download_type.to_alipay_dict()
            else:
                params['file_download_type'] = self.file_download_type
        if self.file_download_url:
            if hasattr(self.file_download_url, 'to_alipay_dict'):
                params['file_download_url'] = self.file_download_url.to_alipay_dict()
            else:
                params['file_download_url'] = self.file_download_url
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
        if self.invoice_fake_code:
            if hasattr(self.invoice_fake_code, 'to_alipay_dict'):
                params['invoice_fake_code'] = self.invoice_fake_code.to_alipay_dict()
            else:
                params['invoice_fake_code'] = self.invoice_fake_code
        if self.invoice_file_data:
            if hasattr(self.invoice_file_data, 'to_alipay_dict'):
                params['invoice_file_data'] = self.invoice_file_data.to_alipay_dict()
            else:
                params['invoice_file_data'] = self.invoice_file_data
        if self.invoice_img_url:
            if hasattr(self.invoice_img_url, 'to_alipay_dict'):
                params['invoice_img_url'] = self.invoice_img_url.to_alipay_dict()
            else:
                params['invoice_img_url'] = self.invoice_img_url
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_operator:
            if hasattr(self.invoice_operator, 'to_alipay_dict'):
                params['invoice_operator'] = self.invoice_operator.to_alipay_dict()
            else:
                params['invoice_operator'] = self.invoice_operator
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
        if self.original_blue_invoice_code:
            if hasattr(self.original_blue_invoice_code, 'to_alipay_dict'):
                params['original_blue_invoice_code'] = self.original_blue_invoice_code.to_alipay_dict()
            else:
                params['original_blue_invoice_code'] = self.original_blue_invoice_code
        if self.original_blue_invoice_no:
            if hasattr(self.original_blue_invoice_no, 'to_alipay_dict'):
                params['original_blue_invoice_no'] = self.original_blue_invoice_no.to_alipay_dict()
            else:
                params['original_blue_invoice_no'] = self.original_blue_invoice_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_invoice_id:
            if hasattr(self.out_invoice_id, 'to_alipay_dict'):
                params['out_invoice_id'] = self.out_invoice_id.to_alipay_dict()
            else:
                params['out_invoice_id'] = self.out_invoice_id
        if self.register_address:
            if hasattr(self.register_address, 'to_alipay_dict'):
                params['register_address'] = self.register_address.to_alipay_dict()
            else:
                params['register_address'] = self.register_address
        if self.register_bank_account:
            if hasattr(self.register_bank_account, 'to_alipay_dict'):
                params['register_bank_account'] = self.register_bank_account.to_alipay_dict()
            else:
                params['register_bank_account'] = self.register_bank_account
        if self.register_bank_name:
            if hasattr(self.register_bank_name, 'to_alipay_dict'):
                params['register_bank_name'] = self.register_bank_name.to_alipay_dict()
            else:
                params['register_bank_name'] = self.register_bank_name
        if self.register_name:
            if hasattr(self.register_name, 'to_alipay_dict'):
                params['register_name'] = self.register_name.to_alipay_dict()
            else:
                params['register_name'] = self.register_name
        if self.register_no:
            if hasattr(self.register_no, 'to_alipay_dict'):
                params['register_no'] = self.register_no.to_alipay_dict()
            else:
                params['register_no'] = self.register_no
        if self.register_phone_no:
            if hasattr(self.register_phone_no, 'to_alipay_dict'):
                params['register_phone_no'] = self.register_phone_no.to_alipay_dict()
            else:
                params['register_phone_no'] = self.register_phone_no
        if self.sum_amount:
            if hasattr(self.sum_amount, 'to_alipay_dict'):
                params['sum_amount'] = self.sum_amount.to_alipay_dict()
            else:
                params['sum_amount'] = self.sum_amount
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_type:
            if hasattr(self.tax_type, 'to_alipay_dict'):
                params['tax_type'] = self.tax_type.to_alipay_dict()
            else:
                params['tax_type'] = self.tax_type
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
        o = InvoiceModelContent()
        if 'extend_fields' in d:
            o.extend_fields = d['extend_fields']
        if 'file_download_type' in d:
            o.file_download_type = d['file_download_type']
        if 'file_download_url' in d:
            o.file_download_url = d['file_download_url']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_content' in d:
            o.invoice_content = d['invoice_content']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_fake_code' in d:
            o.invoice_fake_code = d['invoice_fake_code']
        if 'invoice_file_data' in d:
            o.invoice_file_data = d['invoice_file_data']
        if 'invoice_img_url' in d:
            o.invoice_img_url = d['invoice_img_url']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_operator' in d:
            o.invoice_operator = d['invoice_operator']
        if 'invoice_title' in d:
            o.invoice_title = d['invoice_title']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'original_blue_invoice_code' in d:
            o.original_blue_invoice_code = d['original_blue_invoice_code']
        if 'original_blue_invoice_no' in d:
            o.original_blue_invoice_no = d['original_blue_invoice_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_invoice_id' in d:
            o.out_invoice_id = d['out_invoice_id']
        if 'register_address' in d:
            o.register_address = d['register_address']
        if 'register_bank_account' in d:
            o.register_bank_account = d['register_bank_account']
        if 'register_bank_name' in d:
            o.register_bank_name = d['register_bank_name']
        if 'register_name' in d:
            o.register_name = d['register_name']
        if 'register_no' in d:
            o.register_no = d['register_no']
        if 'register_phone_no' in d:
            o.register_phone_no = d['register_phone_no']
        if 'sum_amount' in d:
            o.sum_amount = d['sum_amount']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


