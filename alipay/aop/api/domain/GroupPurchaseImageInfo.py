#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupPurchaseImageInfo(object):

    def __init__(self):
        self._image_pic = None

    @property
    def image_pic(self):
        return self._image_pic

    @image_pic.setter
    def image_pic(self, value):
        self._image_pic = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_pic:
            if hasattr(self.image_pic, 'to_alipay_dict'):
                params['image_pic'] = self.image_pic.to_alipay_dict()
            else:
                params['image_pic'] = self.image_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupPurchaseImageInfo()
        if 'image_pic' in d:
            o.image_pic = d['image_pic']
        return o


