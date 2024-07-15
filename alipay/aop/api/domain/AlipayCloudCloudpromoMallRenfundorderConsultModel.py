#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMallRenfundorderConsultModel(object):

    def __init__(self):
        self._biz_claim_type = None
        self._goods_status = None
        self._order_line_id = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallRenfundorderConsultModel()
        if 'biz_claim_type' in d:
            o.biz_claim_type = d['biz_claim_type']
        if 'goods_status' in d:
            o.goods_status = d['goods_status']
        if 'order_line_id' in d:
            o.order_line_id = d['order_line_id']
        return o


