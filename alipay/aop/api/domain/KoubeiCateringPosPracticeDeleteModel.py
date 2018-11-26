#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosPracticeDeleteModel(object):

    def __init__(self):
        self._practice_id = None
        self._shop_id = None

    @property
    def practice_id(self):
        return self._practice_id

    @practice_id.setter
    def practice_id(self, value):
        self._practice_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.practice_id:
            if hasattr(self.practice_id, 'to_alipay_dict'):
                params['practice_id'] = self.practice_id.to_alipay_dict()
            else:
                params['practice_id'] = self.practice_id
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
        o = KoubeiCateringPosPracticeDeleteModel()
        if 'practice_id' in d:
            o.practice_id = d['practice_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


