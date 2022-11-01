#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerLiferecordQuitModel(object):

    def __init__(self):
        self._action = None
        self._open_id = None
        self._out_biz_nos = None
        self._user_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_nos(self):
        return self._out_biz_nos

    @out_biz_nos.setter
    def out_biz_nos(self, value):
        if isinstance(value, list):
            self._out_biz_nos = list()
            for i in value:
                self._out_biz_nos.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_nos:
            if isinstance(self.out_biz_nos, list):
                for i in range(0, len(self.out_biz_nos)):
                    element = self.out_biz_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_biz_nos[i] = element.to_alipay_dict()
            if hasattr(self.out_biz_nos, 'to_alipay_dict'):
                params['out_biz_nos'] = self.out_biz_nos.to_alipay_dict()
            else:
                params['out_biz_nos'] = self.out_biz_nos
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
        o = ZhimaCustomerLiferecordQuitModel()
        if 'action' in d:
            o.action = d['action']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_nos' in d:
            o.out_biz_nos = d['out_biz_nos']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


