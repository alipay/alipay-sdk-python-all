#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentInfoModel import ContentInfoModel


class BoothContentInfoModel(object):

    def __init__(self):
        self._booth = None
        self._content_info_list = None

    @property
    def booth(self):
        return self._booth

    @booth.setter
    def booth(self, value):
        self._booth = value
    @property
    def content_info_list(self):
        return self._content_info_list

    @content_info_list.setter
    def content_info_list(self, value):
        if isinstance(value, list):
            self._content_info_list = list()
            for i in value:
                if isinstance(i, ContentInfoModel):
                    self._content_info_list.append(i)
                else:
                    self._content_info_list.append(ContentInfoModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.booth:
            if hasattr(self.booth, 'to_alipay_dict'):
                params['booth'] = self.booth.to_alipay_dict()
            else:
                params['booth'] = self.booth
        if self.content_info_list:
            if isinstance(self.content_info_list, list):
                for i in range(0, len(self.content_info_list)):
                    element = self.content_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_info_list[i] = element.to_alipay_dict()
            if hasattr(self.content_info_list, 'to_alipay_dict'):
                params['content_info_list'] = self.content_info_list.to_alipay_dict()
            else:
                params['content_info_list'] = self.content_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoothContentInfoModel()
        if 'booth' in d:
            o.booth = d['booth']
        if 'content_info_list' in d:
            o.content_info_list = d['content_info_list']
        return o


