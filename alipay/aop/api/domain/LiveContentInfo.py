#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LiveContentRiskInfo import LiveContentRiskInfo


class LiveContentInfo(object):

    def __init__(self):
        self._biz_content_type = None
        self._content_file_type = None
        self._content_id = None
        self._content_risk_info_list = None
        self._content_url = None
        self._mark_lable_name = None

    @property
    def biz_content_type(self):
        return self._biz_content_type

    @biz_content_type.setter
    def biz_content_type(self, value):
        self._biz_content_type = value
    @property
    def content_file_type(self):
        return self._content_file_type

    @content_file_type.setter
    def content_file_type(self, value):
        self._content_file_type = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def content_risk_info_list(self):
        return self._content_risk_info_list

    @content_risk_info_list.setter
    def content_risk_info_list(self, value):
        if isinstance(value, list):
            self._content_risk_info_list = list()
            for i in value:
                if isinstance(i, LiveContentRiskInfo):
                    self._content_risk_info_list.append(i)
                else:
                    self._content_risk_info_list.append(LiveContentRiskInfo.from_alipay_dict(i))
    @property
    def content_url(self):
        return self._content_url

    @content_url.setter
    def content_url(self, value):
        self._content_url = value
    @property
    def mark_lable_name(self):
        return self._mark_lable_name

    @mark_lable_name.setter
    def mark_lable_name(self, value):
        self._mark_lable_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_content_type:
            if hasattr(self.biz_content_type, 'to_alipay_dict'):
                params['biz_content_type'] = self.biz_content_type.to_alipay_dict()
            else:
                params['biz_content_type'] = self.biz_content_type
        if self.content_file_type:
            if hasattr(self.content_file_type, 'to_alipay_dict'):
                params['content_file_type'] = self.content_file_type.to_alipay_dict()
            else:
                params['content_file_type'] = self.content_file_type
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.content_risk_info_list:
            if isinstance(self.content_risk_info_list, list):
                for i in range(0, len(self.content_risk_info_list)):
                    element = self.content_risk_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_risk_info_list[i] = element.to_alipay_dict()
            if hasattr(self.content_risk_info_list, 'to_alipay_dict'):
                params['content_risk_info_list'] = self.content_risk_info_list.to_alipay_dict()
            else:
                params['content_risk_info_list'] = self.content_risk_info_list
        if self.content_url:
            if hasattr(self.content_url, 'to_alipay_dict'):
                params['content_url'] = self.content_url.to_alipay_dict()
            else:
                params['content_url'] = self.content_url
        if self.mark_lable_name:
            if hasattr(self.mark_lable_name, 'to_alipay_dict'):
                params['mark_lable_name'] = self.mark_lable_name.to_alipay_dict()
            else:
                params['mark_lable_name'] = self.mark_lable_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LiveContentInfo()
        if 'biz_content_type' in d:
            o.biz_content_type = d['biz_content_type']
        if 'content_file_type' in d:
            o.content_file_type = d['content_file_type']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'content_risk_info_list' in d:
            o.content_risk_info_list = d['content_risk_info_list']
        if 'content_url' in d:
            o.content_url = d['content_url']
        if 'mark_lable_name' in d:
            o.mark_lable_name = d['mark_lable_name']
        return o


