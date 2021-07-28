#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishCommRuleShowInfo(object):

    def __init__(self):
        self._tag_ext_info = None
        self._tag_name = None
        self._tag_value = None

    @property
    def tag_ext_info(self):
        return self._tag_ext_info

    @tag_ext_info.setter
    def tag_ext_info(self, value):
        self._tag_ext_info = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value
    @property
    def tag_value(self):
        return self._tag_value

    @tag_value.setter
    def tag_value(self, value):
        self._tag_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_ext_info:
            if hasattr(self.tag_ext_info, 'to_alipay_dict'):
                params['tag_ext_info'] = self.tag_ext_info.to_alipay_dict()
            else:
                params['tag_ext_info'] = self.tag_ext_info
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        if self.tag_value:
            if hasattr(self.tag_value, 'to_alipay_dict'):
                params['tag_value'] = self.tag_value.to_alipay_dict()
            else:
                params['tag_value'] = self.tag_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishCommRuleShowInfo()
        if 'tag_ext_info' in d:
            o.tag_ext_info = d['tag_ext_info']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        if 'tag_value' in d:
            o.tag_value = d['tag_value']
        return o


