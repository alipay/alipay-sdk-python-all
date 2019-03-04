#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContentPrizeInfoModel(object):

    def __init__(self):
        self._prize_id = None
        self._prize_logo = None
        self._prize_name = None

    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_logo(self):
        return self._prize_logo

    @prize_logo.setter
    def prize_logo(self, value):
        self._prize_logo = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_logo:
            if hasattr(self.prize_logo, 'to_alipay_dict'):
                params['prize_logo'] = self.prize_logo.to_alipay_dict()
            else:
                params['prize_logo'] = self.prize_logo
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentPrizeInfoModel()
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_logo' in d:
            o.prize_logo = d['prize_logo']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        return o


