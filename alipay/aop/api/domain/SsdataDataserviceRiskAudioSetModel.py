#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskAudioSetModel(object):

    def __init__(self):
        self._creator = None
        self._id_list = None
        self._keyword_list = None
        self._modifier = None
        self._operate_type = None
        self._page_num = None
        self._page_size = None
        self._risk_type = None

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def id_list(self):
        return self._id_list

    @id_list.setter
    def id_list(self, value):
        if isinstance(value, list):
            self._id_list = list()
            for i in value:
                self._id_list.append(i)
    @property
    def keyword_list(self):
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, value):
        if isinstance(value, list):
            self._keyword_list = list()
            for i in value:
                self._keyword_list.append(i)
    @property
    def modifier(self):
        return self._modifier

    @modifier.setter
    def modifier(self, value):
        self._modifier = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.id_list:
            if isinstance(self.id_list, list):
                for i in range(0, len(self.id_list)):
                    element = self.id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.id_list[i] = element.to_alipay_dict()
            if hasattr(self.id_list, 'to_alipay_dict'):
                params['id_list'] = self.id_list.to_alipay_dict()
            else:
                params['id_list'] = self.id_list
        if self.keyword_list:
            if isinstance(self.keyword_list, list):
                for i in range(0, len(self.keyword_list)):
                    element = self.keyword_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keyword_list[i] = element.to_alipay_dict()
            if hasattr(self.keyword_list, 'to_alipay_dict'):
                params['keyword_list'] = self.keyword_list.to_alipay_dict()
            else:
                params['keyword_list'] = self.keyword_list
        if self.modifier:
            if hasattr(self.modifier, 'to_alipay_dict'):
                params['modifier'] = self.modifier.to_alipay_dict()
            else:
                params['modifier'] = self.modifier
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskAudioSetModel()
        if 'creator' in d:
            o.creator = d['creator']
        if 'id_list' in d:
            o.id_list = d['id_list']
        if 'keyword_list' in d:
            o.keyword_list = d['keyword_list']
        if 'modifier' in d:
            o.modifier = d['modifier']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        return o


