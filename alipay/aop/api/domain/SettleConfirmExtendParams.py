#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleConfirmExtendParams(object):

    def __init__(self):
        self._royalty_freeze = None

    @property
    def royalty_freeze(self):
        return self._royalty_freeze

    @royalty_freeze.setter
    def royalty_freeze(self, value):
        self._royalty_freeze = value


    def to_alipay_dict(self):
        params = dict()
        if self.royalty_freeze:
            if hasattr(self.royalty_freeze, 'to_alipay_dict'):
                params['royalty_freeze'] = self.royalty_freeze.to_alipay_dict()
            else:
                params['royalty_freeze'] = self.royalty_freeze
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleConfirmExtendParams()
        if 'royalty_freeze' in d:
            o.royalty_freeze = d['royalty_freeze']
        return o


