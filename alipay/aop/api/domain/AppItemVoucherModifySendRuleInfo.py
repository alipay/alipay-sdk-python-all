#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppItemVoucherModifySendRuleInfo(object):

    def __init__(self):
        self._publish_end_time = None

    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherModifySendRuleInfo()
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        return o


