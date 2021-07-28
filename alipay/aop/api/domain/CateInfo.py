#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CateInfo(object):

    def __init__(self):
        self._cate_code = None
        self._stage_code = None

    @property
    def cate_code(self):
        return self._cate_code

    @cate_code.setter
    def cate_code(self, value):
        self._cate_code = value
    @property
    def stage_code(self):
        return self._stage_code

    @stage_code.setter
    def stage_code(self, value):
        self._stage_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_code:
            if hasattr(self.cate_code, 'to_alipay_dict'):
                params['cate_code'] = self.cate_code.to_alipay_dict()
            else:
                params['cate_code'] = self.cate_code
        if self.stage_code:
            if hasattr(self.stage_code, 'to_alipay_dict'):
                params['stage_code'] = self.stage_code.to_alipay_dict()
            else:
                params['stage_code'] = self.stage_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CateInfo()
        if 'cate_code' in d:
            o.cate_code = d['cate_code']
        if 'stage_code' in d:
            o.stage_code = d['stage_code']
        return o


