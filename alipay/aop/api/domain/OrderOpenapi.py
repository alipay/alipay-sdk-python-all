#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderOpenapi(object):

    def __init__(self):
        self._item_image = None
        self._item_title = None
        self._open_id = None
        self._order_confirm_delivery_time = None
        self._order_create_time = None
        self._order_detail_url = None
        self._order_no = None
        self._order_pay_amount = None
        self._order_pay_time = None
        self._order_refund_time = None
        self._order_status = None
        self._user_id = None

    @property
    def item_image(self):
        return self._item_image

    @item_image.setter
    def item_image(self, value):
        self._item_image = value
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_confirm_delivery_time(self):
        return self._order_confirm_delivery_time

    @order_confirm_delivery_time.setter
    def order_confirm_delivery_time(self, value):
        self._order_confirm_delivery_time = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_pay_amount(self):
        return self._order_pay_amount

    @order_pay_amount.setter
    def order_pay_amount(self, value):
        self._order_pay_amount = value
    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, value):
        self._order_pay_time = value
    @property
    def order_refund_time(self):
        return self._order_refund_time

    @order_refund_time.setter
    def order_refund_time(self, value):
        self._order_refund_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_image:
            if hasattr(self.item_image, 'to_alipay_dict'):
                params['item_image'] = self.item_image.to_alipay_dict()
            else:
                params['item_image'] = self.item_image
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_confirm_delivery_time:
            if hasattr(self.order_confirm_delivery_time, 'to_alipay_dict'):
                params['order_confirm_delivery_time'] = self.order_confirm_delivery_time.to_alipay_dict()
            else:
                params['order_confirm_delivery_time'] = self.order_confirm_delivery_time
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_pay_amount:
            if hasattr(self.order_pay_amount, 'to_alipay_dict'):
                params['order_pay_amount'] = self.order_pay_amount.to_alipay_dict()
            else:
                params['order_pay_amount'] = self.order_pay_amount
        if self.order_pay_time:
            if hasattr(self.order_pay_time, 'to_alipay_dict'):
                params['order_pay_time'] = self.order_pay_time.to_alipay_dict()
            else:
                params['order_pay_time'] = self.order_pay_time
        if self.order_refund_time:
            if hasattr(self.order_refund_time, 'to_alipay_dict'):
                params['order_refund_time'] = self.order_refund_time.to_alipay_dict()
            else:
                params['order_refund_time'] = self.order_refund_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
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
        o = OrderOpenapi()
        if 'item_image' in d:
            o.item_image = d['item_image']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_confirm_delivery_time' in d:
            o.order_confirm_delivery_time = d['order_confirm_delivery_time']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_pay_amount' in d:
            o.order_pay_amount = d['order_pay_amount']
        if 'order_pay_time' in d:
            o.order_pay_time = d['order_pay_time']
        if 'order_refund_time' in d:
            o.order_refund_time = d['order_refund_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


