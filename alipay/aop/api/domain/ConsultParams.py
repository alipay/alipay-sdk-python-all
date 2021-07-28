#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultParams(object):

    def __init__(self):
        self._another_hid = None

    @property
    def another_hid(self):
        return self._another_hid

    @another_hid.setter
    def another_hid(self, value):
        self._another_hid = value


    def to_alipay_dict(self):
        params = dict()
        if self.another_hid:
            if hasattr(self.another_hid, 'to_alipay_dict'):
                params['another_hid'] = self.another_hid.to_alipay_dict()
            else:
                params['another_hid'] = self.another_hid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultParams()
        if 'another_hid' in d:
            o.another_hid = d['another_hid']
        return o


