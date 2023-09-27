#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppItempromoactivityTemplateQueryModel(object):

    def __init__(self):
        self._promotion_type = None

    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppItempromoactivityTemplateQueryModel()
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        return o


