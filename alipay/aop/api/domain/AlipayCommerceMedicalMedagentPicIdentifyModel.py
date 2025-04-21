#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedagentPicIdentifyModel(object):

    def __init__(self):
        self._image_url = None
        self._target_list = None

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def target_list(self):
        return self._target_list

    @target_list.setter
    def target_list(self, value):
        if isinstance(value, list):
            self._target_list = list()
            for i in value:
                self._target_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.target_list:
            if isinstance(self.target_list, list):
                for i in range(0, len(self.target_list)):
                    element = self.target_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_list[i] = element.to_alipay_dict()
            if hasattr(self.target_list, 'to_alipay_dict'):
                params['target_list'] = self.target_list.to_alipay_dict()
            else:
                params['target_list'] = self.target_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedagentPicIdentifyModel()
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'target_list' in d:
            o.target_list = d['target_list']
        return o


