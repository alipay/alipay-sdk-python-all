#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderBusinessInfo import OrderBusinessInfo


class AlipayOfflineProviderGroupmealOrderSyncModel(object):

    def __init__(self):
        self._account_id = None
        self._amount = None
        self._device_sn = None
        self._discount_amount = None
        self._enterprise_id = None
        self._good_name = None
        self._isv_pid = None
        self._merchant_order_link_page = None
        self._merchant_order_status = None
        self._merchant_pid = None
        self._merchant_recharge_link_page = None
        self._open_id = None
        self._order_business_info = None
        self._order_create_time = None
        self._order_modified_time = None
        self._order_pay_time = None
        self._org_id = None
        self._out_biz_no = None
        self._pay_amount = None
        self._payment_type = None
        self._payment_voucher = None
        self._tiny_app_id = None
        self._trade_no = None
        self._user_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def good_name(self):
        return self._good_name

    @good_name.setter
    def good_name(self, value):
        self._good_name = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def merchant_order_link_page(self):
        return self._merchant_order_link_page

    @merchant_order_link_page.setter
    def merchant_order_link_page(self, value):
        self._merchant_order_link_page = value
    @property
    def merchant_order_status(self):
        return self._merchant_order_status

    @merchant_order_status.setter
    def merchant_order_status(self, value):
        self._merchant_order_status = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def merchant_recharge_link_page(self):
        return self._merchant_recharge_link_page

    @merchant_recharge_link_page.setter
    def merchant_recharge_link_page(self, value):
        self._merchant_recharge_link_page = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_business_info(self):
        return self._order_business_info

    @order_business_info.setter
    def order_business_info(self, value):
        if isinstance(value, OrderBusinessInfo):
            self._order_business_info = value
        else:
            self._order_business_info = OrderBusinessInfo.from_alipay_dict(value)
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_modified_time(self):
        return self._order_modified_time

    @order_modified_time.setter
    def order_modified_time(self, value):
        self._order_modified_time = value
    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, value):
        self._order_pay_time = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def payment_voucher(self):
        return self._payment_voucher

    @payment_voucher.setter
    def payment_voucher(self, value):
        self._payment_voucher = value
    @property
    def tiny_app_id(self):
        return self._tiny_app_id

    @tiny_app_id.setter
    def tiny_app_id(self, value):
        self._tiny_app_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.good_name:
            if hasattr(self.good_name, 'to_alipay_dict'):
                params['good_name'] = self.good_name.to_alipay_dict()
            else:
                params['good_name'] = self.good_name
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.merchant_order_link_page:
            if hasattr(self.merchant_order_link_page, 'to_alipay_dict'):
                params['merchant_order_link_page'] = self.merchant_order_link_page.to_alipay_dict()
            else:
                params['merchant_order_link_page'] = self.merchant_order_link_page
        if self.merchant_order_status:
            if hasattr(self.merchant_order_status, 'to_alipay_dict'):
                params['merchant_order_status'] = self.merchant_order_status.to_alipay_dict()
            else:
                params['merchant_order_status'] = self.merchant_order_status
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.merchant_recharge_link_page:
            if hasattr(self.merchant_recharge_link_page, 'to_alipay_dict'):
                params['merchant_recharge_link_page'] = self.merchant_recharge_link_page.to_alipay_dict()
            else:
                params['merchant_recharge_link_page'] = self.merchant_recharge_link_page
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_business_info:
            if hasattr(self.order_business_info, 'to_alipay_dict'):
                params['order_business_info'] = self.order_business_info.to_alipay_dict()
            else:
                params['order_business_info'] = self.order_business_info
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_modified_time:
            if hasattr(self.order_modified_time, 'to_alipay_dict'):
                params['order_modified_time'] = self.order_modified_time.to_alipay_dict()
            else:
                params['order_modified_time'] = self.order_modified_time
        if self.order_pay_time:
            if hasattr(self.order_pay_time, 'to_alipay_dict'):
                params['order_pay_time'] = self.order_pay_time.to_alipay_dict()
            else:
                params['order_pay_time'] = self.order_pay_time
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.payment_voucher:
            if hasattr(self.payment_voucher, 'to_alipay_dict'):
                params['payment_voucher'] = self.payment_voucher.to_alipay_dict()
            else:
                params['payment_voucher'] = self.payment_voucher
        if self.tiny_app_id:
            if hasattr(self.tiny_app_id, 'to_alipay_dict'):
                params['tiny_app_id'] = self.tiny_app_id.to_alipay_dict()
            else:
                params['tiny_app_id'] = self.tiny_app_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AlipayOfflineProviderGroupmealOrderSyncModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'good_name' in d:
            o.good_name = d['good_name']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'merchant_order_link_page' in d:
            o.merchant_order_link_page = d['merchant_order_link_page']
        if 'merchant_order_status' in d:
            o.merchant_order_status = d['merchant_order_status']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'merchant_recharge_link_page' in d:
            o.merchant_recharge_link_page = d['merchant_recharge_link_page']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_business_info' in d:
            o.order_business_info = d['order_business_info']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_modified_time' in d:
            o.order_modified_time = d['order_modified_time']
        if 'order_pay_time' in d:
            o.order_pay_time = d['order_pay_time']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'payment_voucher' in d:
            o.payment_voucher = d['payment_voucher']
        if 'tiny_app_id' in d:
            o.tiny_app_id = d['tiny_app_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


