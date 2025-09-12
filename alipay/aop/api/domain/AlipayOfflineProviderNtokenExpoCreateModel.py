#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UrlInfoList import UrlInfoList


class AlipayOfflineProviderNtokenExpoCreateModel(object):

    def __init__(self):
        self._head_img = None
        self._logo = None
        self._meeting_timeuuid = None
        self._package_subtitle = None
        self._package_title = None
        self._show_mode = None
        self._url_info_list = None

    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def meeting_timeuuid(self):
        return self._meeting_timeuuid

    @meeting_timeuuid.setter
    def meeting_timeuuid(self, value):
        self._meeting_timeuuid = value
    @property
    def package_subtitle(self):
        return self._package_subtitle

    @package_subtitle.setter
    def package_subtitle(self, value):
        self._package_subtitle = value
    @property
    def package_title(self):
        return self._package_title

    @package_title.setter
    def package_title(self, value):
        self._package_title = value
    @property
    def show_mode(self):
        return self._show_mode

    @show_mode.setter
    def show_mode(self, value):
        self._show_mode = value
    @property
    def url_info_list(self):
        return self._url_info_list

    @url_info_list.setter
    def url_info_list(self, value):
        if isinstance(value, list):
            self._url_info_list = list()
            for i in value:
                if isinstance(i, UrlInfoList):
                    self._url_info_list.append(i)
                else:
                    self._url_info_list.append(UrlInfoList.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.head_img:
            if hasattr(self.head_img, 'to_alipay_dict'):
                params['head_img'] = self.head_img.to_alipay_dict()
            else:
                params['head_img'] = self.head_img
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.meeting_timeuuid:
            if hasattr(self.meeting_timeuuid, 'to_alipay_dict'):
                params['meeting_timeuuid'] = self.meeting_timeuuid.to_alipay_dict()
            else:
                params['meeting_timeuuid'] = self.meeting_timeuuid
        if self.package_subtitle:
            if hasattr(self.package_subtitle, 'to_alipay_dict'):
                params['package_subtitle'] = self.package_subtitle.to_alipay_dict()
            else:
                params['package_subtitle'] = self.package_subtitle
        if self.package_title:
            if hasattr(self.package_title, 'to_alipay_dict'):
                params['package_title'] = self.package_title.to_alipay_dict()
            else:
                params['package_title'] = self.package_title
        if self.show_mode:
            if hasattr(self.show_mode, 'to_alipay_dict'):
                params['show_mode'] = self.show_mode.to_alipay_dict()
            else:
                params['show_mode'] = self.show_mode
        if self.url_info_list:
            if isinstance(self.url_info_list, list):
                for i in range(0, len(self.url_info_list)):
                    element = self.url_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.url_info_list[i] = element.to_alipay_dict()
            if hasattr(self.url_info_list, 'to_alipay_dict'):
                params['url_info_list'] = self.url_info_list.to_alipay_dict()
            else:
                params['url_info_list'] = self.url_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNtokenExpoCreateModel()
        if 'head_img' in d:
            o.head_img = d['head_img']
        if 'logo' in d:
            o.logo = d['logo']
        if 'meeting_timeuuid' in d:
            o.meeting_timeuuid = d['meeting_timeuuid']
        if 'package_subtitle' in d:
            o.package_subtitle = d['package_subtitle']
        if 'package_title' in d:
            o.package_title = d['package_title']
        if 'show_mode' in d:
            o.show_mode = d['show_mode']
        if 'url_info_list' in d:
            o.url_info_list = d['url_info_list']
        return o


