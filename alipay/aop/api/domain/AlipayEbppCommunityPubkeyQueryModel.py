#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityPubkeyQueryModel(object):

    def __init__(self):
        self._isv_short_name = None

    @property
    def isv_short_name(self):
        return self._isv_short_name

    @isv_short_name.setter
    def isv_short_name(self, value):
        self._isv_short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_short_name:
            if hasattr(self.isv_short_name, 'to_alipay_dict'):
                params['isv_short_name'] = self.isv_short_name.to_alipay_dict()
            else:
                params['isv_short_name'] = self.isv_short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityPubkeyQueryModel()
        if 'isv_short_name' in d:
            o.isv_short_name = d['isv_short_name']
        return o


