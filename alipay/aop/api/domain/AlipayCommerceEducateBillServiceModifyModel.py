#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduRefundInfo import EduRefundInfo


class AlipayCommerceEducateBillServiceModifyModel(object):

    def __init__(self):
        self._isv_order_no = None
        self._order_status = None
        self._refund_info = None
        self._source = None
        self._trade_no = None
        self._user_id = None

    @property
    def isv_order_no(self):
        return self._isv_order_no

    @isv_order_no.setter
    def isv_order_no(self, value):
        self._isv_order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def refund_info(self):
        return self._refund_info

    @refund_info.setter
    def refund_info(self, value):
        if isinstance(value, EduRefundInfo):
            self._refund_info = value
        else:
            self._refund_info = EduRefundInfo.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
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
        if self.isv_order_no:
            if hasattr(self.isv_order_no, 'to_alipay_dict'):
                params['isv_order_no'] = self.isv_order_no.to_alipay_dict()
            else:
                params['isv_order_no'] = self.isv_order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.refund_info:
            if hasattr(self.refund_info, 'to_alipay_dict'):
                params['refund_info'] = self.refund_info.to_alipay_dict()
            else:
                params['refund_info'] = self.refund_info
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayCommerceEducateBillServiceModifyModel()
        if 'isv_order_no' in d:
            o.isv_order_no = d['isv_order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'refund_info' in d:
            o.refund_info = d['refund_info']
        if 'source' in d:
            o.source = d['source']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


