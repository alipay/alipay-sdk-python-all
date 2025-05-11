#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WelfareAuthExtResp(object):

    def __init__(self):
        self._corp_group = None

    @property
    def corp_group(self):
        return self._corp_group

    @corp_group.setter
    def corp_group(self, value):
        self._corp_group = value


    def to_alipay_dict(self):
        params = dict()
        if self.corp_group:
            if hasattr(self.corp_group, 'to_alipay_dict'):
                params['corp_group'] = self.corp_group.to_alipay_dict()
            else:
                params['corp_group'] = self.corp_group
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WelfareAuthExtResp()
        if 'corp_group' in d:
            o.corp_group = d['corp_group']
        return o


