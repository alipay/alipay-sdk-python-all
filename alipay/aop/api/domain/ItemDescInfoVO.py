#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemDescInfoVO(object):

    def __init__(self):
        self._desc = None
        self._imgs = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def imgs(self):
        return self._imgs

    @imgs.setter
    def imgs(self, value):
        if isinstance(value, list):
            self._imgs = list()
            for i in value:
                self._imgs.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.imgs:
            if isinstance(self.imgs, list):
                for i in range(0, len(self.imgs)):
                    element = self.imgs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.imgs[i] = element.to_alipay_dict()
            if hasattr(self.imgs, 'to_alipay_dict'):
                params['imgs'] = self.imgs.to_alipay_dict()
            else:
                params['imgs'] = self.imgs
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemDescInfoVO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'imgs' in d:
            o.imgs = d['imgs']
        return o


