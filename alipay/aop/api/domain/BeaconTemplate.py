#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BeaconTemplate(object):

    def __init__(self):
        self._context = None
        self._templateid = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value
    @property
    def templateid(self):
        return self._templateid

    @templateid.setter
    def templateid(self, value):
        self._templateid = value


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.templateid:
            if hasattr(self.templateid, 'to_alipay_dict'):
                params['templateid'] = self.templateid.to_alipay_dict()
            else:
                params['templateid'] = self.templateid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BeaconTemplate()
        if 'context' in d:
            o.context = d['context']
        if 'templateid' in d:
            o.templateid = d['templateid']
        return o


