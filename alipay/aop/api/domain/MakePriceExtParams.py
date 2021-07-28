#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MakePriceExtParams(object):

    def __init__(self):
        self._ext_feature = None
        self._ext_info = None

    @property
    def ext_feature(self):
        return self._ext_feature

    @ext_feature.setter
    def ext_feature(self, value):
        self._ext_feature = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_feature:
            if hasattr(self.ext_feature, 'to_alipay_dict'):
                params['ext_feature'] = self.ext_feature.to_alipay_dict()
            else:
                params['ext_feature'] = self.ext_feature
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MakePriceExtParams()
        if 'ext_feature' in d:
            o.ext_feature = d['ext_feature']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        return o


