#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsVunueOrdervoucherVerifyModel(object):

    def __init__(self):
        self._desc = None
        self._order_id = None
        self._out_order_id = None
        self._out_voucher_id = None
        self._verify_count = None
        self._verify_status = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_voucher_id(self):
        return self._out_voucher_id

    @out_voucher_id.setter
    def out_voucher_id(self, value):
        self._out_voucher_id = value
    @property
    def verify_count(self):
        return self._verify_count

    @verify_count.setter
    def verify_count(self, value):
        self._verify_count = value
    @property
    def verify_status(self):
        return self._verify_status

    @verify_status.setter
    def verify_status(self, value):
        self._verify_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_voucher_id:
            if hasattr(self.out_voucher_id, 'to_alipay_dict'):
                params['out_voucher_id'] = self.out_voucher_id.to_alipay_dict()
            else:
                params['out_voucher_id'] = self.out_voucher_id
        if self.verify_count:
            if hasattr(self.verify_count, 'to_alipay_dict'):
                params['verify_count'] = self.verify_count.to_alipay_dict()
            else:
                params['verify_count'] = self.verify_count
        if self.verify_status:
            if hasattr(self.verify_status, 'to_alipay_dict'):
                params['verify_status'] = self.verify_status.to_alipay_dict()
            else:
                params['verify_status'] = self.verify_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsVunueOrdervoucherVerifyModel()
        if 'desc' in d:
            o.desc = d['desc']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_voucher_id' in d:
            o.out_voucher_id = d['out_voucher_id']
        if 'verify_count' in d:
            o.verify_count = d['verify_count']
        if 'verify_status' in d:
            o.verify_status = d['verify_status']
        return o


