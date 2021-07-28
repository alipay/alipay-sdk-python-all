#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdPrincipaldmpSyncModel(object):

    def __init__(self):
        self._biz_token = None
        self._data_id = None
        self._data_name = None
        self._principal_tag = None
        self._strategy = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def data_name(self):
        return self._data_name

    @data_name.setter
    def data_name(self, value):
        self._data_name = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.data_name:
            if hasattr(self.data_name, 'to_alipay_dict'):
                params['data_name'] = self.data_name.to_alipay_dict()
            else:
                params['data_name'] = self.data_name
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.strategy:
            if hasattr(self.strategy, 'to_alipay_dict'):
                params['strategy'] = self.strategy.to_alipay_dict()
            else:
                params['strategy'] = self.strategy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdPrincipaldmpSyncModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'data_name' in d:
            o.data_name = d['data_name']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'strategy' in d:
            o.strategy = d['strategy']
        return o


