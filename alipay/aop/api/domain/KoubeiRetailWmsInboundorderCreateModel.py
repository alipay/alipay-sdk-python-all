#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InboundOrder import InboundOrder
from alipay.aop.api.domain.OperateContext import OperateContext
from alipay.aop.api.domain.InboundOrderLine import InboundOrderLine


class KoubeiRetailWmsInboundorderCreateModel(object):

    def __init__(self):
        self._inbound_order = None
        self._operate_context = None
        self._order_lines = None

    @property
    def inbound_order(self):
        return self._inbound_order

    @inbound_order.setter
    def inbound_order(self, value):
        if isinstance(value, InboundOrder):
            self._inbound_order = value
        else:
            self._inbound_order = InboundOrder.from_alipay_dict(value)
    @property
    def operate_context(self):
        return self._operate_context

    @operate_context.setter
    def operate_context(self, value):
        if isinstance(value, OperateContext):
            self._operate_context = value
        else:
            self._operate_context = OperateContext.from_alipay_dict(value)
    @property
    def order_lines(self):
        return self._order_lines

    @order_lines.setter
    def order_lines(self, value):
        if isinstance(value, list):
            self._order_lines = list()
            for i in value:
                if isinstance(i, InboundOrderLine):
                    self._order_lines.append(i)
                else:
                    self._order_lines.append(InboundOrderLine.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.inbound_order:
            if hasattr(self.inbound_order, 'to_alipay_dict'):
                params['inbound_order'] = self.inbound_order.to_alipay_dict()
            else:
                params['inbound_order'] = self.inbound_order
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.order_lines:
            if isinstance(self.order_lines, list):
                for i in range(0, len(self.order_lines)):
                    element = self.order_lines[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_lines[i] = element.to_alipay_dict()
            if hasattr(self.order_lines, 'to_alipay_dict'):
                params['order_lines'] = self.order_lines.to_alipay_dict()
            else:
                params['order_lines'] = self.order_lines
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsInboundorderCreateModel()
        if 'inbound_order' in d:
            o.inbound_order = d['inbound_order']
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'order_lines' in d:
            o.order_lines = d['order_lines']
        return o


