#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemSellOrderResponse(object):

    def __init__(self):
        self._cps_amount = None
        self._create_time = None
        self._item_id = None
        self._item_instance_id = None
        self._item_name = None
        self._item_price = None
        self._item_type = None
        self._merchant_discount_amount = None
        self._merchant_order_no = None
        self._order_id = None
        self._order_scene = None
        self._order_status = None
        self._pay_commission = None
        self._platform_discount_amount = None
        self._pre_receipt_amount = None
        self._pre_user_fund_amount = None
        self._predict_settle_time = None
        self._receipt_amount = None
        self._refund_cps_amount = None
        self._refund_fee = None
        self._refund_pay_commission = None
        self._remark = None
        self._settle_account_no = None
        self._settle_account_type = None
        self._settle_amount = None
        self._settle_time = None
        self._trade_no = None
        self._user_fund_amount = None

    @property
    def cps_amount(self):
        return self._cps_amount

    @cps_amount.setter
    def cps_amount(self, value):
        self._cps_amount = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_instance_id(self):
        return self._item_instance_id

    @item_instance_id.setter
    def item_instance_id(self, value):
        self._item_instance_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def merchant_discount_amount(self):
        return self._merchant_discount_amount

    @merchant_discount_amount.setter
    def merchant_discount_amount(self, value):
        self._merchant_discount_amount = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_scene(self):
        return self._order_scene

    @order_scene.setter
    def order_scene(self, value):
        self._order_scene = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pay_commission(self):
        return self._pay_commission

    @pay_commission.setter
    def pay_commission(self, value):
        self._pay_commission = value
    @property
    def platform_discount_amount(self):
        return self._platform_discount_amount

    @platform_discount_amount.setter
    def platform_discount_amount(self, value):
        self._platform_discount_amount = value
    @property
    def pre_receipt_amount(self):
        return self._pre_receipt_amount

    @pre_receipt_amount.setter
    def pre_receipt_amount(self, value):
        self._pre_receipt_amount = value
    @property
    def pre_user_fund_amount(self):
        return self._pre_user_fund_amount

    @pre_user_fund_amount.setter
    def pre_user_fund_amount(self, value):
        self._pre_user_fund_amount = value
    @property
    def predict_settle_time(self):
        return self._predict_settle_time

    @predict_settle_time.setter
    def predict_settle_time(self, value):
        self._predict_settle_time = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def refund_cps_amount(self):
        return self._refund_cps_amount

    @refund_cps_amount.setter
    def refund_cps_amount(self, value):
        self._refund_cps_amount = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_pay_commission(self):
        return self._refund_pay_commission

    @refund_pay_commission.setter
    def refund_pay_commission(self, value):
        self._refund_pay_commission = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def settle_account_no(self):
        return self._settle_account_no

    @settle_account_no.setter
    def settle_account_no(self, value):
        self._settle_account_no = value
    @property
    def settle_account_type(self):
        return self._settle_account_type

    @settle_account_type.setter
    def settle_account_type(self, value):
        self._settle_account_type = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
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
    def user_fund_amount(self):
        return self._user_fund_amount

    @user_fund_amount.setter
    def user_fund_amount(self, value):
        self._user_fund_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.cps_amount:
            if hasattr(self.cps_amount, 'to_alipay_dict'):
                params['cps_amount'] = self.cps_amount.to_alipay_dict()
            else:
                params['cps_amount'] = self.cps_amount
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_instance_id:
            if hasattr(self.item_instance_id, 'to_alipay_dict'):
                params['item_instance_id'] = self.item_instance_id.to_alipay_dict()
            else:
                params['item_instance_id'] = self.item_instance_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.merchant_discount_amount:
            if hasattr(self.merchant_discount_amount, 'to_alipay_dict'):
                params['merchant_discount_amount'] = self.merchant_discount_amount.to_alipay_dict()
            else:
                params['merchant_discount_amount'] = self.merchant_discount_amount
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_scene:
            if hasattr(self.order_scene, 'to_alipay_dict'):
                params['order_scene'] = self.order_scene.to_alipay_dict()
            else:
                params['order_scene'] = self.order_scene
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pay_commission:
            if hasattr(self.pay_commission, 'to_alipay_dict'):
                params['pay_commission'] = self.pay_commission.to_alipay_dict()
            else:
                params['pay_commission'] = self.pay_commission
        if self.platform_discount_amount:
            if hasattr(self.platform_discount_amount, 'to_alipay_dict'):
                params['platform_discount_amount'] = self.platform_discount_amount.to_alipay_dict()
            else:
                params['platform_discount_amount'] = self.platform_discount_amount
        if self.pre_receipt_amount:
            if hasattr(self.pre_receipt_amount, 'to_alipay_dict'):
                params['pre_receipt_amount'] = self.pre_receipt_amount.to_alipay_dict()
            else:
                params['pre_receipt_amount'] = self.pre_receipt_amount
        if self.pre_user_fund_amount:
            if hasattr(self.pre_user_fund_amount, 'to_alipay_dict'):
                params['pre_user_fund_amount'] = self.pre_user_fund_amount.to_alipay_dict()
            else:
                params['pre_user_fund_amount'] = self.pre_user_fund_amount
        if self.predict_settle_time:
            if hasattr(self.predict_settle_time, 'to_alipay_dict'):
                params['predict_settle_time'] = self.predict_settle_time.to_alipay_dict()
            else:
                params['predict_settle_time'] = self.predict_settle_time
        if self.receipt_amount:
            if hasattr(self.receipt_amount, 'to_alipay_dict'):
                params['receipt_amount'] = self.receipt_amount.to_alipay_dict()
            else:
                params['receipt_amount'] = self.receipt_amount
        if self.refund_cps_amount:
            if hasattr(self.refund_cps_amount, 'to_alipay_dict'):
                params['refund_cps_amount'] = self.refund_cps_amount.to_alipay_dict()
            else:
                params['refund_cps_amount'] = self.refund_cps_amount
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        if self.refund_pay_commission:
            if hasattr(self.refund_pay_commission, 'to_alipay_dict'):
                params['refund_pay_commission'] = self.refund_pay_commission.to_alipay_dict()
            else:
                params['refund_pay_commission'] = self.refund_pay_commission
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.settle_account_no:
            if hasattr(self.settle_account_no, 'to_alipay_dict'):
                params['settle_account_no'] = self.settle_account_no.to_alipay_dict()
            else:
                params['settle_account_no'] = self.settle_account_no
        if self.settle_account_type:
            if hasattr(self.settle_account_type, 'to_alipay_dict'):
                params['settle_account_type'] = self.settle_account_type.to_alipay_dict()
            else:
                params['settle_account_type'] = self.settle_account_type
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
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
        if self.user_fund_amount:
            if hasattr(self.user_fund_amount, 'to_alipay_dict'):
                params['user_fund_amount'] = self.user_fund_amount.to_alipay_dict()
            else:
                params['user_fund_amount'] = self.user_fund_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemSellOrderResponse()
        if 'cps_amount' in d:
            o.cps_amount = d['cps_amount']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_instance_id' in d:
            o.item_instance_id = d['item_instance_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'merchant_discount_amount' in d:
            o.merchant_discount_amount = d['merchant_discount_amount']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_scene' in d:
            o.order_scene = d['order_scene']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pay_commission' in d:
            o.pay_commission = d['pay_commission']
        if 'platform_discount_amount' in d:
            o.platform_discount_amount = d['platform_discount_amount']
        if 'pre_receipt_amount' in d:
            o.pre_receipt_amount = d['pre_receipt_amount']
        if 'pre_user_fund_amount' in d:
            o.pre_user_fund_amount = d['pre_user_fund_amount']
        if 'predict_settle_time' in d:
            o.predict_settle_time = d['predict_settle_time']
        if 'receipt_amount' in d:
            o.receipt_amount = d['receipt_amount']
        if 'refund_cps_amount' in d:
            o.refund_cps_amount = d['refund_cps_amount']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'refund_pay_commission' in d:
            o.refund_pay_commission = d['refund_pay_commission']
        if 'remark' in d:
            o.remark = d['remark']
        if 'settle_account_no' in d:
            o.settle_account_no = d['settle_account_no']
        if 'settle_account_type' in d:
            o.settle_account_type = d['settle_account_type']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_fund_amount' in d:
            o.user_fund_amount = d['user_fund_amount']
        return o


