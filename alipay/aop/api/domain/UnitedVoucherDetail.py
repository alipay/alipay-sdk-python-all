#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnitedVoucherDetail(object):

    def __init__(self):
        self._active_time = None
        self._camp_order_id = None
        self._ceiling_amount = None
        self._description = None
        self._discount_type = None
        self._expired_time = None
        self._from_amount = None
        self._prize_id = None
        self._prize_send_time = None
        self._reduction_ratio = None
        self._show_order = None
        self._status = None
        self._template_id = None
        self._to_amount = None
        self._voucher_biz_code = None
        self._voucher_id = None

    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def camp_order_id(self):
        return self._camp_order_id

    @camp_order_id.setter
    def camp_order_id(self, value):
        self._camp_order_id = value
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def from_amount(self):
        return self._from_amount

    @from_amount.setter
    def from_amount(self, value):
        self._from_amount = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_send_time(self):
        return self._prize_send_time

    @prize_send_time.setter
    def prize_send_time(self, value):
        self._prize_send_time = value
    @property
    def reduction_ratio(self):
        return self._reduction_ratio

    @reduction_ratio.setter
    def reduction_ratio(self, value):
        self._reduction_ratio = value
    @property
    def show_order(self):
        return self._show_order

    @show_order.setter
    def show_order(self, value):
        self._show_order = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def to_amount(self):
        return self._to_amount

    @to_amount.setter
    def to_amount(self, value):
        self._to_amount = value
    @property
    def voucher_biz_code(self):
        return self._voucher_biz_code

    @voucher_biz_code.setter
    def voucher_biz_code(self, value):
        self._voucher_biz_code = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.camp_order_id:
            if hasattr(self.camp_order_id, 'to_alipay_dict'):
                params['camp_order_id'] = self.camp_order_id.to_alipay_dict()
            else:
                params['camp_order_id'] = self.camp_order_id
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.from_amount:
            if hasattr(self.from_amount, 'to_alipay_dict'):
                params['from_amount'] = self.from_amount.to_alipay_dict()
            else:
                params['from_amount'] = self.from_amount
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_send_time:
            if hasattr(self.prize_send_time, 'to_alipay_dict'):
                params['prize_send_time'] = self.prize_send_time.to_alipay_dict()
            else:
                params['prize_send_time'] = self.prize_send_time
        if self.reduction_ratio:
            if hasattr(self.reduction_ratio, 'to_alipay_dict'):
                params['reduction_ratio'] = self.reduction_ratio.to_alipay_dict()
            else:
                params['reduction_ratio'] = self.reduction_ratio
        if self.show_order:
            if hasattr(self.show_order, 'to_alipay_dict'):
                params['show_order'] = self.show_order.to_alipay_dict()
            else:
                params['show_order'] = self.show_order
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.to_amount:
            if hasattr(self.to_amount, 'to_alipay_dict'):
                params['to_amount'] = self.to_amount.to_alipay_dict()
            else:
                params['to_amount'] = self.to_amount
        if self.voucher_biz_code:
            if hasattr(self.voucher_biz_code, 'to_alipay_dict'):
                params['voucher_biz_code'] = self.voucher_biz_code.to_alipay_dict()
            else:
                params['voucher_biz_code'] = self.voucher_biz_code
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnitedVoucherDetail()
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'camp_order_id' in d:
            o.camp_order_id = d['camp_order_id']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'description' in d:
            o.description = d['description']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'from_amount' in d:
            o.from_amount = d['from_amount']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_send_time' in d:
            o.prize_send_time = d['prize_send_time']
        if 'reduction_ratio' in d:
            o.reduction_ratio = d['reduction_ratio']
        if 'show_order' in d:
            o.show_order = d['show_order']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'to_amount' in d:
            o.to_amount = d['to_amount']
        if 'voucher_biz_code' in d:
            o.voucher_biz_code = d['voucher_biz_code']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


