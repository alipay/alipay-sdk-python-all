#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TempBusinessExtInfo(object):

    def __init__(self):
        self._custom_ext_info_str = None

    @property
    def custom_ext_info_str(self):
        return self._custom_ext_info_str

    @custom_ext_info_str.setter
    def custom_ext_info_str(self, value):
        self._custom_ext_info_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.custom_ext_info_str:
            if hasattr(self.custom_ext_info_str, 'to_alipay_dict'):
                params['custom_ext_info_str'] = self.custom_ext_info_str.to_alipay_dict()
            else:
                params['custom_ext_info_str'] = self.custom_ext_info_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TempBusinessExtInfo()
        if 'custom_ext_info_str' in d:
            o.custom_ext_info_str = d['custom_ext_info_str']
        return o


