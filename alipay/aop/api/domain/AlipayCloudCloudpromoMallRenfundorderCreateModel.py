#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMallRenfundorderCreateModel(object):

    def __init__(self):
        self._biz_claim_type = None
        self._goods_status = None
        self._order_line_id = None
        self._reason_text_id = None
        self._refund_count = None
        self._refund_fee = None

    @property
    def biz_claim_type(self):
        return self._biz_claim_type

    @biz_claim_type.setter
    def biz_claim_type(self, value):
        self._biz_claim_type = value
    @property
    def goods_status(self):
        return self._goods_status

    @goods_status.setter
    def goods_status(self, value):
        self._goods_status = value
    @property
    def order_line_id(self):
        return self._order_line_id

    @order_line_id.setter
    def order_line_id(self, value):
        self._order_line_id = value
    @property
    def reason_text_id(self):
        return self._reason_text_id

    @reason_text_id.setter
    def reason_text_id(self, value):
        self._reason_text_id = value
    @property
    def refund_count(self):
        return self._refund_count

    @refund_count.setter
    def refund_count(self, value):
        self._refund_count = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_claim_type:
            if hasattr(self.biz_claim_type, 'to_alipay_dict'):
                params['biz_claim_type'] = self.biz_claim_type.to_alipay_dict()
            else:
                params['biz_claim_type'] = self.biz_claim_type
        if self.goods_status:
            if hasattr(self.goods_status, 'to_alipay_dict'):
                params['goods_status'] = self.goods_status.to_alipay_dict()
            else:
                params['goods_status'] = self.goods_status
        if self.order_line_id:
            if hasattr(self.order_line_id, 'to_alipay_dict'):
                params['order_line_id'] = self.order_line_id.to_alipay_dict()
            else:
                params['order_line_id'] = self.order_line_id
        if self.reason_text_id:
            if hasattr(self.reason_text_id, 'to_alipay_dict'):
                params['reason_text_id'] = self.reason_text_id.to_alipay_dict()
            else:
                params['reason_text_id'] = self.reason_text_id
        if self.refund_count:
            if hasattr(self.refund_count, 'to_alipay_dict'):
                params['refund_count'] = self.refund_count.to_alipay_dict()
            else:
                params['refund_count'] = self.refund_count
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallRenfundorderCreateModel()
        if 'biz_claim_type' in d:
            o.biz_claim_type = d['biz_claim_type']
        if 'goods_status' in d:
            o.goods_status = d['goods_status']
        if 'order_line_id' in d:
            o.order_line_id = d['order_line_id']
        if 'reason_text_id' in d:
            o.reason_text_id = d['reason_text_id']
        if 'refund_count' in d:
            o.refund_count = d['refund_count']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        return o


