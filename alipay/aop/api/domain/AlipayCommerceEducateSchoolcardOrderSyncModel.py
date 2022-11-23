#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsOrder import GoodsOrder


class AlipayCommerceEducateSchoolcardOrderSyncModel(object):

    def __init__(self):
        self._actual_amount = None
        self._applet_app_id = None
        self._card_balance = None
        self._card_no = None
        self._card_type = None
        self._create_time = None
        self._discount_amount = None
        self._goods_orders = None
        self._merchant_name = None
        self._modified_time = None
        self._open_id = None
        self._order_amount = None
        self._order_detail_url = None
        self._order_status = None
        self._out_biz_no = None
        self._pay_address = None
        self._pay_mode = None
        self._rake_back_pid = None
        self._school_id = None
        self._school_pid = None
        self._service_provider_name = None
        self._type = None
        self._user_id = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def applet_app_id(self):
        return self._applet_app_id

    @applet_app_id.setter
    def applet_app_id(self, value):
        self._applet_app_id = value
    @property
    def card_balance(self):
        return self._card_balance

    @card_balance.setter
    def card_balance(self, value):
        self._card_balance = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def goods_orders(self):
        return self._goods_orders

    @goods_orders.setter
    def goods_orders(self, value):
        if isinstance(value, GoodsOrder):
            self._goods_orders = value
        else:
            self._goods_orders = GoodsOrder.from_alipay_dict(value)
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_address(self):
        return self._pay_address

    @pay_address.setter
    def pay_address(self, value):
        self._pay_address = value
    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, value):
        self._pay_mode = value
    @property
    def rake_back_pid(self):
        return self._rake_back_pid

    @rake_back_pid.setter
    def rake_back_pid(self, value):
        self._rake_back_pid = value
    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value
    @property
    def service_provider_name(self):
        return self._service_provider_name

    @service_provider_name.setter
    def service_provider_name(self, value):
        self._service_provider_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.applet_app_id:
            if hasattr(self.applet_app_id, 'to_alipay_dict'):
                params['applet_app_id'] = self.applet_app_id.to_alipay_dict()
            else:
                params['applet_app_id'] = self.applet_app_id
        if self.card_balance:
            if hasattr(self.card_balance, 'to_alipay_dict'):
                params['card_balance'] = self.card_balance.to_alipay_dict()
            else:
                params['card_balance'] = self.card_balance
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.goods_orders:
            if hasattr(self.goods_orders, 'to_alipay_dict'):
                params['goods_orders'] = self.goods_orders.to_alipay_dict()
            else:
                params['goods_orders'] = self.goods_orders
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_address:
            if hasattr(self.pay_address, 'to_alipay_dict'):
                params['pay_address'] = self.pay_address.to_alipay_dict()
            else:
                params['pay_address'] = self.pay_address
        if self.pay_mode:
            if hasattr(self.pay_mode, 'to_alipay_dict'):
                params['pay_mode'] = self.pay_mode.to_alipay_dict()
            else:
                params['pay_mode'] = self.pay_mode
        if self.rake_back_pid:
            if hasattr(self.rake_back_pid, 'to_alipay_dict'):
                params['rake_back_pid'] = self.rake_back_pid.to_alipay_dict()
            else:
                params['rake_back_pid'] = self.rake_back_pid
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        if self.service_provider_name:
            if hasattr(self.service_provider_name, 'to_alipay_dict'):
                params['service_provider_name'] = self.service_provider_name.to_alipay_dict()
            else:
                params['service_provider_name'] = self.service_provider_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayCommerceEducateSchoolcardOrderSyncModel()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'applet_app_id' in d:
            o.applet_app_id = d['applet_app_id']
        if 'card_balance' in d:
            o.card_balance = d['card_balance']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'goods_orders' in d:
            o.goods_orders = d['goods_orders']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_address' in d:
            o.pay_address = d['pay_address']
        if 'pay_mode' in d:
            o.pay_mode = d['pay_mode']
        if 'rake_back_pid' in d:
            o.rake_back_pid = d['rake_back_pid']
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'service_provider_name' in d:
            o.service_provider_name = d['service_provider_name']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


