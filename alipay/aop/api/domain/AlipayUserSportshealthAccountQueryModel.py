#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserSportshealthAccountQueryModel(object):

    def __init__(self):
        self._out_biz_channel = None

    @property
    def out_biz_channel(self):
        return self._out_biz_channel

    @out_biz_channel.setter
    def out_biz_channel(self, value):
        self._out_biz_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_channel:
            if hasattr(self.out_biz_channel, 'to_alipay_dict'):
                params['out_biz_channel'] = self.out_biz_channel.to_alipay_dict()
            else:
                params['out_biz_channel'] = self.out_biz_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserSportshealthAccountQueryModel()
        if 'out_biz_channel' in d:
            o.out_biz_channel = d['out_biz_channel']
        return o


