#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTourVoucherRefundModel(object):

    def __init__(self):
        self._open_id = None
        self._order_id = None
        self._out_refund_id = None
        self._out_voucher_list = None
        self._refund = None
        self._refund_reason = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_refund_id(self):
        return self._out_refund_id

    @out_refund_id.setter
    def out_refund_id(self, value):
        self._out_refund_id = value
    @property
    def out_voucher_list(self):
        return self._out_voucher_list

    @out_voucher_list.setter
    def out_voucher_list(self, value):
        if isinstance(value, list):
            self._out_voucher_list = list()
            for i in value:
                self._out_voucher_list.append(i)
    @property
    def refund(self):
        return self._refund

    @refund.setter
    def refund(self, value):
        self._refund = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_refund_id:
            if hasattr(self.out_refund_id, 'to_alipay_dict'):
                params['out_refund_id'] = self.out_refund_id.to_alipay_dict()
            else:
                params['out_refund_id'] = self.out_refund_id
        if self.out_voucher_list:
            if isinstance(self.out_voucher_list, list):
                for i in range(0, len(self.out_voucher_list)):
                    element = self.out_voucher_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_voucher_list[i] = element.to_alipay_dict()
            if hasattr(self.out_voucher_list, 'to_alipay_dict'):
                params['out_voucher_list'] = self.out_voucher_list.to_alipay_dict()
            else:
                params['out_voucher_list'] = self.out_voucher_list
        if self.refund:
            if hasattr(self.refund, 'to_alipay_dict'):
                params['refund'] = self.refund.to_alipay_dict()
            else:
                params['refund'] = self.refund
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
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
        o = AlipayCommerceTransportTourVoucherRefundModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_refund_id' in d:
            o.out_refund_id = d['out_refund_id']
        if 'out_voucher_list' in d:
            o.out_voucher_list = d['out_voucher_list']
        if 'refund' in d:
            o.refund = d['refund']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


