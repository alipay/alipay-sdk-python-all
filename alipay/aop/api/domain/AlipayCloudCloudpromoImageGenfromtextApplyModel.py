#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoImageGenfromtextApplyModel(object):

    def __init__(self):
        self._height = None
        self._image_num = None
        self._industry = None
        self._negative_prompt = None
        self._out_biz_id = None
        self._prompt = None
        self._width = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def image_num(self):
        return self._image_num

    @image_num.setter
    def image_num(self, value):
        self._image_num = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def negative_prompt(self):
        return self._negative_prompt

    @negative_prompt.setter
    def negative_prompt(self, value):
        self._negative_prompt = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def prompt(self):
        return self._prompt

    @prompt.setter
    def prompt(self, value):
        self._prompt = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.image_num:
            if hasattr(self.image_num, 'to_alipay_dict'):
                params['image_num'] = self.image_num.to_alipay_dict()
            else:
                params['image_num'] = self.image_num
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.negative_prompt:
            if hasattr(self.negative_prompt, 'to_alipay_dict'):
                params['negative_prompt'] = self.negative_prompt.to_alipay_dict()
            else:
                params['negative_prompt'] = self.negative_prompt
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.prompt:
            if hasattr(self.prompt, 'to_alipay_dict'):
                params['prompt'] = self.prompt.to_alipay_dict()
            else:
                params['prompt'] = self.prompt
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoImageGenfromtextApplyModel()
        if 'height' in d:
            o.height = d['height']
        if 'image_num' in d:
            o.image_num = d['image_num']
        if 'industry' in d:
            o.industry = d['industry']
        if 'negative_prompt' in d:
            o.negative_prompt = d['negative_prompt']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'prompt' in d:
            o.prompt = d['prompt']
        if 'width' in d:
            o.width = d['width']
        return o


