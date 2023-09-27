#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenInvoiceApplyDetail import OpenInvoiceApplyDetail
from alipay.aop.api.domain.OpenInvoiceTravelInfo import OpenInvoiceTravelInfo


class AlipayCommerceEcTcnOpeninvoiceapplySubmitModel(object):

    def __init__(self):
        self._apply_detail_list = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._buyer_tel = None
        self._industry_type = None
        self._invoice_amount = None
        self._invoice_type = None
        self._platform_apply_id = None
        self._travel_info_list = None

    @property
    def apply_detail_list(self):
        return self._apply_detail_list

    @apply_detail_list.setter
    def apply_detail_list(self, value):
        if isinstance(value, list):
            self._apply_detail_list = list()
            for i in value:
                if isinstance(i, OpenInvoiceApplyDetail):
                    self._apply_detail_list.append(i)
                else:
                    self._apply_detail_list.append(OpenInvoiceApplyDetail.from_alipay_dict(i))
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
    def industry_type(self):
        return self._industry_type

    @industry_type.setter
    def industry_type(self, value):
        self._industry_type = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def platform_apply_id(self):
        return self._platform_apply_id

    @platform_apply_id.setter
    def platform_apply_id(self, value):
        self._platform_apply_id = value
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
        if self.apply_detail_list:
            if isinstance(self.apply_detail_list, list):
                for i in range(0, len(self.apply_detail_list)):
                    element = self.apply_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_detail_list, 'to_alipay_dict'):
                params['apply_detail_list'] = self.apply_detail_list.to_alipay_dict()
            else:
                params['apply_detail_list'] = self.apply_detail_list
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
        if self.industry_type:
            if hasattr(self.industry_type, 'to_alipay_dict'):
                params['industry_type'] = self.industry_type.to_alipay_dict()
            else:
                params['industry_type'] = self.industry_type
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.platform_apply_id:
            if hasattr(self.platform_apply_id, 'to_alipay_dict'):
                params['platform_apply_id'] = self.platform_apply_id.to_alipay_dict()
            else:
                params['platform_apply_id'] = self.platform_apply_id
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
        o = AlipayCommerceEcTcnOpeninvoiceapplySubmitModel()
        if 'apply_detail_list' in d:
            o.apply_detail_list = d['apply_detail_list']
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
        if 'industry_type' in d:
            o.industry_type = d['industry_type']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'platform_apply_id' in d:
            o.platform_apply_id = d['platform_apply_id']
        if 'travel_info_list' in d:
            o.travel_info_list = d['travel_info_list']
        return o


