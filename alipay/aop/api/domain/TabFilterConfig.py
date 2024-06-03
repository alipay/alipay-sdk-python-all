#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Banner import Banner
from alipay.aop.api.domain.DataCount import DataCount
from alipay.aop.api.domain.SubTabFilterConfig import SubTabFilterConfig
from alipay.aop.api.domain.SubTabFilterConfig import SubTabFilterConfig
from alipay.aop.api.domain.TabFilterTag import TabFilterTag


class TabFilterConfig(object):

    def __init__(self):
        self._background_img = None
        self._banner = None
        self._data_count = None
        self._min_version_code = None
        self._rank_data_type = None
        self._sub_tab_list = None
        self._sub_tab_list_v2 = None
        self._tag = None
        self._title = None

    @property
    def background_img(self):
        return self._background_img

    @background_img.setter
    def background_img(self, value):
        self._background_img = value
    @property
    def banner(self):
        return self._banner

    @banner.setter
    def banner(self, value):
        if isinstance(value, Banner):
            self._banner = value
        else:
            self._banner = Banner.from_alipay_dict(value)
    @property
    def data_count(self):
        return self._data_count

    @data_count.setter
    def data_count(self, value):
        if isinstance(value, DataCount):
            self._data_count = value
        else:
            self._data_count = DataCount.from_alipay_dict(value)
    @property
    def min_version_code(self):
        return self._min_version_code

    @min_version_code.setter
    def min_version_code(self, value):
        self._min_version_code = value
    @property
    def rank_data_type(self):
        return self._rank_data_type

    @rank_data_type.setter
    def rank_data_type(self, value):
        self._rank_data_type = value
    @property
    def sub_tab_list(self):
        return self._sub_tab_list

    @sub_tab_list.setter
    def sub_tab_list(self, value):
        if isinstance(value, list):
            self._sub_tab_list = list()
            for i in value:
                if isinstance(i, SubTabFilterConfig):
                    self._sub_tab_list.append(i)
                else:
                    self._sub_tab_list.append(SubTabFilterConfig.from_alipay_dict(i))
    @property
    def sub_tab_list_v2(self):
        return self._sub_tab_list_v2

    @sub_tab_list_v2.setter
    def sub_tab_list_v2(self, value):
        if isinstance(value, list):
            self._sub_tab_list_v2 = list()
            for i in value:
                if isinstance(i, SubTabFilterConfig):
                    self._sub_tab_list_v2.append(i)
                else:
                    self._sub_tab_list_v2.append(SubTabFilterConfig.from_alipay_dict(i))
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        if isinstance(value, TabFilterTag):
            self._tag = value
        else:
            self._tag = TabFilterTag.from_alipay_dict(value)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_img:
            if hasattr(self.background_img, 'to_alipay_dict'):
                params['background_img'] = self.background_img.to_alipay_dict()
            else:
                params['background_img'] = self.background_img
        if self.banner:
            if hasattr(self.banner, 'to_alipay_dict'):
                params['banner'] = self.banner.to_alipay_dict()
            else:
                params['banner'] = self.banner
        if self.data_count:
            if hasattr(self.data_count, 'to_alipay_dict'):
                params['data_count'] = self.data_count.to_alipay_dict()
            else:
                params['data_count'] = self.data_count
        if self.min_version_code:
            if hasattr(self.min_version_code, 'to_alipay_dict'):
                params['min_version_code'] = self.min_version_code.to_alipay_dict()
            else:
                params['min_version_code'] = self.min_version_code
        if self.rank_data_type:
            if hasattr(self.rank_data_type, 'to_alipay_dict'):
                params['rank_data_type'] = self.rank_data_type.to_alipay_dict()
            else:
                params['rank_data_type'] = self.rank_data_type
        if self.sub_tab_list:
            if isinstance(self.sub_tab_list, list):
                for i in range(0, len(self.sub_tab_list)):
                    element = self.sub_tab_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_tab_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_tab_list, 'to_alipay_dict'):
                params['sub_tab_list'] = self.sub_tab_list.to_alipay_dict()
            else:
                params['sub_tab_list'] = self.sub_tab_list
        if self.sub_tab_list_v2:
            if isinstance(self.sub_tab_list_v2, list):
                for i in range(0, len(self.sub_tab_list_v2)):
                    element = self.sub_tab_list_v2[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_tab_list_v2[i] = element.to_alipay_dict()
            if hasattr(self.sub_tab_list_v2, 'to_alipay_dict'):
                params['sub_tab_list_v2'] = self.sub_tab_list_v2.to_alipay_dict()
            else:
                params['sub_tab_list_v2'] = self.sub_tab_list_v2
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
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
        o = TabFilterConfig()
        if 'background_img' in d:
            o.background_img = d['background_img']
        if 'banner' in d:
            o.banner = d['banner']
        if 'data_count' in d:
            o.data_count = d['data_count']
        if 'min_version_code' in d:
            o.min_version_code = d['min_version_code']
        if 'rank_data_type' in d:
            o.rank_data_type = d['rank_data_type']
        if 'sub_tab_list' in d:
            o.sub_tab_list = d['sub_tab_list']
        if 'sub_tab_list_v2' in d:
            o.sub_tab_list_v2 = d['sub_tab_list_v2']
        if 'tag' in d:
            o.tag = d['tag']
        if 'title' in d:
            o.title = d['title']
        return o


