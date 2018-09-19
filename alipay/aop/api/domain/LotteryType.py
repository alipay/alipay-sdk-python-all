#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LotteryType(object):

    def __init__(self):
        self._lottery_type_id = None
        self._lottery_type_name = None

    @property
    def lottery_type_id(self):
        return self._lottery_type_id

    @lottery_type_id.setter
    def lottery_type_id(self, value):
        self._lottery_type_id = value
    @property
    def lottery_type_name(self):
        return self._lottery_type_name

    @lottery_type_name.setter
    def lottery_type_name(self, value):
        self._lottery_type_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.lottery_type_id:
            if hasattr(self.lottery_type_id, 'to_alipay_dict'):
                params['lottery_type_id'] = self.lottery_type_id.to_alipay_dict()
            else:
                params['lottery_type_id'] = self.lottery_type_id
        if self.lottery_type_name:
            if hasattr(self.lottery_type_name, 'to_alipay_dict'):
                params['lottery_type_name'] = self.lottery_type_name.to_alipay_dict()
            else:
                params['lottery_type_name'] = self.lottery_type_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LotteryType()
        if 'lottery_type_id' in d:
            o.lottery_type_id = d['lottery_type_id']
        if 'lottery_type_name' in d:
            o.lottery_type_name = d['lottery_type_name']
        return o


