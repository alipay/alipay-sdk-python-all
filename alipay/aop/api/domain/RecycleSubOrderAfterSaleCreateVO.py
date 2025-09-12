#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleSubOrderAfterSaleCreateVO(object):

    def __init__(self):
        self._after_sale_reason = None
        self._after_sale_type = None
        self._sub_order_id = None
        self._sub_out_order_id = None

    @property
    def after_sale_reason(self):
        return self._after_sale_reason

    @after_sale_reason.setter
    def after_sale_reason(self, value):
        self._after_sale_reason = value
    @property
    def after_sale_type(self):
        return self._after_sale_type

    @after_sale_type.setter
    def after_sale_type(self, value):
        self._after_sale_type = value
    @property
    def sub_order_id(self):
        return self._sub_order_id

    @sub_order_id.setter
    def sub_order_id(self, value):
        self._sub_order_id = value
    @property
    def sub_out_order_id(self):
        return self._sub_out_order_id

    @sub_out_order_id.setter
    def sub_out_order_id(self, value):
        self._sub_out_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_sale_reason:
            if hasattr(self.after_sale_reason, 'to_alipay_dict'):
                params['after_sale_reason'] = self.after_sale_reason.to_alipay_dict()
            else:
                params['after_sale_reason'] = self.after_sale_reason
        if self.after_sale_type:
            if hasattr(self.after_sale_type, 'to_alipay_dict'):
                params['after_sale_type'] = self.after_sale_type.to_alipay_dict()
            else:
                params['after_sale_type'] = self.after_sale_type
        if self.sub_order_id:
            if hasattr(self.sub_order_id, 'to_alipay_dict'):
                params['sub_order_id'] = self.sub_order_id.to_alipay_dict()
            else:
                params['sub_order_id'] = self.sub_order_id
        if self.sub_out_order_id:
            if hasattr(self.sub_out_order_id, 'to_alipay_dict'):
                params['sub_out_order_id'] = self.sub_out_order_id.to_alipay_dict()
            else:
                params['sub_out_order_id'] = self.sub_out_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSubOrderAfterSaleCreateVO()
        if 'after_sale_reason' in d:
            o.after_sale_reason = d['after_sale_reason']
        if 'after_sale_type' in d:
            o.after_sale_type = d['after_sale_type']
        if 'sub_order_id' in d:
            o.sub_order_id = d['sub_order_id']
        if 'sub_out_order_id' in d:
            o.sub_out_order_id = d['sub_out_order_id']
        return o


