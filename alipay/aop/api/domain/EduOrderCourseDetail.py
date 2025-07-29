#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduOrderCourseDetail(object):

    def __init__(self):
        self._course_end_date = None
        self._course_id = None
        self._course_start_date = None
        self._deduction_amount = None
        self._deduction_amount_type = None
        self._detail_id = None
        self._discount = None
        self._gift_quantity = None
        self._gift_quantity_unit = None
        self._goods_id = None
        self._goods_name = None
        self._ori_order_id = None
        self._original_price = None
        self._original_price_after_discount = None
        self._payment_type = None
        self._purchase_item_type = None
        self._quantity = None
        self._quantity_unit = None
        self._spec_current_price = None
        self._spec_id = None
        self._spec_name = None
        self._suite_commodity_id = None
        self._suite_commodity_name = None
        self._unpaid_amount = None

    @property
    def course_end_date(self):
        return self._course_end_date

    @course_end_date.setter
    def course_end_date(self, value):
        self._course_end_date = value
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_start_date(self):
        return self._course_start_date

    @course_start_date.setter
    def course_start_date(self, value):
        self._course_start_date = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def deduction_amount_type(self):
        return self._deduction_amount_type

    @deduction_amount_type.setter
    def deduction_amount_type(self, value):
        self._deduction_amount_type = value
    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def gift_quantity(self):
        return self._gift_quantity

    @gift_quantity.setter
    def gift_quantity(self, value):
        self._gift_quantity = value
    @property
    def gift_quantity_unit(self):
        return self._gift_quantity_unit

    @gift_quantity_unit.setter
    def gift_quantity_unit(self, value):
        self._gift_quantity_unit = value
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
    def ori_order_id(self):
        return self._ori_order_id

    @ori_order_id.setter
    def ori_order_id(self, value):
        self._ori_order_id = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def original_price_after_discount(self):
        return self._original_price_after_discount

    @original_price_after_discount.setter
    def original_price_after_discount(self, value):
        self._original_price_after_discount = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def purchase_item_type(self):
        return self._purchase_item_type

    @purchase_item_type.setter
    def purchase_item_type(self, value):
        self._purchase_item_type = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def quantity_unit(self):
        return self._quantity_unit

    @quantity_unit.setter
    def quantity_unit(self, value):
        self._quantity_unit = value
    @property
    def spec_current_price(self):
        return self._spec_current_price

    @spec_current_price.setter
    def spec_current_price(self, value):
        self._spec_current_price = value
    @property
    def spec_id(self):
        return self._spec_id

    @spec_id.setter
    def spec_id(self, value):
        self._spec_id = value
    @property
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value
    @property
    def suite_commodity_id(self):
        return self._suite_commodity_id

    @suite_commodity_id.setter
    def suite_commodity_id(self, value):
        self._suite_commodity_id = value
    @property
    def suite_commodity_name(self):
        return self._suite_commodity_name

    @suite_commodity_name.setter
    def suite_commodity_name(self, value):
        self._suite_commodity_name = value
    @property
    def unpaid_amount(self):
        return self._unpaid_amount

    @unpaid_amount.setter
    def unpaid_amount(self, value):
        self._unpaid_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.course_end_date:
            if hasattr(self.course_end_date, 'to_alipay_dict'):
                params['course_end_date'] = self.course_end_date.to_alipay_dict()
            else:
                params['course_end_date'] = self.course_end_date
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.course_start_date:
            if hasattr(self.course_start_date, 'to_alipay_dict'):
                params['course_start_date'] = self.course_start_date.to_alipay_dict()
            else:
                params['course_start_date'] = self.course_start_date
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.deduction_amount_type:
            if hasattr(self.deduction_amount_type, 'to_alipay_dict'):
                params['deduction_amount_type'] = self.deduction_amount_type.to_alipay_dict()
            else:
                params['deduction_amount_type'] = self.deduction_amount_type
        if self.detail_id:
            if hasattr(self.detail_id, 'to_alipay_dict'):
                params['detail_id'] = self.detail_id.to_alipay_dict()
            else:
                params['detail_id'] = self.detail_id
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.gift_quantity:
            if hasattr(self.gift_quantity, 'to_alipay_dict'):
                params['gift_quantity'] = self.gift_quantity.to_alipay_dict()
            else:
                params['gift_quantity'] = self.gift_quantity
        if self.gift_quantity_unit:
            if hasattr(self.gift_quantity_unit, 'to_alipay_dict'):
                params['gift_quantity_unit'] = self.gift_quantity_unit.to_alipay_dict()
            else:
                params['gift_quantity_unit'] = self.gift_quantity_unit
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
        if self.ori_order_id:
            if hasattr(self.ori_order_id, 'to_alipay_dict'):
                params['ori_order_id'] = self.ori_order_id.to_alipay_dict()
            else:
                params['ori_order_id'] = self.ori_order_id
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.original_price_after_discount:
            if hasattr(self.original_price_after_discount, 'to_alipay_dict'):
                params['original_price_after_discount'] = self.original_price_after_discount.to_alipay_dict()
            else:
                params['original_price_after_discount'] = self.original_price_after_discount
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.purchase_item_type:
            if hasattr(self.purchase_item_type, 'to_alipay_dict'):
                params['purchase_item_type'] = self.purchase_item_type.to_alipay_dict()
            else:
                params['purchase_item_type'] = self.purchase_item_type
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.quantity_unit:
            if hasattr(self.quantity_unit, 'to_alipay_dict'):
                params['quantity_unit'] = self.quantity_unit.to_alipay_dict()
            else:
                params['quantity_unit'] = self.quantity_unit
        if self.spec_current_price:
            if hasattr(self.spec_current_price, 'to_alipay_dict'):
                params['spec_current_price'] = self.spec_current_price.to_alipay_dict()
            else:
                params['spec_current_price'] = self.spec_current_price
        if self.spec_id:
            if hasattr(self.spec_id, 'to_alipay_dict'):
                params['spec_id'] = self.spec_id.to_alipay_dict()
            else:
                params['spec_id'] = self.spec_id
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
        if self.suite_commodity_id:
            if hasattr(self.suite_commodity_id, 'to_alipay_dict'):
                params['suite_commodity_id'] = self.suite_commodity_id.to_alipay_dict()
            else:
                params['suite_commodity_id'] = self.suite_commodity_id
        if self.suite_commodity_name:
            if hasattr(self.suite_commodity_name, 'to_alipay_dict'):
                params['suite_commodity_name'] = self.suite_commodity_name.to_alipay_dict()
            else:
                params['suite_commodity_name'] = self.suite_commodity_name
        if self.unpaid_amount:
            if hasattr(self.unpaid_amount, 'to_alipay_dict'):
                params['unpaid_amount'] = self.unpaid_amount.to_alipay_dict()
            else:
                params['unpaid_amount'] = self.unpaid_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduOrderCourseDetail()
        if 'course_end_date' in d:
            o.course_end_date = d['course_end_date']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_start_date' in d:
            o.course_start_date = d['course_start_date']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_amount_type' in d:
            o.deduction_amount_type = d['deduction_amount_type']
        if 'detail_id' in d:
            o.detail_id = d['detail_id']
        if 'discount' in d:
            o.discount = d['discount']
        if 'gift_quantity' in d:
            o.gift_quantity = d['gift_quantity']
        if 'gift_quantity_unit' in d:
            o.gift_quantity_unit = d['gift_quantity_unit']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'ori_order_id' in d:
            o.ori_order_id = d['ori_order_id']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'original_price_after_discount' in d:
            o.original_price_after_discount = d['original_price_after_discount']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'purchase_item_type' in d:
            o.purchase_item_type = d['purchase_item_type']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'quantity_unit' in d:
            o.quantity_unit = d['quantity_unit']
        if 'spec_current_price' in d:
            o.spec_current_price = d['spec_current_price']
        if 'spec_id' in d:
            o.spec_id = d['spec_id']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'suite_commodity_id' in d:
            o.suite_commodity_id = d['suite_commodity_id']
        if 'suite_commodity_name' in d:
            o.suite_commodity_name = d['suite_commodity_name']
        if 'unpaid_amount' in d:
            o.unpaid_amount = d['unpaid_amount']
        return o


