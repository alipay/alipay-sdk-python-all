#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelShop(object):

    def __init__(self):
        self._progress = None
        self._shop_id = None

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.progress:
            if hasattr(self.progress, 'to_alipay_dict'):
                params['progress'] = self.progress.to_alipay_dict()
            else:
                params['progress'] = self.progress
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelShop()
        if 'progress' in d:
            o.progress = d['progress']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


