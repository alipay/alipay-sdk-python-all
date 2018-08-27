#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneApplicationCancelModel(object):

    def __init__(self):
        self._application_no = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_no:
            if hasattr(self.application_no, 'to_alipay_dict'):
                params['application_no'] = self.application_no.to_alipay_dict()
            else:
                params['application_no'] = self.application_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneApplicationCancelModel()
        if 'application_no' in d:
            o.application_no = d['application_no']
        return o


