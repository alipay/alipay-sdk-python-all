#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreativeRefuseExtendInfo(object):

    def __init__(self):
        self._image_url_list = None

    @property
    def image_url_list(self):
        return self._image_url_list

    @image_url_list.setter
    def image_url_list(self, value):
        if isinstance(value, list):
            self._image_url_list = list()
            for i in value:
                self._image_url_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.image_url_list:
            if isinstance(self.image_url_list, list):
                for i in range(0, len(self.image_url_list)):
                    element = self.image_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_url_list[i] = element.to_alipay_dict()
            if hasattr(self.image_url_list, 'to_alipay_dict'):
                params['image_url_list'] = self.image_url_list.to_alipay_dict()
            else:
                params['image_url_list'] = self.image_url_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeRefuseExtendInfo()
        if 'image_url_list' in d:
            o.image_url_list = d['image_url_list']
        return o


