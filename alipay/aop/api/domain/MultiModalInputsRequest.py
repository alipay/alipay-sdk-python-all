#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MultiModalInputsRequest(object):

    def __init__(self):
        self._images = None

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)


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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiModalInputsRequest()
        if 'images' in d:
            o.images = d['images']
        return o


