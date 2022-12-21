#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSearchAppkeywordquotaQueryModel(object):

    def __init__(self):
        self._target_appid = None

    @property
    def target_appid(self):
        return self._target_appid

    @target_appid.setter
    def target_appid(self, value):
        self._target_appid = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayOpenSearchAppkeywordquotaQueryModel()
        if 'target_appid' in d:
            o.target_appid = d['target_appid']
        return o


