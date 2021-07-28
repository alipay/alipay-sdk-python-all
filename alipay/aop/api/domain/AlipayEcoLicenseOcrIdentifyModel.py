#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoLicenseOcrIdentifyModel(object):

    def __init__(self):
        self._image = None

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value


    def to_alipay_dict(self):
        params = dict()
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoLicenseOcrIdentifyModel()
        if 'image' in d:
            o.image = d['image']
        return o


