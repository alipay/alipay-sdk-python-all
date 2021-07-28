#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BakingItemOperationData import BakingItemOperationData


class KoubeiCateringSmartstoreDataSyncModel(object):

    def __init__(self):
        self._baking_item_operation_data = None
        self._browse_dishs = None
        self._browse_time = None
        self._buy_result = None
        self._cabinet_open_time = None
        self._carry_time = None
        self._delivery_end_time = None
        self._delivery_start_time = None
        self._description = None
        self._discount_price = None
        self._item_discount_price = None
        self._item_order_id = None
        self._item_order_name = None
        self._item_price = None
        self._item_quantity = None
        self._order_create_time = None
        self._order_id = None
        self._order_start_time = None
        self._order_type = None
        self._pay_time = None
        self._pay_type = None
        self._people = None
        self._recognize_end_time = None
        self._recognize_start_time = None
        self._recognize_succeed = None
        self._recommend_dishs = None
        self._refund_amount = None
        self._refund_reason = None
        self._refund_time = None
        self._scene = None
        self._shop_id = None
        self._table_number = None
        self._total_price = None
        self._user_id = None

    @property
    def baking_item_operation_data(self):
        return self._baking_item_operation_data

    @baking_item_operation_data.setter
    def baking_item_operation_data(self, value):
        if isinstance(value, BakingItemOperationData):
            self._baking_item_operation_data = value
        else:
            self._baking_item_operation_data = BakingItemOperationData.from_alipay_dict(value)
    @property
    def browse_dishs(self):
        return self._browse_dishs

    @browse_dishs.setter
    def browse_dishs(self, value):
        self._browse_dishs = value
    @property
    def browse_time(self):
        return self._browse_time

    @browse_time.setter
    def browse_time(self, value):
        self._browse_time = value
    @property
    def buy_result(self):
        return self._buy_result

    @buy_result.setter
    def buy_result(self, value):
        self._buy_result = value
    @property
    def cabinet_open_time(self):
        return self._cabinet_open_time

    @cabinet_open_time.setter
    def cabinet_open_time(self, value):
        self._cabinet_open_time = value
    @property
    def carry_time(self):
        return self._carry_time

    @carry_time.setter
    def carry_time(self, value):
        self._carry_time = value
    @property
    def delivery_end_time(self):
        return self._delivery_end_time

    @delivery_end_time.setter
    def delivery_end_time(self, value):
        self._delivery_end_time = value
    @property
    def delivery_start_time(self):
        return self._delivery_start_time

    @delivery_start_time.setter
    def delivery_start_time(self, value):
        self._delivery_start_time = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def discount_price(self):
        return self._discount_price

    @discount_price.setter
    def discount_price(self, value):
        self._discount_price = value
    @property
    def item_discount_price(self):
        return self._item_discount_price

    @item_discount_price.setter
    def item_discount_price(self, value):
        self._item_discount_price = value
    @property
    def item_order_id(self):
        return self._item_order_id

    @item_order_id.setter
    def item_order_id(self, value):
        self._item_order_id = value
    @property
    def item_order_name(self):
        return self._item_order_name

    @item_order_name.setter
    def item_order_name(self, value):
        self._item_order_name = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        self._item_quantity = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_start_time(self):
        return self._order_start_time

    @order_start_time.setter
    def order_start_time(self, value):
        self._order_start_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def people(self):
        return self._people

    @people.setter
    def people(self, value):
        self._people = value
    @property
    def recognize_end_time(self):
        return self._recognize_end_time

    @recognize_end_time.setter
    def recognize_end_time(self, value):
        self._recognize_end_time = value
    @property
    def recognize_start_time(self):
        return self._recognize_start_time

    @recognize_start_time.setter
    def recognize_start_time(self, value):
        self._recognize_start_time = value
    @property
    def recognize_succeed(self):
        return self._recognize_succeed

    @recognize_succeed.setter
    def recognize_succeed(self, value):
        self._recognize_succeed = value
    @property
    def recommend_dishs(self):
        return self._recommend_dishs

    @recommend_dishs.setter
    def recommend_dishs(self, value):
        self._recommend_dishs = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def table_number(self):
        return self._table_number

    @table_number.setter
    def table_number(self, value):
        self._table_number = value
    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.baking_item_operation_data:
            if hasattr(self.baking_item_operation_data, 'to_alipay_dict'):
                params['baking_item_operation_data'] = self.baking_item_operation_data.to_alipay_dict()
            else:
                params['baking_item_operation_data'] = self.baking_item_operation_data
        if self.browse_dishs:
            if hasattr(self.browse_dishs, 'to_alipay_dict'):
                params['browse_dishs'] = self.browse_dishs.to_alipay_dict()
            else:
                params['browse_dishs'] = self.browse_dishs
        if self.browse_time:
            if hasattr(self.browse_time, 'to_alipay_dict'):
                params['browse_time'] = self.browse_time.to_alipay_dict()
            else:
                params['browse_time'] = self.browse_time
        if self.buy_result:
            if hasattr(self.buy_result, 'to_alipay_dict'):
                params['buy_result'] = self.buy_result.to_alipay_dict()
            else:
                params['buy_result'] = self.buy_result
        if self.cabinet_open_time:
            if hasattr(self.cabinet_open_time, 'to_alipay_dict'):
                params['cabinet_open_time'] = self.cabinet_open_time.to_alipay_dict()
            else:
                params['cabinet_open_time'] = self.cabinet_open_time
        if self.carry_time:
            if hasattr(self.carry_time, 'to_alipay_dict'):
                params['carry_time'] = self.carry_time.to_alipay_dict()
            else:
                params['carry_time'] = self.carry_time
        if self.delivery_end_time:
            if hasattr(self.delivery_end_time, 'to_alipay_dict'):
                params['delivery_end_time'] = self.delivery_end_time.to_alipay_dict()
            else:
                params['delivery_end_time'] = self.delivery_end_time
        if self.delivery_start_time:
            if hasattr(self.delivery_start_time, 'to_alipay_dict'):
                params['delivery_start_time'] = self.delivery_start_time.to_alipay_dict()
            else:
                params['delivery_start_time'] = self.delivery_start_time
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.discount_price:
            if hasattr(self.discount_price, 'to_alipay_dict'):
                params['discount_price'] = self.discount_price.to_alipay_dict()
            else:
                params['discount_price'] = self.discount_price
        if self.item_discount_price:
            if hasattr(self.item_discount_price, 'to_alipay_dict'):
                params['item_discount_price'] = self.item_discount_price.to_alipay_dict()
            else:
                params['item_discount_price'] = self.item_discount_price
        if self.item_order_id:
            if hasattr(self.item_order_id, 'to_alipay_dict'):
                params['item_order_id'] = self.item_order_id.to_alipay_dict()
            else:
                params['item_order_id'] = self.item_order_id
        if self.item_order_name:
            if hasattr(self.item_order_name, 'to_alipay_dict'):
                params['item_order_name'] = self.item_order_name.to_alipay_dict()
            else:
                params['item_order_name'] = self.item_order_name
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.item_quantity:
            if hasattr(self.item_quantity, 'to_alipay_dict'):
                params['item_quantity'] = self.item_quantity.to_alipay_dict()
            else:
                params['item_quantity'] = self.item_quantity
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_start_time:
            if hasattr(self.order_start_time, 'to_alipay_dict'):
                params['order_start_time'] = self.order_start_time.to_alipay_dict()
            else:
                params['order_start_time'] = self.order_start_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.people:
            if hasattr(self.people, 'to_alipay_dict'):
                params['people'] = self.people.to_alipay_dict()
            else:
                params['people'] = self.people
        if self.recognize_end_time:
            if hasattr(self.recognize_end_time, 'to_alipay_dict'):
                params['recognize_end_time'] = self.recognize_end_time.to_alipay_dict()
            else:
                params['recognize_end_time'] = self.recognize_end_time
        if self.recognize_start_time:
            if hasattr(self.recognize_start_time, 'to_alipay_dict'):
                params['recognize_start_time'] = self.recognize_start_time.to_alipay_dict()
            else:
                params['recognize_start_time'] = self.recognize_start_time
        if self.recognize_succeed:
            if hasattr(self.recognize_succeed, 'to_alipay_dict'):
                params['recognize_succeed'] = self.recognize_succeed.to_alipay_dict()
            else:
                params['recognize_succeed'] = self.recognize_succeed
        if self.recommend_dishs:
            if hasattr(self.recommend_dishs, 'to_alipay_dict'):
                params['recommend_dishs'] = self.recommend_dishs.to_alipay_dict()
            else:
                params['recommend_dishs'] = self.recommend_dishs
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.table_number:
            if hasattr(self.table_number, 'to_alipay_dict'):
                params['table_number'] = self.table_number.to_alipay_dict()
            else:
                params['table_number'] = self.table_number
        if self.total_price:
            if hasattr(self.total_price, 'to_alipay_dict'):
                params['total_price'] = self.total_price.to_alipay_dict()
            else:
                params['total_price'] = self.total_price
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
        o = KoubeiCateringSmartstoreDataSyncModel()
        if 'baking_item_operation_data' in d:
            o.baking_item_operation_data = d['baking_item_operation_data']
        if 'browse_dishs' in d:
            o.browse_dishs = d['browse_dishs']
        if 'browse_time' in d:
            o.browse_time = d['browse_time']
        if 'buy_result' in d:
            o.buy_result = d['buy_result']
        if 'cabinet_open_time' in d:
            o.cabinet_open_time = d['cabinet_open_time']
        if 'carry_time' in d:
            o.carry_time = d['carry_time']
        if 'delivery_end_time' in d:
            o.delivery_end_time = d['delivery_end_time']
        if 'delivery_start_time' in d:
            o.delivery_start_time = d['delivery_start_time']
        if 'description' in d:
            o.description = d['description']
        if 'discount_price' in d:
            o.discount_price = d['discount_price']
        if 'item_discount_price' in d:
            o.item_discount_price = d['item_discount_price']
        if 'item_order_id' in d:
            o.item_order_id = d['item_order_id']
        if 'item_order_name' in d:
            o.item_order_name = d['item_order_name']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'item_quantity' in d:
            o.item_quantity = d['item_quantity']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_start_time' in d:
            o.order_start_time = d['order_start_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'people' in d:
            o.people = d['people']
        if 'recognize_end_time' in d:
            o.recognize_end_time = d['recognize_end_time']
        if 'recognize_start_time' in d:
            o.recognize_start_time = d['recognize_start_time']
        if 'recognize_succeed' in d:
            o.recognize_succeed = d['recognize_succeed']
        if 'recommend_dishs' in d:
            o.recommend_dishs = d['recommend_dishs']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'scene' in d:
            o.scene = d['scene']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'table_number' in d:
            o.table_number = d['table_number']
        if 'total_price' in d:
            o.total_price = d['total_price']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


