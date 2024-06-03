#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelPromotionStaticInfo(object):

    def __init__(self):
        self._desc = None
        self._tag = None
        self._type = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelPromotionStaticInfo()
        if 'desc' in d:
            o.desc = d['desc']
        if 'tag' in d:
            o.tag = d['tag']
        if 'type' in d:
            o.type = d['type']
        return o


