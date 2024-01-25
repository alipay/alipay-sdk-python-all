#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryReceiveDTO import DeliveryReceiveDTO


class AlipayOpenMiniOrderDeliveryReceiveModel(object):

    def __init__(self):
        self._delivery_receive_list = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._user_id = None

    @property
    def delivery_receive_list(self):
        return self._delivery_receive_list

    @delivery_receive_list.setter
    def delivery_receive_list(self, value):
        if isinstance(value, list):
            self._delivery_receive_list = list()
            for i in value:
                if isinstance(i, DeliveryReceiveDTO):
                    self._delivery_receive_list.append(i)
                else:
                    self._delivery_receive_list.append(DeliveryReceiveDTO.from_alipay_dict(i))
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_receive_list:
            if isinstance(self.delivery_receive_list, list):
                for i in range(0, len(self.delivery_receive_list)):
                    element = self.delivery_receive_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_receive_list[i] = element.to_alipay_dict()
            if hasattr(self.delivery_receive_list, 'to_alipay_dict'):
                params['delivery_receive_list'] = self.delivery_receive_list.to_alipay_dict()
            else:
                params['delivery_receive_list'] = self.delivery_receive_list
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
        o = AlipayOpenMiniOrderDeliveryReceiveModel()
        if 'delivery_receive_list' in d:
            o.delivery_receive_list = d['delivery_receive_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


