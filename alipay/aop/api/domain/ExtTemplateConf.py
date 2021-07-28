#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtTemplateConf(object):

    def __init__(self):
        self._buyer_id = None
        self._xxhm_info_id = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def xxhm_info_id(self):
        return self._xxhm_info_id

    @xxhm_info_id.setter
    def xxhm_info_id(self, value):
        self._xxhm_info_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.xxhm_info_id:
            if hasattr(self.xxhm_info_id, 'to_alipay_dict'):
                params['xxhm_info_id'] = self.xxhm_info_id.to_alipay_dict()
            else:
                params['xxhm_info_id'] = self.xxhm_info_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtTemplateConf()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'xxhm_info_id' in d:
            o.xxhm_info_id = d['xxhm_info_id']
        return o


