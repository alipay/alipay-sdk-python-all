#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Coupon(object):

    def __init__(self):
        self._available_amount = None
        self._coupon_no = None
        self._deduct_amount = None
        self._gmt_active = None
        self._gmt_create = None
        self._gmt_expired = None
        self._instructions = None
        self._memo = None
        self._merchant_uniq_id = None
        self._multi_use_flag = None
        self._name = None
        self._refund_flag = None
        self._status = None
        self._template_no = None
        self._user_id = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def coupon_no(self):
        return self._coupon_no

    @coupon_no.setter
    def coupon_no(self, value):
        self._coupon_no = value
    @property
    def deduct_amount(self):
        return self._deduct_amount

    @deduct_amount.setter
    def deduct_amount(self, value):
        self._deduct_amount = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def instructions(self):
        return self._instructions

    @instructions.setter
    def instructions(self, value):
        self._instructions = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_uniq_id(self):
        return self._merchant_uniq_id

    @merchant_uniq_id.setter
    def merchant_uniq_id(self, value):
        self._merchant_uniq_id = value
    @property
    def multi_use_flag(self):
        return self._multi_use_flag

    @multi_use_flag.setter
    def multi_use_flag(self, value):
        self._multi_use_flag = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def refund_flag(self):
        return self._refund_flag

    @refund_flag.setter
    def refund_flag(self, value):
        self._refund_flag = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_no(self):
        return self._template_no

    @template_no.setter
    def template_no(self, value):
        self._template_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.coupon_no:
            if hasattr(self.coupon_no, 'to_alipay_dict'):
                params['coupon_no'] = self.coupon_no.to_alipay_dict()
            else:
                params['coupon_no'] = self.coupon_no
        if self.deduct_amount:
            if hasattr(self.deduct_amount, 'to_alipay_dict'):
                params['deduct_amount'] = self.deduct_amount.to_alipay_dict()
            else:
                params['deduct_amount'] = self.deduct_amount
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.instructions:
            if hasattr(self.instructions, 'to_alipay_dict'):
                params['instructions'] = self.instructions.to_alipay_dict()
            else:
                params['instructions'] = self.instructions
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_uniq_id:
            if hasattr(self.merchant_uniq_id, 'to_alipay_dict'):
                params['merchant_uniq_id'] = self.merchant_uniq_id.to_alipay_dict()
            else:
                params['merchant_uniq_id'] = self.merchant_uniq_id
        if self.multi_use_flag:
            if hasattr(self.multi_use_flag, 'to_alipay_dict'):
                params['multi_use_flag'] = self.multi_use_flag.to_alipay_dict()
            else:
                params['multi_use_flag'] = self.multi_use_flag
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.refund_flag:
            if hasattr(self.refund_flag, 'to_alipay_dict'):
                params['refund_flag'] = self.refund_flag.to_alipay_dict()
            else:
                params['refund_flag'] = self.refund_flag
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_no:
            if hasattr(self.template_no, 'to_alipay_dict'):
                params['template_no'] = self.template_no.to_alipay_dict()
            else:
                params['template_no'] = self.template_no
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
        o = Coupon()
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'coupon_no' in d:
            o.coupon_no = d['coupon_no']
        if 'deduct_amount' in d:
            o.deduct_amount = d['deduct_amount']
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'instructions' in d:
            o.instructions = d['instructions']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_uniq_id' in d:
            o.merchant_uniq_id = d['merchant_uniq_id']
        if 'multi_use_flag' in d:
            o.multi_use_flag = d['multi_use_flag']
        if 'name' in d:
            o.name = d['name']
        if 'refund_flag' in d:
            o.refund_flag = d['refund_flag']
        if 'status' in d:
            o.status = d['status']
        if 'template_no' in d:
            o.template_no = d['template_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


