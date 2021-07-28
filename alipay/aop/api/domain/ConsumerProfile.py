#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumerProfile(object):

    def __init__(self):
        self._consumer_profile = None

    @property
    def consumer_profile(self):
        return self._consumer_profile

    @consumer_profile.setter
    def consumer_profile(self, value):
        self._consumer_profile = value


    def to_alipay_dict(self):
        params = dict()
        if self.consumer_profile:
            if hasattr(self.consumer_profile, 'to_alipay_dict'):
                params['consumer_profile'] = self.consumer_profile.to_alipay_dict()
            else:
                params['consumer_profile'] = self.consumer_profile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerProfile()
        if 'consumer_profile' in d:
            o.consumer_profile = d['consumer_profile']
        return o


