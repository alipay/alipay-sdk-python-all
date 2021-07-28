#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo


class JourneyServiceChangeInfo(object):

    def __init__(self):
        self._change_status = None
        self._detail_url = None
        self._ext_info = None
        self._remind_content = None

    @property
    def change_status(self):
        return self._change_status

    @change_status.setter
    def change_status(self, value):
        self._change_status = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def remind_content(self):
        return self._remind_content

    @remind_content.setter
    def remind_content(self, value):
        self._remind_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_status:
            if hasattr(self.change_status, 'to_alipay_dict'):
                params['change_status'] = self.change_status.to_alipay_dict()
            else:
                params['change_status'] = self.change_status
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.remind_content:
            if hasattr(self.remind_content, 'to_alipay_dict'):
                params['remind_content'] = self.remind_content.to_alipay_dict()
            else:
                params['remind_content'] = self.remind_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JourneyServiceChangeInfo()
        if 'change_status' in d:
            o.change_status = d['change_status']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'remind_content' in d:
            o.remind_content = d['remind_content']
        return o


