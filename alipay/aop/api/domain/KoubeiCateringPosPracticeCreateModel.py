#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosPracticeCreateModel(object):

    def __init__(self):
        self._practice_name = None
        self._shop_id = None

    @property
    def practice_name(self):
        return self._practice_name

    @practice_name.setter
    def practice_name(self, value):
        self._practice_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.practice_name:
            if hasattr(self.practice_name, 'to_alipay_dict'):
                params['practice_name'] = self.practice_name.to_alipay_dict()
            else:
                params['practice_name'] = self.practice_name
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
        o = KoubeiCateringPosPracticeCreateModel()
        if 'practice_name' in d:
            o.practice_name = d['practice_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


