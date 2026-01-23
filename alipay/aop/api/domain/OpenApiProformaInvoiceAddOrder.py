#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiBuyerInvoiceInfoOrder import OpenApiBuyerInvoiceInfoOrder
from alipay.aop.api.domain.OpenApiPaymentMethodOrder import OpenApiPaymentMethodOrder
from alipay.aop.api.domain.OpenApiProductInfoOrder import OpenApiProductInfoOrder
from alipay.aop.api.domain.OpenApiSellerInvoiceInfoOrder import OpenApiSellerInvoiceInfoOrder


class OpenApiProformaInvoiceAddOrder(object):

    def __init__(self):
        self._biz_id = None
        self._biz_no = None
        self._buyer_contact_email = None
        self._buyer_country = None
        self._buyer_info = None
        self._buyer_inst_id = None
        self._collect_ccy = None
        self._duty_free = None
        self._fee_end_dt = None
        self._fee_interval_format_str = None
        self._fee_start_dt = None
        self._invoice_date = None
        self._invoice_note = None
        self._invoice_type = None
        self._local_ccy = None
        self._memo = None
        self._operator = None
        self._order_way = None
        self._payment_method_order = None
        self._price_ccy = None
        self._product_info_orders = None
        self._received = None
        self._seller_info = None
        self._tax_rate = None
        self._tax_type = None
        self._without_bill = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def buyer_contact_email(self):
        return self._buyer_contact_email

    @buyer_contact_email.setter
    def buyer_contact_email(self, value):
        self._buyer_contact_email = value
    @property
    def buyer_country(self):
        return self._buyer_country

    @buyer_country.setter
    def buyer_country(self, value):
        self._buyer_country = value
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, OpenApiBuyerInvoiceInfoOrder):
            self._buyer_info = value
        else:
            self._buyer_info = OpenApiBuyerInvoiceInfoOrder.from_alipay_dict(value)
    @property
    def buyer_inst_id(self):
        return self._buyer_inst_id

    @buyer_inst_id.setter
    def buyer_inst_id(self, value):
        self._buyer_inst_id = value
    @property
    def collect_ccy(self):
        return self._collect_ccy

    @collect_ccy.setter
    def collect_ccy(self, value):
        self._collect_ccy = value
    @property
    def duty_free(self):
        return self._duty_free

    @duty_free.setter
    def duty_free(self, value):
        self._duty_free = value
    @property
    def fee_end_dt(self):
        return self._fee_end_dt

    @fee_end_dt.setter
    def fee_end_dt(self, value):
        self._fee_end_dt = value
    @property
    def fee_interval_format_str(self):
        return self._fee_interval_format_str

    @fee_interval_format_str.setter
    def fee_interval_format_str(self, value):
        self._fee_interval_format_str = value
    @property
    def fee_start_dt(self):
        return self._fee_start_dt

    @fee_start_dt.setter
    def fee_start_dt(self, value):
        self._fee_start_dt = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_note(self):
        return self._invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self._invoice_note = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def local_ccy(self):
        return self._local_ccy

    @local_ccy.setter
    def local_ccy(self, value):
        self._local_ccy = value
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
    def order_way(self):
        return self._order_way

    @order_way.setter
    def order_way(self, value):
        self._order_way = value
    @property
    def payment_method_order(self):
        return self._payment_method_order

    @payment_method_order.setter
    def payment_method_order(self, value):
        if isinstance(value, OpenApiPaymentMethodOrder):
            self._payment_method_order = value
        else:
            self._payment_method_order = OpenApiPaymentMethodOrder.from_alipay_dict(value)
    @property
    def price_ccy(self):
        return self._price_ccy

    @price_ccy.setter
    def price_ccy(self, value):
        self._price_ccy = value
    @property
    def product_info_orders(self):
        return self._product_info_orders

    @product_info_orders.setter
    def product_info_orders(self, value):
        if isinstance(value, list):
            self._product_info_orders = list()
            for i in value:
                if isinstance(i, OpenApiProductInfoOrder):
                    self._product_info_orders.append(i)
                else:
                    self._product_info_orders.append(OpenApiProductInfoOrder.from_alipay_dict(i))
    @property
    def received(self):
        return self._received

    @received.setter
    def received(self, value):
        self._received = value
    @property
    def seller_info(self):
        return self._seller_info

    @seller_info.setter
    def seller_info(self, value):
        if isinstance(value, OpenApiSellerInvoiceInfoOrder):
            self._seller_info = value
        else:
            self._seller_info = OpenApiSellerInvoiceInfoOrder.from_alipay_dict(value)
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, value):
        self._tax_type = value
    @property
    def without_bill(self):
        return self._without_bill

    @without_bill.setter
    def without_bill(self, value):
        self._without_bill = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.buyer_contact_email:
            if hasattr(self.buyer_contact_email, 'to_alipay_dict'):
                params['buyer_contact_email'] = self.buyer_contact_email.to_alipay_dict()
            else:
                params['buyer_contact_email'] = self.buyer_contact_email
        if self.buyer_country:
            if hasattr(self.buyer_country, 'to_alipay_dict'):
                params['buyer_country'] = self.buyer_country.to_alipay_dict()
            else:
                params['buyer_country'] = self.buyer_country
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.buyer_inst_id:
            if hasattr(self.buyer_inst_id, 'to_alipay_dict'):
                params['buyer_inst_id'] = self.buyer_inst_id.to_alipay_dict()
            else:
                params['buyer_inst_id'] = self.buyer_inst_id
        if self.collect_ccy:
            if hasattr(self.collect_ccy, 'to_alipay_dict'):
                params['collect_ccy'] = self.collect_ccy.to_alipay_dict()
            else:
                params['collect_ccy'] = self.collect_ccy
        if self.duty_free:
            if hasattr(self.duty_free, 'to_alipay_dict'):
                params['duty_free'] = self.duty_free.to_alipay_dict()
            else:
                params['duty_free'] = self.duty_free
        if self.fee_end_dt:
            if hasattr(self.fee_end_dt, 'to_alipay_dict'):
                params['fee_end_dt'] = self.fee_end_dt.to_alipay_dict()
            else:
                params['fee_end_dt'] = self.fee_end_dt
        if self.fee_interval_format_str:
            if hasattr(self.fee_interval_format_str, 'to_alipay_dict'):
                params['fee_interval_format_str'] = self.fee_interval_format_str.to_alipay_dict()
            else:
                params['fee_interval_format_str'] = self.fee_interval_format_str
        if self.fee_start_dt:
            if hasattr(self.fee_start_dt, 'to_alipay_dict'):
                params['fee_start_dt'] = self.fee_start_dt.to_alipay_dict()
            else:
                params['fee_start_dt'] = self.fee_start_dt
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_note:
            if hasattr(self.invoice_note, 'to_alipay_dict'):
                params['invoice_note'] = self.invoice_note.to_alipay_dict()
            else:
                params['invoice_note'] = self.invoice_note
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.local_ccy:
            if hasattr(self.local_ccy, 'to_alipay_dict'):
                params['local_ccy'] = self.local_ccy.to_alipay_dict()
            else:
                params['local_ccy'] = self.local_ccy
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
        if self.order_way:
            if hasattr(self.order_way, 'to_alipay_dict'):
                params['order_way'] = self.order_way.to_alipay_dict()
            else:
                params['order_way'] = self.order_way
        if self.payment_method_order:
            if hasattr(self.payment_method_order, 'to_alipay_dict'):
                params['payment_method_order'] = self.payment_method_order.to_alipay_dict()
            else:
                params['payment_method_order'] = self.payment_method_order
        if self.price_ccy:
            if hasattr(self.price_ccy, 'to_alipay_dict'):
                params['price_ccy'] = self.price_ccy.to_alipay_dict()
            else:
                params['price_ccy'] = self.price_ccy
        if self.product_info_orders:
            if isinstance(self.product_info_orders, list):
                for i in range(0, len(self.product_info_orders)):
                    element = self.product_info_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_info_orders[i] = element.to_alipay_dict()
            if hasattr(self.product_info_orders, 'to_alipay_dict'):
                params['product_info_orders'] = self.product_info_orders.to_alipay_dict()
            else:
                params['product_info_orders'] = self.product_info_orders
        if self.received:
            if hasattr(self.received, 'to_alipay_dict'):
                params['received'] = self.received.to_alipay_dict()
            else:
                params['received'] = self.received
        if self.seller_info:
            if hasattr(self.seller_info, 'to_alipay_dict'):
                params['seller_info'] = self.seller_info.to_alipay_dict()
            else:
                params['seller_info'] = self.seller_info
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tax_type:
            if hasattr(self.tax_type, 'to_alipay_dict'):
                params['tax_type'] = self.tax_type.to_alipay_dict()
            else:
                params['tax_type'] = self.tax_type
        if self.without_bill:
            if hasattr(self.without_bill, 'to_alipay_dict'):
                params['without_bill'] = self.without_bill.to_alipay_dict()
            else:
                params['without_bill'] = self.without_bill
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiProformaInvoiceAddOrder()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'buyer_contact_email' in d:
            o.buyer_contact_email = d['buyer_contact_email']
        if 'buyer_country' in d:
            o.buyer_country = d['buyer_country']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'buyer_inst_id' in d:
            o.buyer_inst_id = d['buyer_inst_id']
        if 'collect_ccy' in d:
            o.collect_ccy = d['collect_ccy']
        if 'duty_free' in d:
            o.duty_free = d['duty_free']
        if 'fee_end_dt' in d:
            o.fee_end_dt = d['fee_end_dt']
        if 'fee_interval_format_str' in d:
            o.fee_interval_format_str = d['fee_interval_format_str']
        if 'fee_start_dt' in d:
            o.fee_start_dt = d['fee_start_dt']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'local_ccy' in d:
            o.local_ccy = d['local_ccy']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'order_way' in d:
            o.order_way = d['order_way']
        if 'payment_method_order' in d:
            o.payment_method_order = d['payment_method_order']
        if 'price_ccy' in d:
            o.price_ccy = d['price_ccy']
        if 'product_info_orders' in d:
            o.product_info_orders = d['product_info_orders']
        if 'received' in d:
            o.received = d['received']
        if 'seller_info' in d:
            o.seller_info = d['seller_info']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        if 'without_bill' in d:
            o.without_bill = d['without_bill']
        return o


