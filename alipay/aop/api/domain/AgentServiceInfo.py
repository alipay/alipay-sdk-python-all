#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceExtInfoMap import ServiceExtInfoMap


class AgentServiceInfo(object):

    def __init__(self):
        self._ext_infos = None
        self._link_url = None
        self._logo = None
        self._priority = None
        self._scm_info = None
        self._sub_title = None
        self._title = None

    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        if isinstance(value, ServiceExtInfoMap):
            self._ext_infos = value
        else:
            self._ext_infos = ServiceExtInfoMap.from_alipay_dict(value)
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def scm_info(self):
        return self._scm_info

    @scm_info.setter
    def scm_info(self, value):
        self._scm_info = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.scm_info:
            if hasattr(self.scm_info, 'to_alipay_dict'):
                params['scm_info'] = self.scm_info.to_alipay_dict()
            else:
                params['scm_info'] = self.scm_info
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
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
        o = AgentServiceInfo()
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'logo' in d:
            o.logo = d['logo']
        if 'priority' in d:
            o.priority = d['priority']
        if 'scm_info' in d:
            o.scm_info = d['scm_info']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        return o


