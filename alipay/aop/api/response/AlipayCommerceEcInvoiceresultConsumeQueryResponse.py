#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceMerchantItem import InvoiceMerchantItem


class AlipayCommerceEcInvoiceresultConsumeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcInvoiceresultConsumeQueryResponse, self).__init__()
        self._alipay_trade_no = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._buyer_tel = None
        self._fail_message = None
        self._invoice_amount = None
        self._invoice_amount_without_tax = None
        self._invoice_apply_id = None
        self._invoice_date = None
        self._invoice_item_list = None
        self._invoice_kind = None
        self._invoice_no = None
        self._invoice_red_reason = None
        self._invoice_status = None
        self._invoice_tax_amount = None
        self._invoice_type = None
        self._outer_apply_id = None
        self._pdf_file_url = None
        self._related_blue_invoice_no = None
        self._remark = None
        self._seller_name = None
        self._seller_tax_no = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
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
    def fail_message(self):
        return self._fail_message

    @fail_message.setter
    def fail_message(self, value):
        self._fail_message = value
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
    def invoice_apply_id(self):
        return self._invoice_apply_id

    @invoice_apply_id.setter
    def invoice_apply_id(self, value):
        self._invoice_apply_id = value
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
                if isinstance(i, InvoiceMerchantItem):
                    self._invoice_item_list.append(i)
                else:
                    self._invoice_item_list.append(InvoiceMerchantItem.from_alipay_dict(i))
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
    def invoice_red_reason(self):
        return self._invoice_red_reason

    @invoice_red_reason.setter
    def invoice_red_reason(self, value):
        self._invoice_red_reason = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
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
    def outer_apply_id(self):
        return self._outer_apply_id

    @outer_apply_id.setter
    def outer_apply_id(self, value):
        self._outer_apply_id = value
    @property
    def pdf_file_url(self):
        return self._pdf_file_url

    @pdf_file_url.setter
    def pdf_file_url(self, value):
        self._pdf_file_url = value
    @property
    def related_blue_invoice_no(self):
        return self._related_blue_invoice_no

    @related_blue_invoice_no.setter
    def related_blue_invoice_no(self, value):
        self._related_blue_invoice_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcInvoiceresultConsumeQueryResponse, self).parse_response_content(response_content)
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
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
        if 'fail_message' in response:
            self.fail_message = response['fail_message']
        if 'invoice_amount' in response:
            self.invoice_amount = response['invoice_amount']
        if 'invoice_amount_without_tax' in response:
            self.invoice_amount_without_tax = response['invoice_amount_without_tax']
        if 'invoice_apply_id' in response:
            self.invoice_apply_id = response['invoice_apply_id']
        if 'invoice_date' in response:
            self.invoice_date = response['invoice_date']
        if 'invoice_item_list' in response:
            self.invoice_item_list = response['invoice_item_list']
        if 'invoice_kind' in response:
            self.invoice_kind = response['invoice_kind']
        if 'invoice_no' in response:
            self.invoice_no = response['invoice_no']
        if 'invoice_red_reason' in response:
            self.invoice_red_reason = response['invoice_red_reason']
        if 'invoice_status' in response:
            self.invoice_status = response['invoice_status']
        if 'invoice_tax_amount' in response:
            self.invoice_tax_amount = response['invoice_tax_amount']
        if 'invoice_type' in response:
            self.invoice_type = response['invoice_type']
        if 'outer_apply_id' in response:
            self.outer_apply_id = response['outer_apply_id']
        if 'pdf_file_url' in response:
            self.pdf_file_url = response['pdf_file_url']
        if 'related_blue_invoice_no' in response:
            self.related_blue_invoice_no = response['related_blue_invoice_no']
        if 'remark' in response:
            self.remark = response['remark']
        if 'seller_name' in response:
            self.seller_name = response['seller_name']
        if 'seller_tax_no' in response:
            self.seller_tax_no = response['seller_tax_no']
