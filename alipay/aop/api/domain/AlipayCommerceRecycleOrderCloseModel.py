#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleSubOrderCloseVO import RecycleSubOrderCloseVO


class AlipayCommerceRecycleOrderCloseModel(object):

    def __init__(self):
        self._close_reason = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._sub_order_close_list = None
        self._user_id = None

    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
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
    def sub_order_close_list(self):
        return self._sub_order_close_list

    @sub_order_close_list.setter
    def sub_order_close_list(self, value):
        if isinstance(value, list):
            self._sub_order_close_list = list()
            for i in value:
                if isinstance(i, RecycleSubOrderCloseVO):
                    self._sub_order_close_list.append(i)
                else:
                    self._sub_order_close_list.append(RecycleSubOrderCloseVO.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
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
        if self.sub_order_close_list:
            if isinstance(self.sub_order_close_list, list):
                for i in range(0, len(self.sub_order_close_list)):
                    element = self.sub_order_close_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_order_close_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_order_close_list, 'to_alipay_dict'):
                params['sub_order_close_list'] = self.sub_order_close_list.to_alipay_dict()
            else:
                params['sub_order_close_list'] = self.sub_order_close_list
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
        o = AlipayCommerceRecycleOrderCloseModel()
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'sub_order_close_list' in d:
            o.sub_order_close_list = d['sub_order_close_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


