#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsOutboundorderBatchqueryModel(object):

    def __init__(self):
        self._operate_context = None
        self._out_biz_no_list = None
        self._outbound_order_id_list = None

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
    def out_biz_no_list(self):
        return self._out_biz_no_list

    @out_biz_no_list.setter
    def out_biz_no_list(self, value):
        if isinstance(value, list):
            self._out_biz_no_list = list()
            for i in value:
                self._out_biz_no_list.append(i)
    @property
    def outbound_order_id_list(self):
        return self._outbound_order_id_list

    @outbound_order_id_list.setter
    def outbound_order_id_list(self, value):
        if isinstance(value, list):
            self._outbound_order_id_list = list()
            for i in value:
                self._outbound_order_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.out_biz_no_list:
            if isinstance(self.out_biz_no_list, list):
                for i in range(0, len(self.out_biz_no_list)):
                    element = self.out_biz_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_biz_no_list[i] = element.to_alipay_dict()
            if hasattr(self.out_biz_no_list, 'to_alipay_dict'):
                params['out_biz_no_list'] = self.out_biz_no_list.to_alipay_dict()
            else:
                params['out_biz_no_list'] = self.out_biz_no_list
        if self.outbound_order_id_list:
            if isinstance(self.outbound_order_id_list, list):
                for i in range(0, len(self.outbound_order_id_list)):
                    element = self.outbound_order_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.outbound_order_id_list[i] = element.to_alipay_dict()
            if hasattr(self.outbound_order_id_list, 'to_alipay_dict'):
                params['outbound_order_id_list'] = self.outbound_order_id_list.to_alipay_dict()
            else:
                params['outbound_order_id_list'] = self.outbound_order_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsOutboundorderBatchqueryModel()
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'out_biz_no_list' in d:
            o.out_biz_no_list = d['out_biz_no_list']
        if 'outbound_order_id_list' in d:
            o.outbound_order_id_list = d['outbound_order_id_list']
        return o


