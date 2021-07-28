#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmIsvInitializeModel(object):

    def __init__(self):
        self._isv_pub_key = None

    @property
    def isv_pub_key(self):
        return self._isv_pub_key

    @isv_pub_key.setter
    def isv_pub_key(self, value):
        self._isv_pub_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_pub_key:
            if hasattr(self.isv_pub_key, 'to_alipay_dict'):
                params['isv_pub_key'] = self.isv_pub_key.to_alipay_dict()
            else:
                params['isv_pub_key'] = self.isv_pub_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmIsvInitializeModel()
        if 'isv_pub_key' in d:
            o.isv_pub_key = d['isv_pub_key']
        return o


