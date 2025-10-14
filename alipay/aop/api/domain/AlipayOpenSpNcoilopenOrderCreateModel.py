#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNcoilopenOrderCreateModel(object):

    def __init__(self):
        self._delivery_plan = None
        self._order_describe = None
        self._rebate_pid = None
        self._reference_id = None

    @property
    def delivery_plan(self):
        return self._delivery_plan

    @delivery_plan.setter
    def delivery_plan(self, value):
        self._delivery_plan = value
    @property
    def order_describe(self):
        return self._order_describe

    @order_describe.setter
    def order_describe(self, value):
        self._order_describe = value
    @property
    def rebate_pid(self):
        return self._rebate_pid

    @rebate_pid.setter
    def rebate_pid(self, value):
        self._rebate_pid = value
    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_plan:
            if hasattr(self.delivery_plan, 'to_alipay_dict'):
                params['delivery_plan'] = self.delivery_plan.to_alipay_dict()
            else:
                params['delivery_plan'] = self.delivery_plan
        if self.order_describe:
            if hasattr(self.order_describe, 'to_alipay_dict'):
                params['order_describe'] = self.order_describe.to_alipay_dict()
            else:
                params['order_describe'] = self.order_describe
        if self.rebate_pid:
            if hasattr(self.rebate_pid, 'to_alipay_dict'):
                params['rebate_pid'] = self.rebate_pid.to_alipay_dict()
            else:
                params['rebate_pid'] = self.rebate_pid
        if self.reference_id:
            if hasattr(self.reference_id, 'to_alipay_dict'):
                params['reference_id'] = self.reference_id.to_alipay_dict()
            else:
                params['reference_id'] = self.reference_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNcoilopenOrderCreateModel()
        if 'delivery_plan' in d:
            o.delivery_plan = d['delivery_plan']
        if 'order_describe' in d:
            o.order_describe = d['order_describe']
        if 'rebate_pid' in d:
            o.rebate_pid = d['rebate_pid']
        if 'reference_id' in d:
            o.reference_id = d['reference_id']
        return o


