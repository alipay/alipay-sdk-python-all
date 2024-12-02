#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppTestPayModel(object):

    def __init__(self):
        self._body_date = None

    @property
    def body_date(self):
        return self._body_date

    @body_date.setter
    def body_date(self, value):
        self._body_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.body_date:
            if hasattr(self.body_date, 'to_alipay_dict'):
                params['body_date'] = self.body_date.to_alipay_dict()
            else:
                params['body_date'] = self.body_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppTestPayModel()
        if 'body_date' in d:
            o.body_date = d['body_date']
        return o


