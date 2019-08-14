#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradePrecreateConfirmExtendParam(object):

    def __init__(self):
        self._precreate_code_from = None

    @property
    def precreate_code_from(self):
        return self._precreate_code_from

    @precreate_code_from.setter
    def precreate_code_from(self, value):
        self._precreate_code_from = value


    def to_alipay_dict(self):
        params = dict()
        if self.precreate_code_from:
            if hasattr(self.precreate_code_from, 'to_alipay_dict'):
                params['precreate_code_from'] = self.precreate_code_from.to_alipay_dict()
            else:
                params['precreate_code_from'] = self.precreate_code_from
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradePrecreateConfirmExtendParam()
        if 'precreate_code_from' in d:
            o.precreate_code_from = d['precreate_code_from']
        return o


