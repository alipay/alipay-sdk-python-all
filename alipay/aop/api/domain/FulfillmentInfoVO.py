#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentBizInfo import FulfillmentBizInfo


class FulfillmentInfoVO(object):

    def __init__(self):
        self._fulfillment_biz_info = None
        self._fulfillment_id = None
        self._open_id = None
        self._trade_order_id = None
        self._type = None
        self._user_id = None

    @property
    def fulfillment_biz_info(self):
        return self._fulfillment_biz_info

    @fulfillment_biz_info.setter
    def fulfillment_biz_info(self, value):
        if isinstance(value, FulfillmentBizInfo):
            self._fulfillment_biz_info = value
        else:
            self._fulfillment_biz_info = FulfillmentBizInfo.from_alipay_dict(value)
    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def trade_order_id(self):
        return self._trade_order_id

    @trade_order_id.setter
    def trade_order_id(self, value):
        self._trade_order_id = value
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
        if self.fulfillment_biz_info:
            if hasattr(self.fulfillment_biz_info, 'to_alipay_dict'):
                params['fulfillment_biz_info'] = self.fulfillment_biz_info.to_alipay_dict()
            else:
                params['fulfillment_biz_info'] = self.fulfillment_biz_info
        if self.fulfillment_id:
            if hasattr(self.fulfillment_id, 'to_alipay_dict'):
                params['fulfillment_id'] = self.fulfillment_id.to_alipay_dict()
            else:
                params['fulfillment_id'] = self.fulfillment_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.trade_order_id:
            if hasattr(self.trade_order_id, 'to_alipay_dict'):
                params['trade_order_id'] = self.trade_order_id.to_alipay_dict()
            else:
                params['trade_order_id'] = self.trade_order_id
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
        o = FulfillmentInfoVO()
        if 'fulfillment_biz_info' in d:
            o.fulfillment_biz_info = d['fulfillment_biz_info']
        if 'fulfillment_id' in d:
            o.fulfillment_id = d['fulfillment_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'trade_order_id' in d:
            o.trade_order_id = d['trade_order_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


