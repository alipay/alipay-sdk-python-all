#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TagOperationRequest import TagOperationRequest


class AnttechOceanbaseObglobalTagCreateormodifyModel(object):

    def __init__(self):
        self._operate_tag_request = None

    @property
    def operate_tag_request(self):
        return self._operate_tag_request

    @operate_tag_request.setter
    def operate_tag_request(self, value):
        if isinstance(value, TagOperationRequest):
            self._operate_tag_request = value
        else:
            self._operate_tag_request = TagOperationRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.operate_tag_request:
            if hasattr(self.operate_tag_request, 'to_alipay_dict'):
                params['operate_tag_request'] = self.operate_tag_request.to_alipay_dict()
            else:
                params['operate_tag_request'] = self.operate_tag_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalTagCreateormodifyModel()
        if 'operate_tag_request' in d:
            o.operate_tag_request = d['operate_tag_request']
        return o


