#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySecurityKnowledgeCheckModel(object):

    def __init__(self):
        self._biz_id = None
        self._link_list = None
        self._pic_url_list = None
        self._text_list = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def link_list(self):
        return self._link_list

    @link_list.setter
    def link_list(self, value):
        if isinstance(value, list):
            self._link_list = list()
            for i in value:
                self._link_list.append(i)
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
    def text_list(self):
        return self._text_list

    @text_list.setter
    def text_list(self, value):
        if isinstance(value, list):
            self._text_list = list()
            for i in value:
                self._text_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.link_list:
            if isinstance(self.link_list, list):
                for i in range(0, len(self.link_list)):
                    element = self.link_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.link_list[i] = element.to_alipay_dict()
            if hasattr(self.link_list, 'to_alipay_dict'):
                params['link_list'] = self.link_list.to_alipay_dict()
            else:
                params['link_list'] = self.link_list
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
        if self.text_list:
            if isinstance(self.text_list, list):
                for i in range(0, len(self.text_list)):
                    element = self.text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.text_list[i] = element.to_alipay_dict()
            if hasattr(self.text_list, 'to_alipay_dict'):
                params['text_list'] = self.text_list.to_alipay_dict()
            else:
                params['text_list'] = self.text_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySecurityKnowledgeCheckModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'link_list' in d:
            o.link_list = d['link_list']
        if 'pic_url_list' in d:
            o.pic_url_list = d['pic_url_list']
        if 'text_list' in d:
            o.text_list = d['text_list']
        return o


