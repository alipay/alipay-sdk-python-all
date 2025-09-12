#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantContent(object):

    def __init__(self):
        self._link_type = None

    @property
    def link_type(self):
        return self._link_type

    @link_type.setter
    def link_type(self, value):
        self._link_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.link_type:
            if hasattr(self.link_type, 'to_alipay_dict'):
                params['link_type'] = self.link_type.to_alipay_dict()
            else:
                params['link_type'] = self.link_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantContent()
        if 'link_type' in d:
            o.link_type = d['link_type']
        return o


