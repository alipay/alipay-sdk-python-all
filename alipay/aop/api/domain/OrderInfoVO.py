#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderInfoVO(object):

    def __init__(self):
        self._cancel_time = None
        self._confirm_time = None
        self._create_time = None
        self._delivery_time = None
        self._delivery_type = None
        self._finish_time = None
        self._mi_type = None
        self._note = None
        self._order_scene = None
        self._order_seq = None
        self._order_status = None
        self._pay_time = None
        self._pick_type = None
        self._pre_order_type = None
        self._predict_delivery_end_time = None
        self._predict_delivery_start_time = None
        self._quantity = None
        self._update_time = None
        self._user_expect_end_time = None
        self._user_expect_start_time = None
        self._weight = None

    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def confirm_time(self):
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, value):
        self._confirm_time = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        self._delivery_time = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def mi_type(self):
        return self._mi_type

    @mi_type.setter
    def mi_type(self, value):
        self._mi_type = value
    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value
    @property
    def order_scene(self):
        return self._order_scene

    @order_scene.setter
    def order_scene(self, value):
        self._order_scene = value
    @property
    def order_seq(self):
        return self._order_seq

    @order_seq.setter
    def order_seq(self, value):
        self._order_seq = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pick_type(self):
        return self._pick_type

    @pick_type.setter
    def pick_type(self, value):
        self._pick_type = value
    @property
    def pre_order_type(self):
        return self._pre_order_type

    @pre_order_type.setter
    def pre_order_type(self, value):
        self._pre_order_type = value
    @property
    def predict_delivery_end_time(self):
        return self._predict_delivery_end_time

    @predict_delivery_end_time.setter
    def predict_delivery_end_time(self, value):
        self._predict_delivery_end_time = value
    @property
    def predict_delivery_start_time(self):
        return self._predict_delivery_start_time

    @predict_delivery_start_time.setter
    def predict_delivery_start_time(self, value):
        self._predict_delivery_start_time = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def user_expect_end_time(self):
        return self._user_expect_end_time

    @user_expect_end_time.setter
    def user_expect_end_time(self, value):
        self._user_expect_end_time = value
    @property
    def user_expect_start_time(self):
        return self._user_expect_start_time

    @user_expect_start_time.setter
    def user_expect_start_time(self, value):
        self._user_expect_start_time = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.confirm_time:
            if hasattr(self.confirm_time, 'to_alipay_dict'):
                params['confirm_time'] = self.confirm_time.to_alipay_dict()
            else:
                params['confirm_time'] = self.confirm_time
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.delivery_time:
            if hasattr(self.delivery_time, 'to_alipay_dict'):
                params['delivery_time'] = self.delivery_time.to_alipay_dict()
            else:
                params['delivery_time'] = self.delivery_time
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.mi_type:
            if hasattr(self.mi_type, 'to_alipay_dict'):
                params['mi_type'] = self.mi_type.to_alipay_dict()
            else:
                params['mi_type'] = self.mi_type
        if self.note:
            if hasattr(self.note, 'to_alipay_dict'):
                params['note'] = self.note.to_alipay_dict()
            else:
                params['note'] = self.note
        if self.order_scene:
            if hasattr(self.order_scene, 'to_alipay_dict'):
                params['order_scene'] = self.order_scene.to_alipay_dict()
            else:
                params['order_scene'] = self.order_scene
        if self.order_seq:
            if hasattr(self.order_seq, 'to_alipay_dict'):
                params['order_seq'] = self.order_seq.to_alipay_dict()
            else:
                params['order_seq'] = self.order_seq
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.pick_type:
            if hasattr(self.pick_type, 'to_alipay_dict'):
                params['pick_type'] = self.pick_type.to_alipay_dict()
            else:
                params['pick_type'] = self.pick_type
        if self.pre_order_type:
            if hasattr(self.pre_order_type, 'to_alipay_dict'):
                params['pre_order_type'] = self.pre_order_type.to_alipay_dict()
            else:
                params['pre_order_type'] = self.pre_order_type
        if self.predict_delivery_end_time:
            if hasattr(self.predict_delivery_end_time, 'to_alipay_dict'):
                params['predict_delivery_end_time'] = self.predict_delivery_end_time.to_alipay_dict()
            else:
                params['predict_delivery_end_time'] = self.predict_delivery_end_time
        if self.predict_delivery_start_time:
            if hasattr(self.predict_delivery_start_time, 'to_alipay_dict'):
                params['predict_delivery_start_time'] = self.predict_delivery_start_time.to_alipay_dict()
            else:
                params['predict_delivery_start_time'] = self.predict_delivery_start_time
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.user_expect_end_time:
            if hasattr(self.user_expect_end_time, 'to_alipay_dict'):
                params['user_expect_end_time'] = self.user_expect_end_time.to_alipay_dict()
            else:
                params['user_expect_end_time'] = self.user_expect_end_time
        if self.user_expect_start_time:
            if hasattr(self.user_expect_start_time, 'to_alipay_dict'):
                params['user_expect_start_time'] = self.user_expect_start_time.to_alipay_dict()
            else:
                params['user_expect_start_time'] = self.user_expect_start_time
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderInfoVO()
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'confirm_time' in d:
            o.confirm_time = d['confirm_time']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'delivery_time' in d:
            o.delivery_time = d['delivery_time']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'mi_type' in d:
            o.mi_type = d['mi_type']
        if 'note' in d:
            o.note = d['note']
        if 'order_scene' in d:
            o.order_scene = d['order_scene']
        if 'order_seq' in d:
            o.order_seq = d['order_seq']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'pick_type' in d:
            o.pick_type = d['pick_type']
        if 'pre_order_type' in d:
            o.pre_order_type = d['pre_order_type']
        if 'predict_delivery_end_time' in d:
            o.predict_delivery_end_time = d['predict_delivery_end_time']
        if 'predict_delivery_start_time' in d:
            o.predict_delivery_start_time = d['predict_delivery_start_time']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'user_expect_end_time' in d:
            o.user_expect_end_time = d['user_expect_end_time']
        if 'user_expect_start_time' in d:
            o.user_expect_start_time = d['user_expect_start_time']
        if 'weight' in d:
            o.weight = d['weight']
        return o


