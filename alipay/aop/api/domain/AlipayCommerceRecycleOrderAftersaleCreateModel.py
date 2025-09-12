#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleSubOrderAfterSaleCreateVO import RecycleSubOrderAfterSaleCreateVO


class AlipayCommerceRecycleOrderAftersaleCreateModel(object):

    def __init__(self):
        self._after_sale_reason = None
        self._after_sale_type = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._sub_order_after_sale_create_list = None
        self._user_id = None

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
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def sub_order_after_sale_create_list(self):
        return self._sub_order_after_sale_create_list

    @sub_order_after_sale_create_list.setter
    def sub_order_after_sale_create_list(self, value):
        if isinstance(value, list):
            self._sub_order_after_sale_create_list = list()
            for i in value:
                if isinstance(i, RecycleSubOrderAfterSaleCreateVO):
                    self._sub_order_after_sale_create_list.append(i)
                else:
                    self._sub_order_after_sale_create_list.append(RecycleSubOrderAfterSaleCreateVO.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.sub_order_after_sale_create_list:
            if isinstance(self.sub_order_after_sale_create_list, list):
                for i in range(0, len(self.sub_order_after_sale_create_list)):
                    element = self.sub_order_after_sale_create_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_order_after_sale_create_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_order_after_sale_create_list, 'to_alipay_dict'):
                params['sub_order_after_sale_create_list'] = self.sub_order_after_sale_create_list.to_alipay_dict()
            else:
                params['sub_order_after_sale_create_list'] = self.sub_order_after_sale_create_list
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
        o = AlipayCommerceRecycleOrderAftersaleCreateModel()
        if 'after_sale_reason' in d:
            o.after_sale_reason = d['after_sale_reason']
        if 'after_sale_type' in d:
            o.after_sale_type = d['after_sale_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'sub_order_after_sale_create_list' in d:
            o.sub_order_after_sale_create_list = d['sub_order_after_sale_create_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


