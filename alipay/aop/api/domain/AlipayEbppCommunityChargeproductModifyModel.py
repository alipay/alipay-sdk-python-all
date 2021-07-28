#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityChargeproductModifyModel(object):

    def __init__(self):
        self._community_short_name = None
        self._maintaining_end = None
        self._maintaining_start = None

    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def maintaining_end(self):
        return self._maintaining_end

    @maintaining_end.setter
    def maintaining_end(self, value):
        self._maintaining_end = value
    @property
    def maintaining_start(self):
        return self._maintaining_start

    @maintaining_start.setter
    def maintaining_start(self, value):
        self._maintaining_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.maintaining_end:
            if hasattr(self.maintaining_end, 'to_alipay_dict'):
                params['maintaining_end'] = self.maintaining_end.to_alipay_dict()
            else:
                params['maintaining_end'] = self.maintaining_end
        if self.maintaining_start:
            if hasattr(self.maintaining_start, 'to_alipay_dict'):
                params['maintaining_start'] = self.maintaining_start.to_alipay_dict()
            else:
                params['maintaining_start'] = self.maintaining_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityChargeproductModifyModel()
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'maintaining_end' in d:
            o.maintaining_end = d['maintaining_end']
        if 'maintaining_start' in d:
            o.maintaining_start = d['maintaining_start']
        return o


