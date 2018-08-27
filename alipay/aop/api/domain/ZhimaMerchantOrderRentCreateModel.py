#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantOrderRentCreateModel(object):

    def __init__(self):
        self._address = None
        self._borrow_cycle = None
        self._borrow_cycle_unit = None
        self._borrow_shop_name = None
        self._borrow_time = None
        self._cert_no = None
        self._credit_biz = None
        self._deposit_amount = None
        self._deposit_state = None
        self._expiry_time = None
        self._extend_info = None
        self._goods_name = None
        self._invoke_return_url = None
        self._invoke_state = None
        self._invoke_type = None
        self._mobile_no = None
        self._name = None
        self._notify_url = None
        self._out_order_no = None
        self._product_code = None
        self._rent_amount = None
        self._rent_info = None
        self._rent_settle_type = None
        self._rent_unit = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def borrow_cycle(self):
        return self._borrow_cycle

    @borrow_cycle.setter
    def borrow_cycle(self, value):
        self._borrow_cycle = value
    @property
    def borrow_cycle_unit(self):
        return self._borrow_cycle_unit

    @borrow_cycle_unit.setter
    def borrow_cycle_unit(self, value):
        self._borrow_cycle_unit = value
    @property
    def borrow_shop_name(self):
        return self._borrow_shop_name

    @borrow_shop_name.setter
    def borrow_shop_name(self, value):
        self._borrow_shop_name = value
    @property
    def borrow_time(self):
        return self._borrow_time

    @borrow_time.setter
    def borrow_time(self, value):
        self._borrow_time = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def credit_biz(self):
        return self._credit_biz

    @credit_biz.setter
    def credit_biz(self, value):
        self._credit_biz = value
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def deposit_state(self):
        return self._deposit_state

    @deposit_state.setter
    def deposit_state(self, value):
        self._deposit_state = value
    @property
    def expiry_time(self):
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self._expiry_time = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def invoke_return_url(self):
        return self._invoke_return_url

    @invoke_return_url.setter
    def invoke_return_url(self, value):
        self._invoke_return_url = value
    @property
    def invoke_state(self):
        return self._invoke_state

    @invoke_state.setter
    def invoke_state(self, value):
        self._invoke_state = value
    @property
    def invoke_type(self):
        return self._invoke_type

    @invoke_type.setter
    def invoke_type(self, value):
        self._invoke_type = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def rent_amount(self):
        return self._rent_amount

    @rent_amount.setter
    def rent_amount(self, value):
        self._rent_amount = value
    @property
    def rent_info(self):
        return self._rent_info

    @rent_info.setter
    def rent_info(self, value):
        self._rent_info = value
    @property
    def rent_settle_type(self):
        return self._rent_settle_type

    @rent_settle_type.setter
    def rent_settle_type(self, value):
        self._rent_settle_type = value
    @property
    def rent_unit(self):
        return self._rent_unit

    @rent_unit.setter
    def rent_unit(self, value):
        self._rent_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.borrow_cycle:
            if hasattr(self.borrow_cycle, 'to_alipay_dict'):
                params['borrow_cycle'] = self.borrow_cycle.to_alipay_dict()
            else:
                params['borrow_cycle'] = self.borrow_cycle
        if self.borrow_cycle_unit:
            if hasattr(self.borrow_cycle_unit, 'to_alipay_dict'):
                params['borrow_cycle_unit'] = self.borrow_cycle_unit.to_alipay_dict()
            else:
                params['borrow_cycle_unit'] = self.borrow_cycle_unit
        if self.borrow_shop_name:
            if hasattr(self.borrow_shop_name, 'to_alipay_dict'):
                params['borrow_shop_name'] = self.borrow_shop_name.to_alipay_dict()
            else:
                params['borrow_shop_name'] = self.borrow_shop_name
        if self.borrow_time:
            if hasattr(self.borrow_time, 'to_alipay_dict'):
                params['borrow_time'] = self.borrow_time.to_alipay_dict()
            else:
                params['borrow_time'] = self.borrow_time
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.credit_biz:
            if hasattr(self.credit_biz, 'to_alipay_dict'):
                params['credit_biz'] = self.credit_biz.to_alipay_dict()
            else:
                params['credit_biz'] = self.credit_biz
        if self.deposit_amount:
            if hasattr(self.deposit_amount, 'to_alipay_dict'):
                params['deposit_amount'] = self.deposit_amount.to_alipay_dict()
            else:
                params['deposit_amount'] = self.deposit_amount
        if self.deposit_state:
            if hasattr(self.deposit_state, 'to_alipay_dict'):
                params['deposit_state'] = self.deposit_state.to_alipay_dict()
            else:
                params['deposit_state'] = self.deposit_state
        if self.expiry_time:
            if hasattr(self.expiry_time, 'to_alipay_dict'):
                params['expiry_time'] = self.expiry_time.to_alipay_dict()
            else:
                params['expiry_time'] = self.expiry_time
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.invoke_return_url:
            if hasattr(self.invoke_return_url, 'to_alipay_dict'):
                params['invoke_return_url'] = self.invoke_return_url.to_alipay_dict()
            else:
                params['invoke_return_url'] = self.invoke_return_url
        if self.invoke_state:
            if hasattr(self.invoke_state, 'to_alipay_dict'):
                params['invoke_state'] = self.invoke_state.to_alipay_dict()
            else:
                params['invoke_state'] = self.invoke_state
        if self.invoke_type:
            if hasattr(self.invoke_type, 'to_alipay_dict'):
                params['invoke_type'] = self.invoke_type.to_alipay_dict()
            else:
                params['invoke_type'] = self.invoke_type
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.notify_url:
            if hasattr(self.notify_url, 'to_alipay_dict'):
                params['notify_url'] = self.notify_url.to_alipay_dict()
            else:
                params['notify_url'] = self.notify_url
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.rent_amount:
            if hasattr(self.rent_amount, 'to_alipay_dict'):
                params['rent_amount'] = self.rent_amount.to_alipay_dict()
            else:
                params['rent_amount'] = self.rent_amount
        if self.rent_info:
            if hasattr(self.rent_info, 'to_alipay_dict'):
                params['rent_info'] = self.rent_info.to_alipay_dict()
            else:
                params['rent_info'] = self.rent_info
        if self.rent_settle_type:
            if hasattr(self.rent_settle_type, 'to_alipay_dict'):
                params['rent_settle_type'] = self.rent_settle_type.to_alipay_dict()
            else:
                params['rent_settle_type'] = self.rent_settle_type
        if self.rent_unit:
            if hasattr(self.rent_unit, 'to_alipay_dict'):
                params['rent_unit'] = self.rent_unit.to_alipay_dict()
            else:
                params['rent_unit'] = self.rent_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantOrderRentCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'borrow_cycle' in d:
            o.borrow_cycle = d['borrow_cycle']
        if 'borrow_cycle_unit' in d:
            o.borrow_cycle_unit = d['borrow_cycle_unit']
        if 'borrow_shop_name' in d:
            o.borrow_shop_name = d['borrow_shop_name']
        if 'borrow_time' in d:
            o.borrow_time = d['borrow_time']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'credit_biz' in d:
            o.credit_biz = d['credit_biz']
        if 'deposit_amount' in d:
            o.deposit_amount = d['deposit_amount']
        if 'deposit_state' in d:
            o.deposit_state = d['deposit_state']
        if 'expiry_time' in d:
            o.expiry_time = d['expiry_time']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'invoke_return_url' in d:
            o.invoke_return_url = d['invoke_return_url']
        if 'invoke_state' in d:
            o.invoke_state = d['invoke_state']
        if 'invoke_type' in d:
            o.invoke_type = d['invoke_type']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'name' in d:
            o.name = d['name']
        if 'notify_url' in d:
            o.notify_url = d['notify_url']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'rent_amount' in d:
            o.rent_amount = d['rent_amount']
        if 'rent_info' in d:
            o.rent_info = d['rent_info']
        if 'rent_settle_type' in d:
            o.rent_settle_type = d['rent_settle_type']
        if 'rent_unit' in d:
            o.rent_unit = d['rent_unit']
        return o


