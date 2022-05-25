#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ManjiangTesttttttt import ManjiangTesttttttt


class AlipayCommerceAcommunicationSsmmmmmCaptureModel(object):

    def __init__(self):
        self._activity_id = None
        self._s = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        if isinstance(value, ManjiangTesttttttt):
            self._s = value
        else:
            self._s = ManjiangTesttttttt.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.s:
            if hasattr(self.s, 'to_alipay_dict'):
                params['s'] = self.s.to_alipay_dict()
            else:
                params['s'] = self.s
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationSsmmmmmCaptureModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 's' in d:
            o.s = d['s']
        return o


