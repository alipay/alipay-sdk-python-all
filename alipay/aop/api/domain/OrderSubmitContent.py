#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubOrderContent import SubOrderContent


class OrderSubmitContent(object):

    def __init__(self):
        self._consignee_name = None
        self._consignee_phone = None
        self._delivery_address = None
        self._discount_fee = None
        self._logistics_info = None
        self._order_status = None
        self._order_url = None
        self._origin_fee = None
        self._out_order_id = None
        self._pay_date = None
        self._pay_fee = None
        self._shop_name = None
        self._shop_url = None
        self._unimall_sub_orders = None

    @property
    def consignee_name(self):
        return self._consignee_name

    @consignee_name.setter
    def consignee_name(self, value):
        self._consignee_name = value
    @property
    def consignee_phone(self):
        return self._consignee_phone

    @consignee_phone.setter
    def consignee_phone(self, value):
        self._consignee_phone = value
    @property
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        self._delivery_address = value
    @property
    def discount_fee(self):
        return self._discount_fee

    @discount_fee.setter
    def discount_fee(self, value):
        self._discount_fee = value
    @property
    def logistics_info(self):
        return self._logistics_info

    @logistics_info.setter
    def logistics_info(self, value):
        self._logistics_info = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_url(self):
        return self._order_url

    @order_url.setter
    def order_url(self, value):
        self._order_url = value
    @property
    def origin_fee(self):
        return self._origin_fee

    @origin_fee.setter
    def origin_fee(self, value):
        self._origin_fee = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def pay_fee(self):
        return self._pay_fee

    @pay_fee.setter
    def pay_fee(self, value):
        self._pay_fee = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_url(self):
        return self._shop_url

    @shop_url.setter
    def shop_url(self, value):
        self._shop_url = value
    @property
    def unimall_sub_orders(self):
        return self._unimall_sub_orders

    @unimall_sub_orders.setter
    def unimall_sub_orders(self, value):
        if isinstance(value, list):
            self._unimall_sub_orders = list()
            for i in value:
                if isinstance(i, SubOrderContent):
                    self._unimall_sub_orders.append(i)
                else:
                    self._unimall_sub_orders.append(SubOrderContent.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.consignee_name:
            if hasattr(self.consignee_name, 'to_alipay_dict'):
                params['consignee_name'] = self.consignee_name.to_alipay_dict()
            else:
                params['consignee_name'] = self.consignee_name
        if self.consignee_phone:
            if hasattr(self.consignee_phone, 'to_alipay_dict'):
                params['consignee_phone'] = self.consignee_phone.to_alipay_dict()
            else:
                params['consignee_phone'] = self.consignee_phone
        if self.delivery_address:
            if hasattr(self.delivery_address, 'to_alipay_dict'):
                params['delivery_address'] = self.delivery_address.to_alipay_dict()
            else:
                params['delivery_address'] = self.delivery_address
        if self.discount_fee:
            if hasattr(self.discount_fee, 'to_alipay_dict'):
                params['discount_fee'] = self.discount_fee.to_alipay_dict()
            else:
                params['discount_fee'] = self.discount_fee
        if self.logistics_info:
            if hasattr(self.logistics_info, 'to_alipay_dict'):
                params['logistics_info'] = self.logistics_info.to_alipay_dict()
            else:
                params['logistics_info'] = self.logistics_info
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_url:
            if hasattr(self.order_url, 'to_alipay_dict'):
                params['order_url'] = self.order_url.to_alipay_dict()
            else:
                params['order_url'] = self.order_url
        if self.origin_fee:
            if hasattr(self.origin_fee, 'to_alipay_dict'):
                params['origin_fee'] = self.origin_fee.to_alipay_dict()
            else:
                params['origin_fee'] = self.origin_fee
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.pay_fee:
            if hasattr(self.pay_fee, 'to_alipay_dict'):
                params['pay_fee'] = self.pay_fee.to_alipay_dict()
            else:
                params['pay_fee'] = self.pay_fee
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_url:
            if hasattr(self.shop_url, 'to_alipay_dict'):
                params['shop_url'] = self.shop_url.to_alipay_dict()
            else:
                params['shop_url'] = self.shop_url
        if self.unimall_sub_orders:
            if isinstance(self.unimall_sub_orders, list):
                for i in range(0, len(self.unimall_sub_orders)):
                    element = self.unimall_sub_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.unimall_sub_orders[i] = element.to_alipay_dict()
            if hasattr(self.unimall_sub_orders, 'to_alipay_dict'):
                params['unimall_sub_orders'] = self.unimall_sub_orders.to_alipay_dict()
            else:
                params['unimall_sub_orders'] = self.unimall_sub_orders
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderSubmitContent()
        if 'consignee_name' in d:
            o.consignee_name = d['consignee_name']
        if 'consignee_phone' in d:
            o.consignee_phone = d['consignee_phone']
        if 'delivery_address' in d:
            o.delivery_address = d['delivery_address']
        if 'discount_fee' in d:
            o.discount_fee = d['discount_fee']
        if 'logistics_info' in d:
            o.logistics_info = d['logistics_info']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_url' in d:
            o.order_url = d['order_url']
        if 'origin_fee' in d:
            o.origin_fee = d['origin_fee']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'pay_fee' in d:
            o.pay_fee = d['pay_fee']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_url' in d:
            o.shop_url = d['shop_url']
        if 'unimall_sub_orders' in d:
            o.unimall_sub_orders = d['unimall_sub_orders']
        return o


