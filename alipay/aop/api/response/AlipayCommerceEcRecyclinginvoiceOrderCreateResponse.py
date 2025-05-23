#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceOrderCreateResponse, self).__init__()
        self._collection_invoice_page_alipay_url = None
        self._collection_invoice_page_url = None
        self._memo = None
        self._order_id = None
        self._outer_order_id = None
        self._payment_invoice_page_alipay_url = None
        self._payment_invoice_page_url = None
        self._payment_invoice_qr_code_url = None
        self._tax_authority_remind = None

    @property
    def collection_invoice_page_alipay_url(self):
        return self._collection_invoice_page_alipay_url

    @collection_invoice_page_alipay_url.setter
    def collection_invoice_page_alipay_url(self, value):
        self._collection_invoice_page_alipay_url = value
    @property
    def collection_invoice_page_url(self):
        return self._collection_invoice_page_url

    @collection_invoice_page_url.setter
    def collection_invoice_page_url(self, value):
        self._collection_invoice_page_url = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def outer_order_id(self):
        return self._outer_order_id

    @outer_order_id.setter
    def outer_order_id(self, value):
        self._outer_order_id = value
    @property
    def payment_invoice_page_alipay_url(self):
        return self._payment_invoice_page_alipay_url

    @payment_invoice_page_alipay_url.setter
    def payment_invoice_page_alipay_url(self, value):
        self._payment_invoice_page_alipay_url = value
    @property
    def payment_invoice_page_url(self):
        return self._payment_invoice_page_url

    @payment_invoice_page_url.setter
    def payment_invoice_page_url(self, value):
        self._payment_invoice_page_url = value
    @property
    def payment_invoice_qr_code_url(self):
        return self._payment_invoice_qr_code_url

    @payment_invoice_qr_code_url.setter
    def payment_invoice_qr_code_url(self, value):
        self._payment_invoice_qr_code_url = value
    @property
    def tax_authority_remind(self):
        return self._tax_authority_remind

    @tax_authority_remind.setter
    def tax_authority_remind(self, value):
        self._tax_authority_remind = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceOrderCreateResponse, self).parse_response_content(response_content)
        if 'collection_invoice_page_alipay_url' in response:
            self.collection_invoice_page_alipay_url = response['collection_invoice_page_alipay_url']
        if 'collection_invoice_page_url' in response:
            self.collection_invoice_page_url = response['collection_invoice_page_url']
        if 'memo' in response:
            self.memo = response['memo']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'outer_order_id' in response:
            self.outer_order_id = response['outer_order_id']
        if 'payment_invoice_page_alipay_url' in response:
            self.payment_invoice_page_alipay_url = response['payment_invoice_page_alipay_url']
        if 'payment_invoice_page_url' in response:
            self.payment_invoice_page_url = response['payment_invoice_page_url']
        if 'payment_invoice_qr_code_url' in response:
            self.payment_invoice_qr_code_url = response['payment_invoice_qr_code_url']
        if 'tax_authority_remind' in response:
            self.tax_authority_remind = response['tax_authority_remind']
