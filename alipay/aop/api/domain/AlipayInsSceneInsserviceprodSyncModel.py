#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInsserviceprodSyncModel(object):

    def __init__(self):
        self._biz_data = None
        self._cur_node = None
        self._order_no = None
        self._user_id = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def cur_node(self):
        return self._cur_node

    @cur_node.setter
    def cur_node(self, value):
        self._cur_node = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.cur_node:
            if hasattr(self.cur_node, 'to_alipay_dict'):
                params['cur_node'] = self.cur_node.to_alipay_dict()
            else:
                params['cur_node'] = self.cur_node
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
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
        o = AlipayInsSceneInsserviceprodSyncModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'cur_node' in d:
            o.cur_node = d['cur_node']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


