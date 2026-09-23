#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsMarketingInscouponQueryModel(object):

    def __init__(self):
        self._bind_voucher_id = None
        self._coupon_type = None
        self._open_id = None
        self._source = None
        self._user_id = None

    @property
    def bind_voucher_id(self):
        return self._bind_voucher_id

    @bind_voucher_id.setter
    def bind_voucher_id(self, value):
        self._bind_voucher_id = value
    @property
    def coupon_type(self):
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, value):
        if isinstance(value, list):
            self._coupon_type = list()
            for i in value:
                self._coupon_type.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_voucher_id:
            if hasattr(self.bind_voucher_id, 'to_alipay_dict'):
                params['bind_voucher_id'] = self.bind_voucher_id.to_alipay_dict()
            else:
                params['bind_voucher_id'] = self.bind_voucher_id
        if self.coupon_type:
            if isinstance(self.coupon_type, list):
                for i in range(0, len(self.coupon_type)):
                    element = self.coupon_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coupon_type[i] = element.to_alipay_dict()
            if hasattr(self.coupon_type, 'to_alipay_dict'):
                params['coupon_type'] = self.coupon_type.to_alipay_dict()
            else:
                params['coupon_type'] = self.coupon_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayInsMarketingInscouponQueryModel()
        if 'bind_voucher_id' in d:
            o.bind_voucher_id = d['bind_voucher_id']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


