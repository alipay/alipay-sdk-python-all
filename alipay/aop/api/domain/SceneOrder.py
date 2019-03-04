#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallDiscountDetail import MallDiscountDetail


class SceneOrder(object):

    def __init__(self):
        self._buyer_user_id = None
        self._discount_detail = None
        self._order_id = None
        self._order_type = None
        self._out_order_no = None
        self._real_amount = None
        self._scene_code = None
        self._seller_user_id = None
        self._status = None
        self._subject = None
        self._total_amount = None
        self._trade_no = None
        self._trade_success_time = None
        self._trade_time = None

    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def discount_detail(self):
        return self._discount_detail

    @discount_detail.setter
    def discount_detail(self, value):
        if isinstance(value, list):
            self._discount_detail = list()
            for i in value:
                if isinstance(i, MallDiscountDetail):
                    self._discount_detail.append(i)
                else:
                    self._discount_detail.append(MallDiscountDetail.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def seller_user_id(self):
        return self._seller_user_id

    @seller_user_id.setter
    def seller_user_id(self, value):
        self._seller_user_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_success_time(self):
        return self._trade_success_time

    @trade_success_time.setter
    def trade_success_time(self, value):
        self._trade_success_time = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_user_id:
            if hasattr(self.buyer_user_id, 'to_alipay_dict'):
                params['buyer_user_id'] = self.buyer_user_id.to_alipay_dict()
            else:
                params['buyer_user_id'] = self.buyer_user_id
        if self.discount_detail:
            if isinstance(self.discount_detail, list):
                for i in range(0, len(self.discount_detail)):
                    element = self.discount_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_detail[i] = element.to_alipay_dict()
            if hasattr(self.discount_detail, 'to_alipay_dict'):
                params['discount_detail'] = self.discount_detail.to_alipay_dict()
            else:
                params['discount_detail'] = self.discount_detail
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.seller_user_id:
            if hasattr(self.seller_user_id, 'to_alipay_dict'):
                params['seller_user_id'] = self.seller_user_id.to_alipay_dict()
            else:
                params['seller_user_id'] = self.seller_user_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_success_time:
            if hasattr(self.trade_success_time, 'to_alipay_dict'):
                params['trade_success_time'] = self.trade_success_time.to_alipay_dict()
            else:
                params['trade_success_time'] = self.trade_success_time
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneOrder()
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'discount_detail' in d:
            o.discount_detail = d['discount_detail']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'seller_user_id' in d:
            o.seller_user_id = d['seller_user_id']
        if 'status' in d:
            o.status = d['status']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_success_time' in d:
            o.trade_success_time = d['trade_success_time']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


