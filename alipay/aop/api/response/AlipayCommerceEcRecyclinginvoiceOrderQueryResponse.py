#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderInvoice import OrderInvoice
from alipay.aop.api.domain.RecyclinginvoiceOrderItem import RecyclinginvoiceOrderItem
from alipay.aop.api.domain.OrderPayment import OrderPayment
from alipay.aop.api.domain.OrderTax import OrderTax


class AlipayCommerceEcRecyclinginvoiceOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceOrderQueryResponse, self).__init__()
        self._collection_invoice_page_alipay_url = None
        self._collection_invoice_page_url = None
        self._company_clerk_id = None
        self._company_supplier_id = None
        self._gmt_success = None
        self._memo = None
        self._order_amount = None
        self._order_id = None
        self._order_invoice_list = None
        self._order_item_list = None
        self._order_payment = None
        self._order_status = None
        self._order_tax_item_list = None
        self._outer_order_id = None
        self._payment_invoice_page_alipay_url = None
        self._payment_invoice_page_url = None
        self._payment_invoice_qr_code_url = None
        self._product_id = None
        self._seller_name = None
        self._seller_open_id = None
        self._seller_phone = None
        self._seller_user_id = None
        self._tax_no = None
        self._tax_total_amount = None

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
    def company_clerk_id(self):
        return self._company_clerk_id

    @company_clerk_id.setter
    def company_clerk_id(self, value):
        self._company_clerk_id = value
    @property
    def company_supplier_id(self):
        return self._company_supplier_id

    @company_supplier_id.setter
    def company_supplier_id(self, value):
        self._company_supplier_id = value
    @property
    def gmt_success(self):
        return self._gmt_success

    @gmt_success.setter
    def gmt_success(self, value):
        self._gmt_success = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_invoice_list(self):
        return self._order_invoice_list

    @order_invoice_list.setter
    def order_invoice_list(self, value):
        if isinstance(value, list):
            self._order_invoice_list = list()
            for i in value:
                if isinstance(i, OrderInvoice):
                    self._order_invoice_list.append(i)
                else:
                    self._order_invoice_list.append(OrderInvoice.from_alipay_dict(i))
    @property
    def order_item_list(self):
        return self._order_item_list

    @order_item_list.setter
    def order_item_list(self, value):
        if isinstance(value, list):
            self._order_item_list = list()
            for i in value:
                if isinstance(i, RecyclinginvoiceOrderItem):
                    self._order_item_list.append(i)
                else:
                    self._order_item_list.append(RecyclinginvoiceOrderItem.from_alipay_dict(i))
    @property
    def order_payment(self):
        return self._order_payment

    @order_payment.setter
    def order_payment(self, value):
        if isinstance(value, OrderPayment):
            self._order_payment = value
        else:
            self._order_payment = OrderPayment.from_alipay_dict(value)
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_tax_item_list(self):
        return self._order_tax_item_list

    @order_tax_item_list.setter
    def order_tax_item_list(self, value):
        if isinstance(value, list):
            self._order_tax_item_list = list()
            for i in value:
                if isinstance(i, OrderTax):
                    self._order_tax_item_list.append(i)
                else:
                    self._order_tax_item_list.append(OrderTax.from_alipay_dict(i))
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
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def seller_open_id(self):
        return self._seller_open_id

    @seller_open_id.setter
    def seller_open_id(self, value):
        self._seller_open_id = value
    @property
    def seller_phone(self):
        return self._seller_phone

    @seller_phone.setter
    def seller_phone(self, value):
        self._seller_phone = value
    @property
    def seller_user_id(self):
        return self._seller_user_id

    @seller_user_id.setter
    def seller_user_id(self, value):
        self._seller_user_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def tax_total_amount(self):
        return self._tax_total_amount

    @tax_total_amount.setter
    def tax_total_amount(self, value):
        self._tax_total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceOrderQueryResponse, self).parse_response_content(response_content)
        if 'collection_invoice_page_alipay_url' in response:
            self.collection_invoice_page_alipay_url = response['collection_invoice_page_alipay_url']
        if 'collection_invoice_page_url' in response:
            self.collection_invoice_page_url = response['collection_invoice_page_url']
        if 'company_clerk_id' in response:
            self.company_clerk_id = response['company_clerk_id']
        if 'company_supplier_id' in response:
            self.company_supplier_id = response['company_supplier_id']
        if 'gmt_success' in response:
            self.gmt_success = response['gmt_success']
        if 'memo' in response:
            self.memo = response['memo']
        if 'order_amount' in response:
            self.order_amount = response['order_amount']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_invoice_list' in response:
            self.order_invoice_list = response['order_invoice_list']
        if 'order_item_list' in response:
            self.order_item_list = response['order_item_list']
        if 'order_payment' in response:
            self.order_payment = response['order_payment']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_tax_item_list' in response:
            self.order_tax_item_list = response['order_tax_item_list']
        if 'outer_order_id' in response:
            self.outer_order_id = response['outer_order_id']
        if 'payment_invoice_page_alipay_url' in response:
            self.payment_invoice_page_alipay_url = response['payment_invoice_page_alipay_url']
        if 'payment_invoice_page_url' in response:
            self.payment_invoice_page_url = response['payment_invoice_page_url']
        if 'payment_invoice_qr_code_url' in response:
            self.payment_invoice_qr_code_url = response['payment_invoice_qr_code_url']
        if 'product_id' in response:
            self.product_id = response['product_id']
        if 'seller_name' in response:
            self.seller_name = response['seller_name']
        if 'seller_open_id' in response:
            self.seller_open_id = response['seller_open_id']
        if 'seller_phone' in response:
            self.seller_phone = response['seller_phone']
        if 'seller_user_id' in response:
            self.seller_user_id = response['seller_user_id']
        if 'tax_no' in response:
            self.tax_no = response['tax_no']
        if 'tax_total_amount' in response:
            self.tax_total_amount = response['tax_total_amount']
