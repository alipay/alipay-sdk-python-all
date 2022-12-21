#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneMarketingUserThirdpartequityQueryModel(object):

    def __init__(self):
        self._equity_type = None
        self._open_id = None
        self._source = None
        self._user_id = None

    @property
    def equity_type(self):
        return self._equity_type

    @equity_type.setter
    def equity_type(self, value):
        self._equity_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.equity_type:
            if hasattr(self.equity_type, 'to_alipay_dict'):
                params['equity_type'] = self.equity_type.to_alipay_dict()
            else:
                params['equity_type'] = self.equity_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AntfortuneMarketingUserThirdpartequityQueryModel()
        if 'equity_type' in d:
            o.equity_type = d['equity_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


