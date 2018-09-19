#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringOrderInfoSyncModel(object):

    def __init__(self):
        self._action = None
        self._action_info = None
        self._order_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def action_info(self):
        return self._action_info

    @action_info.setter
    def action_info(self, value):
        self._action_info = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.action_info:
            if hasattr(self.action_info, 'to_alipay_dict'):
                params['action_info'] = self.action_info.to_alipay_dict()
            else:
                params['action_info'] = self.action_info
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderInfoSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'action_info' in d:
            o.action_info = d['action_info']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


