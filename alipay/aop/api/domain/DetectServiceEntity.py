#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DetectServiceEntity(object):

    def __init__(self):
        self._biz_uniq_id = None
        self._content = None
        self._detect_type_list = None
        self._extend_info = None
        self._pic_url_list = None
        self._service = None
        self._title = None

    @property
    def biz_uniq_id(self):
        return self._biz_uniq_id

    @biz_uniq_id.setter
    def biz_uniq_id(self, value):
        self._biz_uniq_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def detect_type_list(self):
        return self._detect_type_list

    @detect_type_list.setter
    def detect_type_list(self, value):
        if isinstance(value, list):
            self._detect_type_list = list()
            for i in value:
                self._detect_type_list.append(i)
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def pic_url_list(self):
        return self._pic_url_list

    @pic_url_list.setter
    def pic_url_list(self, value):
        if isinstance(value, list):
            self._pic_url_list = list()
            for i in value:
                self._pic_url_list.append(i)
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_uniq_id:
            if hasattr(self.biz_uniq_id, 'to_alipay_dict'):
                params['biz_uniq_id'] = self.biz_uniq_id.to_alipay_dict()
            else:
                params['biz_uniq_id'] = self.biz_uniq_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.detect_type_list:
            if isinstance(self.detect_type_list, list):
                for i in range(0, len(self.detect_type_list)):
                    element = self.detect_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detect_type_list[i] = element.to_alipay_dict()
            if hasattr(self.detect_type_list, 'to_alipay_dict'):
                params['detect_type_list'] = self.detect_type_list.to_alipay_dict()
            else:
                params['detect_type_list'] = self.detect_type_list
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.pic_url_list:
            if isinstance(self.pic_url_list, list):
                for i in range(0, len(self.pic_url_list)):
                    element = self.pic_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pic_url_list[i] = element.to_alipay_dict()
            if hasattr(self.pic_url_list, 'to_alipay_dict'):
                params['pic_url_list'] = self.pic_url_list.to_alipay_dict()
            else:
                params['pic_url_list'] = self.pic_url_list
        if self.service:
            if hasattr(self.service, 'to_alipay_dict'):
                params['service'] = self.service.to_alipay_dict()
            else:
                params['service'] = self.service
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DetectServiceEntity()
        if 'biz_uniq_id' in d:
            o.biz_uniq_id = d['biz_uniq_id']
        if 'content' in d:
            o.content = d['content']
        if 'detect_type_list' in d:
            o.detect_type_list = d['detect_type_list']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'pic_url_list' in d:
            o.pic_url_list = d['pic_url_list']
        if 'service' in d:
            o.service = d['service']
        if 'title' in d:
            o.title = d['title']
        return o


