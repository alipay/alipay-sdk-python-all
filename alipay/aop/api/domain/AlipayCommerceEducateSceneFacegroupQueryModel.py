#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSceneFacegroupQueryModel(object):

    def __init__(self):
        self._alipay_school_id = None

    @property
    def alipay_school_id(self):
        return self._alipay_school_id

    @alipay_school_id.setter
    def alipay_school_id(self, value):
        self._alipay_school_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_school_id:
            if hasattr(self.alipay_school_id, 'to_alipay_dict'):
                params['alipay_school_id'] = self.alipay_school_id.to_alipay_dict()
            else:
                params['alipay_school_id'] = self.alipay_school_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSceneFacegroupQueryModel()
        if 'alipay_school_id' in d:
            o.alipay_school_id = d['alipay_school_id']
        return o


