#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizTagExtParams import BizTagExtParams


class BizTagEntity(object):

    def __init__(self):
        self._biz_tag_ext_params = None
        self._name = None

    @property
    def biz_tag_ext_params(self):
        return self._biz_tag_ext_params

    @biz_tag_ext_params.setter
    def biz_tag_ext_params(self, value):
        if isinstance(value, BizTagExtParams):
            self._biz_tag_ext_params = value
        else:
            self._biz_tag_ext_params = BizTagExtParams.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tag_ext_params:
            if hasattr(self.biz_tag_ext_params, 'to_alipay_dict'):
                params['biz_tag_ext_params'] = self.biz_tag_ext_params.to_alipay_dict()
            else:
                params['biz_tag_ext_params'] = self.biz_tag_ext_params
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizTagEntity()
        if 'biz_tag_ext_params' in d:
            o.biz_tag_ext_params = d['biz_tag_ext_params']
        if 'name' in d:
            o.name = d['name']
        return o


