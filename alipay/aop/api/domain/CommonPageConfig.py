#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommonPageConfig(object):

    def __init__(self):
        self._background_image = None
        self._float_diaphaneity = None

    @property
    def background_image(self):
        return self._background_image

    @background_image.setter
    def background_image(self, value):
        self._background_image = value
    @property
    def float_diaphaneity(self):
        return self._float_diaphaneity

    @float_diaphaneity.setter
    def float_diaphaneity(self, value):
        self._float_diaphaneity = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_image:
            if hasattr(self.background_image, 'to_alipay_dict'):
                params['background_image'] = self.background_image.to_alipay_dict()
            else:
                params['background_image'] = self.background_image
        if self.float_diaphaneity:
            if hasattr(self.float_diaphaneity, 'to_alipay_dict'):
                params['float_diaphaneity'] = self.float_diaphaneity.to_alipay_dict()
            else:
                params['float_diaphaneity'] = self.float_diaphaneity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonPageConfig()
        if 'background_image' in d:
            o.background_image = d['background_image']
        if 'float_diaphaneity' in d:
            o.float_diaphaneity = d['float_diaphaneity']
        return o


