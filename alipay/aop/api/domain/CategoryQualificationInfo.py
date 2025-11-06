#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupPurchaseImageInfo import GroupPurchaseImageInfo


class CategoryQualificationInfo(object):

    def __init__(self):
        self._images = None
        self._qual_code = None

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                if isinstance(i, GroupPurchaseImageInfo):
                    self._images.append(i)
                else:
                    self._images.append(GroupPurchaseImageInfo.from_alipay_dict(i))
    @property
    def qual_code(self):
        return self._qual_code

    @qual_code.setter
    def qual_code(self, value):
        self._qual_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.images:
            if isinstance(self.images, list):
                for i in range(0, len(self.images)):
                    element = self.images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images[i] = element.to_alipay_dict()
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        if self.qual_code:
            if hasattr(self.qual_code, 'to_alipay_dict'):
                params['qual_code'] = self.qual_code.to_alipay_dict()
            else:
                params['qual_code'] = self.qual_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryQualificationInfo()
        if 'images' in d:
            o.images = d['images']
        if 'qual_code' in d:
            o.qual_code = d['qual_code']
        return o


