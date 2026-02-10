#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportMallOrderCreateModel(object):

    def __init__(self):
        self._brand_id = None
        self._brand_name = None
        self._car_series = None
        self._car_series_name = None
        self._create_by = None
        self._create_time = None
        self._discount_price = None
        self._ecology_status = None
        self._first_pay_type = None
        self._goods_id = None
        self._goods_name = None
        self._goods_price = None
        self._goods_supplier = None
        self._goods_type_id = None
        self._goods_type_name = None
        self._iccid = None
        self._item_type = None
        self._order_biz_type = None
        self._order_channel = None
        self._order_invalid_reason = None
        self._order_status = None
        self._parent_order_no = None
        self._pay_time = None
        self._quantity = None
        self._recharge_phone = None
        self._request_id = None
        self._second_pay_type = None
        self._shop_order_no = None
        self._sid = None
        self._spu_id = None
        self._tenant_id = None
        self._third_create_time = None
        self._third_id = None
        self._third_order_status = None
        self._third_payment_time = None
        self._total_amount = None
        self._trade_price = None
        self._update_by = None
        self._update_time = None
        self._user_phone = None
        self._valid_time = None
        self._vin = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def car_series(self):
        return self._car_series

    @car_series.setter
    def car_series(self, value):
        self._car_series = value
    @property
    def car_series_name(self):
        return self._car_series_name

    @car_series_name.setter
    def car_series_name(self, value):
        self._car_series_name = value
    @property
    def create_by(self):
        return self._create_by

    @create_by.setter
    def create_by(self, value):
        self._create_by = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def discount_price(self):
        return self._discount_price

    @discount_price.setter
    def discount_price(self, value):
        self._discount_price = value
    @property
    def ecology_status(self):
        return self._ecology_status

    @ecology_status.setter
    def ecology_status(self, value):
        self._ecology_status = value
    @property
    def first_pay_type(self):
        return self._first_pay_type

    @first_pay_type.setter
    def first_pay_type(self, value):
        self._first_pay_type = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_price(self):
        return self._goods_price

    @goods_price.setter
    def goods_price(self, value):
        self._goods_price = value
    @property
    def goods_supplier(self):
        return self._goods_supplier

    @goods_supplier.setter
    def goods_supplier(self, value):
        self._goods_supplier = value
    @property
    def goods_type_id(self):
        return self._goods_type_id

    @goods_type_id.setter
    def goods_type_id(self, value):
        self._goods_type_id = value
    @property
    def goods_type_name(self):
        return self._goods_type_name

    @goods_type_name.setter
    def goods_type_name(self, value):
        self._goods_type_name = value
    @property
    def iccid(self):
        return self._iccid

    @iccid.setter
    def iccid(self, value):
        self._iccid = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def order_biz_type(self):
        return self._order_biz_type

    @order_biz_type.setter
    def order_biz_type(self, value):
        self._order_biz_type = value
    @property
    def order_channel(self):
        return self._order_channel

    @order_channel.setter
    def order_channel(self, value):
        self._order_channel = value
    @property
    def order_invalid_reason(self):
        return self._order_invalid_reason

    @order_invalid_reason.setter
    def order_invalid_reason(self, value):
        self._order_invalid_reason = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def parent_order_no(self):
        return self._parent_order_no

    @parent_order_no.setter
    def parent_order_no(self, value):
        self._parent_order_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def recharge_phone(self):
        return self._recharge_phone

    @recharge_phone.setter
    def recharge_phone(self, value):
        self._recharge_phone = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def second_pay_type(self):
        return self._second_pay_type

    @second_pay_type.setter
    def second_pay_type(self, value):
        self._second_pay_type = value
    @property
    def shop_order_no(self):
        return self._shop_order_no

    @shop_order_no.setter
    def shop_order_no(self, value):
        self._shop_order_no = value
    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, value):
        self._sid = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def third_create_time(self):
        return self._third_create_time

    @third_create_time.setter
    def third_create_time(self, value):
        self._third_create_time = value
    @property
    def third_id(self):
        return self._third_id

    @third_id.setter
    def third_id(self, value):
        self._third_id = value
    @property
    def third_order_status(self):
        return self._third_order_status

    @third_order_status.setter
    def third_order_status(self, value):
        self._third_order_status = value
    @property
    def third_payment_time(self):
        return self._third_payment_time

    @third_payment_time.setter
    def third_payment_time(self, value):
        self._third_payment_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_price(self):
        return self._trade_price

    @trade_price.setter
    def trade_price(self, value):
        self._trade_price = value
    @property
    def update_by(self):
        return self._update_by

    @update_by.setter
    def update_by(self, value):
        self._update_by = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.car_series:
            if hasattr(self.car_series, 'to_alipay_dict'):
                params['car_series'] = self.car_series.to_alipay_dict()
            else:
                params['car_series'] = self.car_series
        if self.car_series_name:
            if hasattr(self.car_series_name, 'to_alipay_dict'):
                params['car_series_name'] = self.car_series_name.to_alipay_dict()
            else:
                params['car_series_name'] = self.car_series_name
        if self.create_by:
            if hasattr(self.create_by, 'to_alipay_dict'):
                params['create_by'] = self.create_by.to_alipay_dict()
            else:
                params['create_by'] = self.create_by
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.discount_price:
            if hasattr(self.discount_price, 'to_alipay_dict'):
                params['discount_price'] = self.discount_price.to_alipay_dict()
            else:
                params['discount_price'] = self.discount_price
        if self.ecology_status:
            if hasattr(self.ecology_status, 'to_alipay_dict'):
                params['ecology_status'] = self.ecology_status.to_alipay_dict()
            else:
                params['ecology_status'] = self.ecology_status
        if self.first_pay_type:
            if hasattr(self.first_pay_type, 'to_alipay_dict'):
                params['first_pay_type'] = self.first_pay_type.to_alipay_dict()
            else:
                params['first_pay_type'] = self.first_pay_type
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_price:
            if hasattr(self.goods_price, 'to_alipay_dict'):
                params['goods_price'] = self.goods_price.to_alipay_dict()
            else:
                params['goods_price'] = self.goods_price
        if self.goods_supplier:
            if hasattr(self.goods_supplier, 'to_alipay_dict'):
                params['goods_supplier'] = self.goods_supplier.to_alipay_dict()
            else:
                params['goods_supplier'] = self.goods_supplier
        if self.goods_type_id:
            if hasattr(self.goods_type_id, 'to_alipay_dict'):
                params['goods_type_id'] = self.goods_type_id.to_alipay_dict()
            else:
                params['goods_type_id'] = self.goods_type_id
        if self.goods_type_name:
            if hasattr(self.goods_type_name, 'to_alipay_dict'):
                params['goods_type_name'] = self.goods_type_name.to_alipay_dict()
            else:
                params['goods_type_name'] = self.goods_type_name
        if self.iccid:
            if hasattr(self.iccid, 'to_alipay_dict'):
                params['iccid'] = self.iccid.to_alipay_dict()
            else:
                params['iccid'] = self.iccid
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.order_biz_type:
            if hasattr(self.order_biz_type, 'to_alipay_dict'):
                params['order_biz_type'] = self.order_biz_type.to_alipay_dict()
            else:
                params['order_biz_type'] = self.order_biz_type
        if self.order_channel:
            if hasattr(self.order_channel, 'to_alipay_dict'):
                params['order_channel'] = self.order_channel.to_alipay_dict()
            else:
                params['order_channel'] = self.order_channel
        if self.order_invalid_reason:
            if hasattr(self.order_invalid_reason, 'to_alipay_dict'):
                params['order_invalid_reason'] = self.order_invalid_reason.to_alipay_dict()
            else:
                params['order_invalid_reason'] = self.order_invalid_reason
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.parent_order_no:
            if hasattr(self.parent_order_no, 'to_alipay_dict'):
                params['parent_order_no'] = self.parent_order_no.to_alipay_dict()
            else:
                params['parent_order_no'] = self.parent_order_no
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.recharge_phone:
            if hasattr(self.recharge_phone, 'to_alipay_dict'):
                params['recharge_phone'] = self.recharge_phone.to_alipay_dict()
            else:
                params['recharge_phone'] = self.recharge_phone
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.second_pay_type:
            if hasattr(self.second_pay_type, 'to_alipay_dict'):
                params['second_pay_type'] = self.second_pay_type.to_alipay_dict()
            else:
                params['second_pay_type'] = self.second_pay_type
        if self.shop_order_no:
            if hasattr(self.shop_order_no, 'to_alipay_dict'):
                params['shop_order_no'] = self.shop_order_no.to_alipay_dict()
            else:
                params['shop_order_no'] = self.shop_order_no
        if self.sid:
            if hasattr(self.sid, 'to_alipay_dict'):
                params['sid'] = self.sid.to_alipay_dict()
            else:
                params['sid'] = self.sid
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.third_create_time:
            if hasattr(self.third_create_time, 'to_alipay_dict'):
                params['third_create_time'] = self.third_create_time.to_alipay_dict()
            else:
                params['third_create_time'] = self.third_create_time
        if self.third_id:
            if hasattr(self.third_id, 'to_alipay_dict'):
                params['third_id'] = self.third_id.to_alipay_dict()
            else:
                params['third_id'] = self.third_id
        if self.third_order_status:
            if hasattr(self.third_order_status, 'to_alipay_dict'):
                params['third_order_status'] = self.third_order_status.to_alipay_dict()
            else:
                params['third_order_status'] = self.third_order_status
        if self.third_payment_time:
            if hasattr(self.third_payment_time, 'to_alipay_dict'):
                params['third_payment_time'] = self.third_payment_time.to_alipay_dict()
            else:
                params['third_payment_time'] = self.third_payment_time
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_price:
            if hasattr(self.trade_price, 'to_alipay_dict'):
                params['trade_price'] = self.trade_price.to_alipay_dict()
            else:
                params['trade_price'] = self.trade_price
        if self.update_by:
            if hasattr(self.update_by, 'to_alipay_dict'):
                params['update_by'] = self.update_by.to_alipay_dict()
            else:
                params['update_by'] = self.update_by
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        if self.vin:
            if hasattr(self.vin, 'to_alipay_dict'):
                params['vin'] = self.vin.to_alipay_dict()
            else:
                params['vin'] = self.vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportMallOrderCreateModel()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'car_series' in d:
            o.car_series = d['car_series']
        if 'car_series_name' in d:
            o.car_series_name = d['car_series_name']
        if 'create_by' in d:
            o.create_by = d['create_by']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'discount_price' in d:
            o.discount_price = d['discount_price']
        if 'ecology_status' in d:
            o.ecology_status = d['ecology_status']
        if 'first_pay_type' in d:
            o.first_pay_type = d['first_pay_type']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_price' in d:
            o.goods_price = d['goods_price']
        if 'goods_supplier' in d:
            o.goods_supplier = d['goods_supplier']
        if 'goods_type_id' in d:
            o.goods_type_id = d['goods_type_id']
        if 'goods_type_name' in d:
            o.goods_type_name = d['goods_type_name']
        if 'iccid' in d:
            o.iccid = d['iccid']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'order_biz_type' in d:
            o.order_biz_type = d['order_biz_type']
        if 'order_channel' in d:
            o.order_channel = d['order_channel']
        if 'order_invalid_reason' in d:
            o.order_invalid_reason = d['order_invalid_reason']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'parent_order_no' in d:
            o.parent_order_no = d['parent_order_no']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'recharge_phone' in d:
            o.recharge_phone = d['recharge_phone']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'second_pay_type' in d:
            o.second_pay_type = d['second_pay_type']
        if 'shop_order_no' in d:
            o.shop_order_no = d['shop_order_no']
        if 'sid' in d:
            o.sid = d['sid']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'third_create_time' in d:
            o.third_create_time = d['third_create_time']
        if 'third_id' in d:
            o.third_id = d['third_id']
        if 'third_order_status' in d:
            o.third_order_status = d['third_order_status']
        if 'third_payment_time' in d:
            o.third_payment_time = d['third_payment_time']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_price' in d:
            o.trade_price = d['trade_price']
        if 'update_by' in d:
            o.update_by = d['update_by']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        if 'vin' in d:
            o.vin = d['vin']
        return o


