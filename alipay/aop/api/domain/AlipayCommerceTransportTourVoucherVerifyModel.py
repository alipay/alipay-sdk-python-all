#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherVerifyInfo import VoucherVerifyInfo


class AlipayCommerceTransportTourVoucherVerifyModel(object):

    def __init__(self):
        self._ant_shop_id = None
        self._open_id = None
        self._operate_serial_id = None
        self._operate_time = None
        self._order_id = None
        self._user_id = None
        self._voucher_verify_info = None

    @property
    def ant_shop_id(self):
        return self._ant_shop_id

    @ant_shop_id.setter
    def ant_shop_id(self, value):
        self._ant_shop_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operate_serial_id(self):
        return self._operate_serial_id

    @operate_serial_id.setter
    def operate_serial_id(self, value):
        self._operate_serial_id = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_verify_info(self):
        return self._voucher_verify_info

    @voucher_verify_info.setter
    def voucher_verify_info(self, value):
        if isinstance(value, VoucherVerifyInfo):
            self._voucher_verify_info = value
        else:
            self._voucher_verify_info = VoucherVerifyInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ant_shop_id:
            if hasattr(self.ant_shop_id, 'to_alipay_dict'):
                params['ant_shop_id'] = self.ant_shop_id.to_alipay_dict()
            else:
                params['ant_shop_id'] = self.ant_shop_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operate_serial_id:
            if hasattr(self.operate_serial_id, 'to_alipay_dict'):
                params['operate_serial_id'] = self.operate_serial_id.to_alipay_dict()
            else:
                params['operate_serial_id'] = self.operate_serial_id
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.voucher_verify_info:
            if hasattr(self.voucher_verify_info, 'to_alipay_dict'):
                params['voucher_verify_info'] = self.voucher_verify_info.to_alipay_dict()
            else:
                params['voucher_verify_info'] = self.voucher_verify_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTourVoucherVerifyModel()
        if 'ant_shop_id' in d:
            o.ant_shop_id = d['ant_shop_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operate_serial_id' in d:
            o.operate_serial_id = d['operate_serial_id']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'voucher_verify_info' in d:
            o.voucher_verify_info = d['voucher_verify_info']
        return o


