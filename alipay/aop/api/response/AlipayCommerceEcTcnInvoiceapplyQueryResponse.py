#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenInvoiceTravelInfo import OpenInvoiceTravelInfo


class AlipayCommerceEcTcnInvoiceapplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcTcnInvoiceapplyQueryResponse, self).__init__()
        self._apply_id = None
        self._apply_status = None
        self._apply_time = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._buyer_tel = None
        self._failed_reason = None
        self._invoice_amount = None
        self._invoice_kind = None
        self._invoice_type = None
        self._item_name = None
        self._item_tax_code = None
        self._item_tax_rate = None
        self._item_unit = None
        self._platform_apply_id = None
        self._travel_info_list = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
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
    def failed_reason(self):
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, value):
        self._failed_reason = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_tax_code(self):
        return self._item_tax_code

    @item_tax_code.setter
    def item_tax_code(self, value):
        self._item_tax_code = value
    @property
    def item_tax_rate(self):
        return self._item_tax_rate

    @item_tax_rate.setter
    def item_tax_rate(self, value):
        self._item_tax_rate = value
    @property
    def item_unit(self):
        return self._item_unit

    @item_unit.setter
    def item_unit(self, value):
        self._item_unit = value
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
        if isinstance(value, OpenInvoiceTravelInfo):
            self._travel_info_list = value
        else:
            self._travel_info_list = OpenInvoiceTravelInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcTcnInvoiceapplyQueryResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'apply_status' in response:
            self.apply_status = response['apply_status']
        if 'apply_time' in response:
            self.apply_time = response['apply_time']
        if 'buyer_address' in response:
            self.buyer_address = response['buyer_address']
        if 'buyer_bank_account' in response:
            self.buyer_bank_account = response['buyer_bank_account']
        if 'buyer_bank_name' in response:
            self.buyer_bank_name = response['buyer_bank_name']
        if 'buyer_name' in response:
            self.buyer_name = response['buyer_name']
        if 'buyer_tax_no' in response:
            self.buyer_tax_no = response['buyer_tax_no']
        if 'buyer_tel' in response:
            self.buyer_tel = response['buyer_tel']
        if 'failed_reason' in response:
            self.failed_reason = response['failed_reason']
        if 'invoice_amount' in response:
            self.invoice_amount = response['invoice_amount']
        if 'invoice_kind' in response:
            self.invoice_kind = response['invoice_kind']
        if 'invoice_type' in response:
            self.invoice_type = response['invoice_type']
        if 'item_name' in response:
            self.item_name = response['item_name']
        if 'item_tax_code' in response:
            self.item_tax_code = response['item_tax_code']
        if 'item_tax_rate' in response:
            self.item_tax_rate = response['item_tax_rate']
        if 'item_unit' in response:
            self.item_unit = response['item_unit']
        if 'platform_apply_id' in response:
            self.platform_apply_id = response['platform_apply_id']
        if 'travel_info_list' in response:
            self.travel_info_list = response['travel_info_list']
