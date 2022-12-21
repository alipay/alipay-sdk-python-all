#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSearchSubservicekeywordDeleteModel(object):

    def __init__(self):
        self._config_id = None
        self._target_appid = None

    @property
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value
    @property
    def target_appid(self):
        return self._target_appid

    @target_appid.setter
    def target_appid(self, value):
        self._target_appid = value


    def to_alipay_dict(self):
        params = dict()
        if self.config_id:
            if hasattr(self.config_id, 'to_alipay_dict'):
                params['config_id'] = self.config_id.to_alipay_dict()
            else:
                params['config_id'] = self.config_id
        if self.target_appid:
            if hasattr(self.target_appid, 'to_alipay_dict'):
                params['target_appid'] = self.target_appid.to_alipay_dict()
            else:
                params['target_appid'] = self.target_appid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSearchSubservicekeywordDeleteModel()
        if 'config_id' in d:
            o.config_id = d['config_id']
        if 'target_appid' in d:
            o.target_appid = d['target_appid']
        return o


