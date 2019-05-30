#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsHealthGiftBatchAlreadyOpenedResult(object):

    def __init__(self):
        self._already_opened = None
        self._biz_type = None

    @property
    def already_opened(self):
        return self._already_opened

    @already_opened.setter
    def already_opened(self, value):
        self._already_opened = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.already_opened:
            if hasattr(self.already_opened, 'to_alipay_dict'):
                params['already_opened'] = self.already_opened.to_alipay_dict()
            else:
                params['already_opened'] = self.already_opened
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsHealthGiftBatchAlreadyOpenedResult()
        if 'already_opened' in d:
            o.already_opened = d['already_opened']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        return o


