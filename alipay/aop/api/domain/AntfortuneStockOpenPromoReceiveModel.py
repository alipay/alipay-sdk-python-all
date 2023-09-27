#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TargetSendOrderParam import TargetSendOrderParam


class AntfortuneStockOpenPromoReceiveModel(object):

    def __init__(self):
        self._open_id = None
        self._target_send_order_list = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def target_send_order_list(self):
        return self._target_send_order_list

    @target_send_order_list.setter
    def target_send_order_list(self, value):
        if isinstance(value, list):
            self._target_send_order_list = list()
            for i in value:
                if isinstance(i, TargetSendOrderParam):
                    self._target_send_order_list.append(i)
                else:
                    self._target_send_order_list.append(TargetSendOrderParam.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.target_send_order_list:
            if isinstance(self.target_send_order_list, list):
                for i in range(0, len(self.target_send_order_list)):
                    element = self.target_send_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_send_order_list[i] = element.to_alipay_dict()
            if hasattr(self.target_send_order_list, 'to_alipay_dict'):
                params['target_send_order_list'] = self.target_send_order_list.to_alipay_dict()
            else:
                params['target_send_order_list'] = self.target_send_order_list
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
        o = AntfortuneStockOpenPromoReceiveModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'target_send_order_list' in d:
            o.target_send_order_list = d['target_send_order_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


