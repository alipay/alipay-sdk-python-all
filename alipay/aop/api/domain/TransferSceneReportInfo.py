#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferSceneReportInfo(object):

    def __init__(self):
        self._info_content = None
        self._info_type = None

    @property
    def info_content(self):
        return self._info_content

    @info_content.setter
    def info_content(self, value):
        self._info_content = value
    @property
    def info_type(self):
        return self._info_type

    @info_type.setter
    def info_type(self, value):
        self._info_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.info_content:
            if hasattr(self.info_content, 'to_alipay_dict'):
                params['info_content'] = self.info_content.to_alipay_dict()
            else:
                params['info_content'] = self.info_content
        if self.info_type:
            if hasattr(self.info_type, 'to_alipay_dict'):
                params['info_type'] = self.info_type.to_alipay_dict()
            else:
                params['info_type'] = self.info_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferSceneReportInfo()
        if 'info_content' in d:
            o.info_content = d['info_content']
        if 'info_type' in d:
            o.info_type = d['info_type']
        return o


