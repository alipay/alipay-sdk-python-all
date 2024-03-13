#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationCreditphoneRefundModel(object):

    def __init__(self):
        self._alipay_biz_no = None
        self._alipay_open_id = None
        self._alipay_order_no = None
        self._alipay_user_id = None
        self._in_advance_order = None
        self._refund_request_no = None

    @property
    def alipay_biz_no(self):
        return self._alipay_biz_no

    @alipay_biz_no.setter
    def alipay_biz_no(self, value):
        self._alipay_biz_no = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def in_advance_order(self):
        return self._in_advance_order

    @in_advance_order.setter
    def in_advance_order(self, value):
        self._in_advance_order = value
    @property
    def refund_request_no(self):
        return self._refund_request_no

    @refund_request_no.setter
    def refund_request_no(self, value):
        self._refund_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_biz_no:
            if hasattr(self.alipay_biz_no, 'to_alipay_dict'):
                params['alipay_biz_no'] = self.alipay_biz_no.to_alipay_dict()
            else:
                params['alipay_biz_no'] = self.alipay_biz_no
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.in_advance_order:
            if hasattr(self.in_advance_order, 'to_alipay_dict'):
                params['in_advance_order'] = self.in_advance_order.to_alipay_dict()
            else:
                params['in_advance_order'] = self.in_advance_order
        if self.refund_request_no:
            if hasattr(self.refund_request_no, 'to_alipay_dict'):
                params['refund_request_no'] = self.refund_request_no.to_alipay_dict()
            else:
                params['refund_request_no'] = self.refund_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationCreditphoneRefundModel()
        if 'alipay_biz_no' in d:
            o.alipay_biz_no = d['alipay_biz_no']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'in_advance_order' in d:
            o.in_advance_order = d['in_advance_order']
        if 'refund_request_no' in d:
            o.refund_request_no = d['refund_request_no']
        return o


