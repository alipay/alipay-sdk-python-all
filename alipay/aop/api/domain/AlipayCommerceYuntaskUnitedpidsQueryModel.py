#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskUnitedpidsQueryModel(object):

    def __init__(self):
        self._united_id = None

    @property
    def united_id(self):
        return self._united_id

    @united_id.setter
    def united_id(self, value):
        self._united_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.united_id:
            if hasattr(self.united_id, 'to_alipay_dict'):
                params['united_id'] = self.united_id.to_alipay_dict()
            else:
                params['united_id'] = self.united_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskUnitedpidsQueryModel()
        if 'united_id' in d:
            o.united_id = d['united_id']
        return o


