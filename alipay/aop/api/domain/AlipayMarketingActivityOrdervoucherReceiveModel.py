#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderVoucherReceiveInfo import OrderVoucherReceiveInfo


class AlipayMarketingActivityOrdervoucherReceiveModel(object):

    def __init__(self):
        self._receive_info_list = None
        self._send_merchant_id = None
        self._send_merchant_open_id = None
        self._user_id = None
        self._user_open_id = None

    @property
    def receive_info_list(self):
        return self._receive_info_list

    @receive_info_list.setter
    def receive_info_list(self, value):
        if isinstance(value, list):
            self._receive_info_list = list()
            for i in value:
                if isinstance(i, OrderVoucherReceiveInfo):
                    self._receive_info_list.append(i)
                else:
                    self._receive_info_list.append(OrderVoucherReceiveInfo.from_alipay_dict(i))
    @property
    def send_merchant_id(self):
        return self._send_merchant_id

    @send_merchant_id.setter
    def send_merchant_id(self, value):
        self._send_merchant_id = value
    @property
    def send_merchant_open_id(self):
        return self._send_merchant_open_id

    @send_merchant_open_id.setter
    def send_merchant_open_id(self, value):
        self._send_merchant_open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.receive_info_list:
            if isinstance(self.receive_info_list, list):
                for i in range(0, len(self.receive_info_list)):
                    element = self.receive_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.receive_info_list[i] = element.to_alipay_dict()
            if hasattr(self.receive_info_list, 'to_alipay_dict'):
                params['receive_info_list'] = self.receive_info_list.to_alipay_dict()
            else:
                params['receive_info_list'] = self.receive_info_list
        if self.send_merchant_id:
            if hasattr(self.send_merchant_id, 'to_alipay_dict'):
                params['send_merchant_id'] = self.send_merchant_id.to_alipay_dict()
            else:
                params['send_merchant_id'] = self.send_merchant_id
        if self.send_merchant_open_id:
            if hasattr(self.send_merchant_open_id, 'to_alipay_dict'):
                params['send_merchant_open_id'] = self.send_merchant_open_id.to_alipay_dict()
            else:
                params['send_merchant_open_id'] = self.send_merchant_open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityOrdervoucherReceiveModel()
        if 'receive_info_list' in d:
            o.receive_info_list = d['receive_info_list']
        if 'send_merchant_id' in d:
            o.send_merchant_id = d['send_merchant_id']
        if 'send_merchant_open_id' in d:
            o.send_merchant_open_id = d['send_merchant_open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        return o


