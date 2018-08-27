#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringEleOrderSyncModel(object):

    def __init__(self):
        self._action = None
        self._alipay_user_id = None
        self._data = None
        self._source = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringEleOrderSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'data' in d:
            o.data = d['data']
        if 'source' in d:
            o.source = d['source']
        return o


