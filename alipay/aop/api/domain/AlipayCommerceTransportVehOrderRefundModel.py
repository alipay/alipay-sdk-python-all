#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubOrderRefundRequest import SubOrderRefundRequest


class AlipayCommerceTransportVehOrderRefundModel(object):

    def __init__(self):
        self._alipay_order_no = None
        self._order_type = None
        self._out_request_no = None
        self._refund_reason = None
        self._sub_order_refund_list = None
        self._trade_no = None
        self._user_id = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def sub_order_refund_list(self):
        return self._sub_order_refund_list

    @sub_order_refund_list.setter
    def sub_order_refund_list(self, value):
        if isinstance(value, list):
            self._sub_order_refund_list = list()
            for i in value:
                if isinstance(i, SubOrderRefundRequest):
                    self._sub_order_refund_list.append(i)
                else:
                    self._sub_order_refund_list.append(SubOrderRefundRequest.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.sub_order_refund_list:
            if isinstance(self.sub_order_refund_list, list):
                for i in range(0, len(self.sub_order_refund_list)):
                    element = self.sub_order_refund_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_order_refund_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_order_refund_list, 'to_alipay_dict'):
                params['sub_order_refund_list'] = self.sub_order_refund_list.to_alipay_dict()
            else:
                params['sub_order_refund_list'] = self.sub_order_refund_list
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AlipayCommerceTransportVehOrderRefundModel()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'sub_order_refund_list' in d:
            o.sub_order_refund_list = d['sub_order_refund_list']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


