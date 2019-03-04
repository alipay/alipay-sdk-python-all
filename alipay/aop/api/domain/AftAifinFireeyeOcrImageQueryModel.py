#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AftAifinFireeyeOcrImageQueryModel(object):

    def __init__(self):
        self._image = None
        self._ocr_type = None
        self._product_instance_id = None

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def ocr_type(self):
        return self._ocr_type

    @ocr_type.setter
    def ocr_type(self, value):
        self._ocr_type = value
    @property
    def product_instance_id(self):
        return self._product_instance_id

    @product_instance_id.setter
    def product_instance_id(self, value):
        self._product_instance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.ocr_type:
            if hasattr(self.ocr_type, 'to_alipay_dict'):
                params['ocr_type'] = self.ocr_type.to_alipay_dict()
            else:
                params['ocr_type'] = self.ocr_type
        if self.product_instance_id:
            if hasattr(self.product_instance_id, 'to_alipay_dict'):
                params['product_instance_id'] = self.product_instance_id.to_alipay_dict()
            else:
                params['product_instance_id'] = self.product_instance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftAifinFireeyeOcrImageQueryModel()
        if 'image' in d:
            o.image = d['image']
        if 'ocr_type' in d:
            o.ocr_type = d['ocr_type']
        if 'product_instance_id' in d:
            o.product_instance_id = d['product_instance_id']
        return o


