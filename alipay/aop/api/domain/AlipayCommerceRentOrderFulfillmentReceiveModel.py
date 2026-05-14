#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentAdditionalMediaInfo import FulfillmentAdditionalMediaInfo


class AlipayCommerceRentOrderFulfillmentReceiveModel(object):

    def __init__(self):
        self._additional_media_list = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._type = None
        self._user_id = None

    @property
    def additional_media_list(self):
        return self._additional_media_list

    @additional_media_list.setter
    def additional_media_list(self, value):
        if isinstance(value, list):
            self._additional_media_list = list()
            for i in value:
                if isinstance(i, FulfillmentAdditionalMediaInfo):
                    self._additional_media_list.append(i)
                else:
                    self._additional_media_list.append(FulfillmentAdditionalMediaInfo.from_alipay_dict(i))
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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_media_list:
            if isinstance(self.additional_media_list, list):
                for i in range(0, len(self.additional_media_list)):
                    element = self.additional_media_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.additional_media_list[i] = element.to_alipay_dict()
            if hasattr(self.additional_media_list, 'to_alipay_dict'):
                params['additional_media_list'] = self.additional_media_list.to_alipay_dict()
            else:
                params['additional_media_list'] = self.additional_media_list
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
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayCommerceRentOrderFulfillmentReceiveModel()
        if 'additional_media_list' in d:
            o.additional_media_list = d['additional_media_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


