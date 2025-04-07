#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LandingChannelInfoVO(object):

    def __init__(self):
        self._union_rent_tag = None

    @property
    def union_rent_tag(self):
        return self._union_rent_tag

    @union_rent_tag.setter
    def union_rent_tag(self, value):
        self._union_rent_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.union_rent_tag:
            if hasattr(self.union_rent_tag, 'to_alipay_dict'):
                params['union_rent_tag'] = self.union_rent_tag.to_alipay_dict()
            else:
                params['union_rent_tag'] = self.union_rent_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LandingChannelInfoVO()
        if 'union_rent_tag' in d:
            o.union_rent_tag = d['union_rent_tag']
        return o


