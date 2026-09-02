#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReverseContentData import ReverseContentData


class AlipayCommerceMedicalHealthArchiveReverseModel(object):

    def __init__(self):
        self._content_data = None

    @property
    def content_data(self):
        return self._content_data

    @content_data.setter
    def content_data(self, value):
        if isinstance(value, ReverseContentData):
            self._content_data = value
        else:
            self._content_data = ReverseContentData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.content_data:
            if hasattr(self.content_data, 'to_alipay_dict'):
                params['content_data'] = self.content_data.to_alipay_dict()
            else:
                params['content_data'] = self.content_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthArchiveReverseModel()
        if 'content_data' in d:
            o.content_data = d['content_data']
        return o


