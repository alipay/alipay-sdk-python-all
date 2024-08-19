#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreativeDeleteFailDetail(object):

    def __init__(self):
        self._creative_outer_id = None
        self._fail_reason = None

    @property
    def creative_outer_id(self):
        return self._creative_outer_id

    @creative_outer_id.setter
    def creative_outer_id(self, value):
        self._creative_outer_id = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.creative_outer_id:
            if hasattr(self.creative_outer_id, 'to_alipay_dict'):
                params['creative_outer_id'] = self.creative_outer_id.to_alipay_dict()
            else:
                params['creative_outer_id'] = self.creative_outer_id
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeDeleteFailDetail()
        if 'creative_outer_id' in d:
            o.creative_outer_id = d['creative_outer_id']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        return o


