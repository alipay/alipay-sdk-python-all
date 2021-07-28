#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotNetflowInfoQueryModel(object):

    def __init__(self):
        self._device_tag = None

    @property
    def device_tag(self):
        return self._device_tag

    @device_tag.setter
    def device_tag(self, value):
        self._device_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_tag:
            if hasattr(self.device_tag, 'to_alipay_dict'):
                params['device_tag'] = self.device_tag.to_alipay_dict()
            else:
                params['device_tag'] = self.device_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotNetflowInfoQueryModel()
        if 'device_tag' in d:
            o.device_tag = d['device_tag']
        return o


