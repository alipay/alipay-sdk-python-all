#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SelfItemOrderBillDetailResponse(object):

    def __init__(self):
        self._certificate_id = None
        self._certificate_price = None
        self._certificate_status = None
        self._fee_category = None
        self._item_type = None
        self._merchant_verification_no = None
        self._mini_app_id = None
        self._order_scene = None
        self._pay_discounted_price = None
        self._platform_service = None
        self._platform_service_refund = None
        self._predict_settle_time = None
        self._real_receipt_amount = None
        self._refund_fee = None
        self._self_shop_name = None
        self._serial_no = None
        self._settle_amount = None
        self._settle_status = None
        self._settle_time = None
        self._trade_no = None
        self._verification_shop_id = None
        self._verification_shop_name = None
        self._verification_time = None
        self._verification_trade_no = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_price(self):
        return self._certificate_price

    @certificate_price.setter
    def certificate_price(self, value):
        self._certificate_price = value
    @property
    def certificate_status(self):
        return self._certificate_status

    @certificate_status.setter
    def certificate_status(self, value):
        self._certificate_status = value
    @property
    def fee_category(self):
        return self._fee_category

    @fee_category.setter
    def fee_category(self, value):
        self._fee_category = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def merchant_verification_no(self):
        return self._merchant_verification_no

    @merchant_verification_no.setter
    def merchant_verification_no(self, value):
        self._merchant_verification_no = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def order_scene(self):
        return self._order_scene

    @order_scene.setter
    def order_scene(self, value):
        self._order_scene = value
    @property
    def pay_discounted_price(self):
        return self._pay_discounted_price

    @pay_discounted_price.setter
    def pay_discounted_price(self, value):
        self._pay_discounted_price = value
    @property
    def platform_service(self):
        return self._platform_service

    @platform_service.setter
    def platform_service(self, value):
        self._platform_service = value
    @property
    def platform_service_refund(self):
        return self._platform_service_refund

    @platform_service_refund.setter
    def platform_service_refund(self, value):
        self._platform_service_refund = value
    @property
    def predict_settle_time(self):
        return self._predict_settle_time

    @predict_settle_time.setter
    def predict_settle_time(self, value):
        self._predict_settle_time = value
    @property
    def real_receipt_amount(self):
        return self._real_receipt_amount

    @real_receipt_amount.setter
    def real_receipt_amount(self, value):
        self._real_receipt_amount = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def self_shop_name(self):
        return self._self_shop_name

    @self_shop_name.setter
    def self_shop_name(self, value):
        self._self_shop_name = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def settle_time(self):
        return self._settle_time

    @settle_time.setter
    def settle_time(self, value):
        self._settle_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def verification_shop_id(self):
        return self._verification_shop_id

    @verification_shop_id.setter
    def verification_shop_id(self, value):
        self._verification_shop_id = value
    @property
    def verification_shop_name(self):
        return self._verification_shop_name

    @verification_shop_name.setter
    def verification_shop_name(self, value):
        self._verification_shop_name = value
    @property
    def verification_time(self):
        return self._verification_time

    @verification_time.setter
    def verification_time(self, value):
        self._verification_time = value
    @property
    def verification_trade_no(self):
        return self._verification_trade_no

    @verification_trade_no.setter
    def verification_trade_no(self, value):
        self._verification_trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_price:
            if hasattr(self.certificate_price, 'to_alipay_dict'):
                params['certificate_price'] = self.certificate_price.to_alipay_dict()
            else:
                params['certificate_price'] = self.certificate_price
        if self.certificate_status:
            if hasattr(self.certificate_status, 'to_alipay_dict'):
                params['certificate_status'] = self.certificate_status.to_alipay_dict()
            else:
                params['certificate_status'] = self.certificate_status
        if self.fee_category:
            if hasattr(self.fee_category, 'to_alipay_dict'):
                params['fee_category'] = self.fee_category.to_alipay_dict()
            else:
                params['fee_category'] = self.fee_category
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.merchant_verification_no:
            if hasattr(self.merchant_verification_no, 'to_alipay_dict'):
                params['merchant_verification_no'] = self.merchant_verification_no.to_alipay_dict()
            else:
                params['merchant_verification_no'] = self.merchant_verification_no
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.order_scene:
            if hasattr(self.order_scene, 'to_alipay_dict'):
                params['order_scene'] = self.order_scene.to_alipay_dict()
            else:
                params['order_scene'] = self.order_scene
        if self.pay_discounted_price:
            if hasattr(self.pay_discounted_price, 'to_alipay_dict'):
                params['pay_discounted_price'] = self.pay_discounted_price.to_alipay_dict()
            else:
                params['pay_discounted_price'] = self.pay_discounted_price
        if self.platform_service:
            if hasattr(self.platform_service, 'to_alipay_dict'):
                params['platform_service'] = self.platform_service.to_alipay_dict()
            else:
                params['platform_service'] = self.platform_service
        if self.platform_service_refund:
            if hasattr(self.platform_service_refund, 'to_alipay_dict'):
                params['platform_service_refund'] = self.platform_service_refund.to_alipay_dict()
            else:
                params['platform_service_refund'] = self.platform_service_refund
        if self.predict_settle_time:
            if hasattr(self.predict_settle_time, 'to_alipay_dict'):
                params['predict_settle_time'] = self.predict_settle_time.to_alipay_dict()
            else:
                params['predict_settle_time'] = self.predict_settle_time
        if self.real_receipt_amount:
            if hasattr(self.real_receipt_amount, 'to_alipay_dict'):
                params['real_receipt_amount'] = self.real_receipt_amount.to_alipay_dict()
            else:
                params['real_receipt_amount'] = self.real_receipt_amount
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        if self.self_shop_name:
            if hasattr(self.self_shop_name, 'to_alipay_dict'):
                params['self_shop_name'] = self.self_shop_name.to_alipay_dict()
            else:
                params['self_shop_name'] = self.self_shop_name
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.settle_time:
            if hasattr(self.settle_time, 'to_alipay_dict'):
                params['settle_time'] = self.settle_time.to_alipay_dict()
            else:
                params['settle_time'] = self.settle_time
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.verification_shop_id:
            if hasattr(self.verification_shop_id, 'to_alipay_dict'):
                params['verification_shop_id'] = self.verification_shop_id.to_alipay_dict()
            else:
                params['verification_shop_id'] = self.verification_shop_id
        if self.verification_shop_name:
            if hasattr(self.verification_shop_name, 'to_alipay_dict'):
                params['verification_shop_name'] = self.verification_shop_name.to_alipay_dict()
            else:
                params['verification_shop_name'] = self.verification_shop_name
        if self.verification_time:
            if hasattr(self.verification_time, 'to_alipay_dict'):
                params['verification_time'] = self.verification_time.to_alipay_dict()
            else:
                params['verification_time'] = self.verification_time
        if self.verification_trade_no:
            if hasattr(self.verification_trade_no, 'to_alipay_dict'):
                params['verification_trade_no'] = self.verification_trade_no.to_alipay_dict()
            else:
                params['verification_trade_no'] = self.verification_trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SelfItemOrderBillDetailResponse()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_price' in d:
            o.certificate_price = d['certificate_price']
        if 'certificate_status' in d:
            o.certificate_status = d['certificate_status']
        if 'fee_category' in d:
            o.fee_category = d['fee_category']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'merchant_verification_no' in d:
            o.merchant_verification_no = d['merchant_verification_no']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'order_scene' in d:
            o.order_scene = d['order_scene']
        if 'pay_discounted_price' in d:
            o.pay_discounted_price = d['pay_discounted_price']
        if 'platform_service' in d:
            o.platform_service = d['platform_service']
        if 'platform_service_refund' in d:
            o.platform_service_refund = d['platform_service_refund']
        if 'predict_settle_time' in d:
            o.predict_settle_time = d['predict_settle_time']
        if 'real_receipt_amount' in d:
            o.real_receipt_amount = d['real_receipt_amount']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'self_shop_name' in d:
            o.self_shop_name = d['self_shop_name']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'verification_shop_id' in d:
            o.verification_shop_id = d['verification_shop_id']
        if 'verification_shop_name' in d:
            o.verification_shop_name = d['verification_shop_name']
        if 'verification_time' in d:
            o.verification_time = d['verification_time']
        if 'verification_trade_no' in d:
            o.verification_trade_no = d['verification_trade_no']
        return o


