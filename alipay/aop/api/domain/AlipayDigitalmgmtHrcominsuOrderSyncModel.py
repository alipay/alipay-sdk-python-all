#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderItemDTO import OrderItemDTO


class AlipayDigitalmgmtHrcominsuOrderSyncModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._channel_order_no = None
        self._channel_raw_status = None
        self._channel_status = None
        self._channel_type = None
        self._customer_id = None
        self._detail_url = None
        self._items = None
        self._merchant_name = None
        self._merchant_no = None
        self._mobile = None
        self._open_id = None
        self._order_time = None
        self._pay_amount = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def channel_order_no(self):
        return self._channel_order_no

    @channel_order_no.setter
    def channel_order_no(self, value):
        self._channel_order_no = value
    @property
    def channel_raw_status(self):
        return self._channel_raw_status

    @channel_raw_status.setter
    def channel_raw_status(self, value):
        self._channel_raw_status = value
    @property
    def channel_status(self):
        return self._channel_status

    @channel_status.setter
    def channel_status(self, value):
        self._channel_status = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, OrderItemDTO):
                    self._items.append(i)
                else:
                    self._items.append(OrderItemDTO.from_alipay_dict(i))
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_no(self):
        return self._merchant_no

    @merchant_no.setter
    def merchant_no(self, value):
        self._merchant_no = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.channel_order_no:
            if hasattr(self.channel_order_no, 'to_alipay_dict'):
                params['channel_order_no'] = self.channel_order_no.to_alipay_dict()
            else:
                params['channel_order_no'] = self.channel_order_no
        if self.channel_raw_status:
            if hasattr(self.channel_raw_status, 'to_alipay_dict'):
                params['channel_raw_status'] = self.channel_raw_status.to_alipay_dict()
            else:
                params['channel_raw_status'] = self.channel_raw_status
        if self.channel_status:
            if hasattr(self.channel_status, 'to_alipay_dict'):
                params['channel_status'] = self.channel_status.to_alipay_dict()
            else:
                params['channel_status'] = self.channel_status
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_no:
            if hasattr(self.merchant_no, 'to_alipay_dict'):
                params['merchant_no'] = self.merchant_no.to_alipay_dict()
            else:
                params['merchant_no'] = self.merchant_no
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrcominsuOrderSyncModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'channel_order_no' in d:
            o.channel_order_no = d['channel_order_no']
        if 'channel_raw_status' in d:
            o.channel_raw_status = d['channel_raw_status']
        if 'channel_status' in d:
            o.channel_status = d['channel_status']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'items' in d:
            o.items = d['items']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_no' in d:
            o.merchant_no = d['merchant_no']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        return o


