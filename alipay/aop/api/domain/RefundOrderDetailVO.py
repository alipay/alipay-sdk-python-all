#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundItemVO import RefundItemVO
from alipay.aop.api.domain.MedicareVO import MedicareVO


class RefundOrderDetailVO(object):

    def __init__(self):
        self._amount = None
        self._amount_item = None
        self._amount_user = None
        self._apply_time = None
        self._confirm_time = None
        self._delivery_discount_fee = None
        self._delivery_fee = None
        self._delivery_price = None
        self._distance_markup_price = None
        self._images = None
        self._items = None
        self._medicare = None
        self._mi_amount = None
        self._operator_role = None
        self._order_no = None
        self._packing_fee = None
        self._reason = None
        self._reason_code = None
        self._refund_msg = None
        self._refund_order_no = None
        self._refund_status = None
        self._refund_type = None
        self._refuse_reason = None
        self._refuse_reason_code = None
        self._success_time = None
        self._time_markup_price = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def amount_item(self):
        return self._amount_item

    @amount_item.setter
    def amount_item(self, value):
        self._amount_item = value
    @property
    def amount_user(self):
        return self._amount_user

    @amount_user.setter
    def amount_user(self, value):
        self._amount_user = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def confirm_time(self):
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, value):
        self._confirm_time = value
    @property
    def delivery_discount_fee(self):
        return self._delivery_discount_fee

    @delivery_discount_fee.setter
    def delivery_discount_fee(self, value):
        self._delivery_discount_fee = value
    @property
    def delivery_fee(self):
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value):
        self._delivery_fee = value
    @property
    def delivery_price(self):
        return self._delivery_price

    @delivery_price.setter
    def delivery_price(self, value):
        self._delivery_price = value
    @property
    def distance_markup_price(self):
        return self._distance_markup_price

    @distance_markup_price.setter
    def distance_markup_price(self, value):
        self._distance_markup_price = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, RefundItemVO):
                    self._items.append(i)
                else:
                    self._items.append(RefundItemVO.from_alipay_dict(i))
    @property
    def medicare(self):
        return self._medicare

    @medicare.setter
    def medicare(self, value):
        if isinstance(value, MedicareVO):
            self._medicare = value
        else:
            self._medicare = MedicareVO.from_alipay_dict(value)
    @property
    def mi_amount(self):
        return self._mi_amount

    @mi_amount.setter
    def mi_amount(self, value):
        self._mi_amount = value
    @property
    def operator_role(self):
        return self._operator_role

    @operator_role.setter
    def operator_role(self, value):
        self._operator_role = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def packing_fee(self):
        return self._packing_fee

    @packing_fee.setter
    def packing_fee(self, value):
        self._packing_fee = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def refund_msg(self):
        return self._refund_msg

    @refund_msg.setter
    def refund_msg(self, value):
        self._refund_msg = value
    @property
    def refund_order_no(self):
        return self._refund_order_no

    @refund_order_no.setter
    def refund_order_no(self, value):
        self._refund_order_no = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def refuse_reason_code(self):
        return self._refuse_reason_code

    @refuse_reason_code.setter
    def refuse_reason_code(self, value):
        self._refuse_reason_code = value
    @property
    def success_time(self):
        return self._success_time

    @success_time.setter
    def success_time(self, value):
        self._success_time = value
    @property
    def time_markup_price(self):
        return self._time_markup_price

    @time_markup_price.setter
    def time_markup_price(self, value):
        self._time_markup_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.amount_item:
            if hasattr(self.amount_item, 'to_alipay_dict'):
                params['amount_item'] = self.amount_item.to_alipay_dict()
            else:
                params['amount_item'] = self.amount_item
        if self.amount_user:
            if hasattr(self.amount_user, 'to_alipay_dict'):
                params['amount_user'] = self.amount_user.to_alipay_dict()
            else:
                params['amount_user'] = self.amount_user
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.confirm_time:
            if hasattr(self.confirm_time, 'to_alipay_dict'):
                params['confirm_time'] = self.confirm_time.to_alipay_dict()
            else:
                params['confirm_time'] = self.confirm_time
        if self.delivery_discount_fee:
            if hasattr(self.delivery_discount_fee, 'to_alipay_dict'):
                params['delivery_discount_fee'] = self.delivery_discount_fee.to_alipay_dict()
            else:
                params['delivery_discount_fee'] = self.delivery_discount_fee
        if self.delivery_fee:
            if hasattr(self.delivery_fee, 'to_alipay_dict'):
                params['delivery_fee'] = self.delivery_fee.to_alipay_dict()
            else:
                params['delivery_fee'] = self.delivery_fee
        if self.delivery_price:
            if hasattr(self.delivery_price, 'to_alipay_dict'):
                params['delivery_price'] = self.delivery_price.to_alipay_dict()
            else:
                params['delivery_price'] = self.delivery_price
        if self.distance_markup_price:
            if hasattr(self.distance_markup_price, 'to_alipay_dict'):
                params['distance_markup_price'] = self.distance_markup_price.to_alipay_dict()
            else:
                params['distance_markup_price'] = self.distance_markup_price
        if self.images:
            if isinstance(self.images, list):
                for i in range(0, len(self.images)):
                    element = self.images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images[i] = element.to_alipay_dict()
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
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
        if self.medicare:
            if hasattr(self.medicare, 'to_alipay_dict'):
                params['medicare'] = self.medicare.to_alipay_dict()
            else:
                params['medicare'] = self.medicare
        if self.mi_amount:
            if hasattr(self.mi_amount, 'to_alipay_dict'):
                params['mi_amount'] = self.mi_amount.to_alipay_dict()
            else:
                params['mi_amount'] = self.mi_amount
        if self.operator_role:
            if hasattr(self.operator_role, 'to_alipay_dict'):
                params['operator_role'] = self.operator_role.to_alipay_dict()
            else:
                params['operator_role'] = self.operator_role
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.packing_fee:
            if hasattr(self.packing_fee, 'to_alipay_dict'):
                params['packing_fee'] = self.packing_fee.to_alipay_dict()
            else:
                params['packing_fee'] = self.packing_fee
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.refund_msg:
            if hasattr(self.refund_msg, 'to_alipay_dict'):
                params['refund_msg'] = self.refund_msg.to_alipay_dict()
            else:
                params['refund_msg'] = self.refund_msg
        if self.refund_order_no:
            if hasattr(self.refund_order_no, 'to_alipay_dict'):
                params['refund_order_no'] = self.refund_order_no.to_alipay_dict()
            else:
                params['refund_order_no'] = self.refund_order_no
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        if self.refuse_reason:
            if hasattr(self.refuse_reason, 'to_alipay_dict'):
                params['refuse_reason'] = self.refuse_reason.to_alipay_dict()
            else:
                params['refuse_reason'] = self.refuse_reason
        if self.refuse_reason_code:
            if hasattr(self.refuse_reason_code, 'to_alipay_dict'):
                params['refuse_reason_code'] = self.refuse_reason_code.to_alipay_dict()
            else:
                params['refuse_reason_code'] = self.refuse_reason_code
        if self.success_time:
            if hasattr(self.success_time, 'to_alipay_dict'):
                params['success_time'] = self.success_time.to_alipay_dict()
            else:
                params['success_time'] = self.success_time
        if self.time_markup_price:
            if hasattr(self.time_markup_price, 'to_alipay_dict'):
                params['time_markup_price'] = self.time_markup_price.to_alipay_dict()
            else:
                params['time_markup_price'] = self.time_markup_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundOrderDetailVO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'amount_item' in d:
            o.amount_item = d['amount_item']
        if 'amount_user' in d:
            o.amount_user = d['amount_user']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'confirm_time' in d:
            o.confirm_time = d['confirm_time']
        if 'delivery_discount_fee' in d:
            o.delivery_discount_fee = d['delivery_discount_fee']
        if 'delivery_fee' in d:
            o.delivery_fee = d['delivery_fee']
        if 'delivery_price' in d:
            o.delivery_price = d['delivery_price']
        if 'distance_markup_price' in d:
            o.distance_markup_price = d['distance_markup_price']
        if 'images' in d:
            o.images = d['images']
        if 'items' in d:
            o.items = d['items']
        if 'medicare' in d:
            o.medicare = d['medicare']
        if 'mi_amount' in d:
            o.mi_amount = d['mi_amount']
        if 'operator_role' in d:
            o.operator_role = d['operator_role']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'packing_fee' in d:
            o.packing_fee = d['packing_fee']
        if 'reason' in d:
            o.reason = d['reason']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'refund_msg' in d:
            o.refund_msg = d['refund_msg']
        if 'refund_order_no' in d:
            o.refund_order_no = d['refund_order_no']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        if 'refuse_reason' in d:
            o.refuse_reason = d['refuse_reason']
        if 'refuse_reason_code' in d:
            o.refuse_reason_code = d['refuse_reason_code']
        if 'success_time' in d:
            o.success_time = d['success_time']
        if 'time_markup_price' in d:
            o.time_markup_price = d['time_markup_price']
        return o


