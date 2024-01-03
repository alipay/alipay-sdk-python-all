#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenServicemarketQrcodeOfflineGetModel(object):

    def __init__(self):
        self._app_name = None
        self._callback = None
        self._merchandise_id = None
        self._ticket = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, value):
        self._callback = value
    @property
    def merchandise_id(self):
        return self._merchandise_id

    @merchandise_id.setter
    def merchandise_id(self, value):
        self._merchandise_id = value
    @property
    def ticket(self):
        return self._ticket

    @ticket.setter
    def ticket(self, value):
        self._ticket = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.callback:
            if hasattr(self.callback, 'to_alipay_dict'):
                params['callback'] = self.callback.to_alipay_dict()
            else:
                params['callback'] = self.callback
        if self.merchandise_id:
            if hasattr(self.merchandise_id, 'to_alipay_dict'):
                params['merchandise_id'] = self.merchandise_id.to_alipay_dict()
            else:
                params['merchandise_id'] = self.merchandise_id
        if self.ticket:
            if hasattr(self.ticket, 'to_alipay_dict'):
                params['ticket'] = self.ticket.to_alipay_dict()
            else:
                params['ticket'] = self.ticket
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketQrcodeOfflineGetModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'callback' in d:
            o.callback = d['callback']
        if 'merchandise_id' in d:
            o.merchandise_id = d['merchandise_id']
        if 'ticket' in d:
            o.ticket = d['ticket']
        return o


