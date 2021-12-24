#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InputInvoiceBillLinkOrderDTO import InputInvoiceBillLinkOrderDTO
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.ApInvoiceLineOrderRequest import ApInvoiceLineOrderRequest
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class RelateInputInvoiceOrderDTO(object):

    def __init__(self):
        self._attachment_name = None
        self._attachment_oss_key = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_inst_id = None
        self._buyer_invoice_title = None
        self._buyer_tax_no = None
        self._buyer_telephone = None
        self._input_invoice_bill_link_order_list = None
        self._inst_id = None
        self._invoice_amt = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_line_orders = None
        self._invoice_material = None
        self._invoice_no = None
        self._invoice_note = None
        self._invoice_receive_date = None
        self._invoice_source = None
        self._invoice_type = None
        self._ip_role_id = None
        self._memo = None
        self._operator = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_company_name = None
        self._seller_ip_role_id = None
        self._seller_mid = None
        self._seller_tax_no = None
        self._seller_telephone = None
        self._tax_amt = None
        self._tax_rate = None

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
    def input_invoice_bill_link_order_list(self):
        return self._input_invoice_bill_link_order_list

    @input_invoice_bill_link_order_list.setter
    def input_invoice_bill_link_order_list(self, value):
        if isinstance(value, list):
            self._input_invoice_bill_link_order_list = list()
            for i in value:
                if isinstance(i, InputInvoiceBillLinkOrderDTO):
                    self._input_invoice_bill_link_order_list.append(i)
                else:
                    self._input_invoice_bill_link_order_list.append(InputInvoiceBillLinkOrderDTO.from_alipay_dict(i))
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
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
    def invoice_line_orders(self):
        return self._invoice_line_orders

    @invoice_line_orders.setter
    def invoice_line_orders(self, value):
        if isinstance(value, list):
            self._invoice_line_orders = list()
            for i in value:
                if isinstance(i, ApInvoiceLineOrderRequest):
                    self._invoice_line_orders.append(i)
                else:
                    self._invoice_line_orders.append(ApInvoiceLineOrderRequest.from_alipay_dict(i))
    @property
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
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
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
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
    @property
    def tax_amt(self):
        return self._tax_amt

    @tax_amt.setter
    def tax_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_amt = value
        else:
            self._tax_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.input_invoice_bill_link_order_list:
            if isinstance(self.input_invoice_bill_link_order_list, list):
                for i in range(0, len(self.input_invoice_bill_link_order_list)):
                    element = self.input_invoice_bill_link_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.input_invoice_bill_link_order_list[i] = element.to_alipay_dict()
            if hasattr(self.input_invoice_bill_link_order_list, 'to_alipay_dict'):
                params['input_invoice_bill_link_order_list'] = self.input_invoice_bill_link_order_list.to_alipay_dict()
            else:
                params['input_invoice_bill_link_order_list'] = self.input_invoice_bill_link_order_list
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
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
        if self.invoice_line_orders:
            if isinstance(self.invoice_line_orders, list):
                for i in range(0, len(self.invoice_line_orders)):
                    element = self.invoice_line_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_line_orders[i] = element.to_alipay_dict()
            if hasattr(self.invoice_line_orders, 'to_alipay_dict'):
                params['invoice_line_orders'] = self.invoice_line_orders.to_alipay_dict()
            else:
                params['invoice_line_orders'] = self.invoice_line_orders
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
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
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
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
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RelateInputInvoiceOrderDTO()
        if 'attachment_name' in d:
            o.attachment_name = d['attachment_name']
        if 'attachment_oss_key' in d:
            o.attachment_oss_key = d['attachment_oss_key']
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
        if 'input_invoice_bill_link_order_list' in d:
            o.input_invoice_bill_link_order_list = d['input_invoice_bill_link_order_list']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_line_orders' in d:
            o.invoice_line_orders = d['invoice_line_orders']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
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
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
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
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


