#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommonPrizeModelVo(object):

    def __init__(self):
        self._prize_desc_image_url = None
        self._prize_down_desc_text = None
        self._prize_name = None

    @property
    def prize_desc_image_url(self):
        return self._prize_desc_image_url

    @prize_desc_image_url.setter
    def prize_desc_image_url(self, value):
        self._prize_desc_image_url = value
    @property
    def prize_down_desc_text(self):
        return self._prize_down_desc_text

    @prize_down_desc_text.setter
    def prize_down_desc_text(self, value):
        self._prize_down_desc_text = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_desc_image_url:
            if hasattr(self.prize_desc_image_url, 'to_alipay_dict'):
                params['prize_desc_image_url'] = self.prize_desc_image_url.to_alipay_dict()
            else:
                params['prize_desc_image_url'] = self.prize_desc_image_url
        if self.prize_down_desc_text:
            if hasattr(self.prize_down_desc_text, 'to_alipay_dict'):
                params['prize_down_desc_text'] = self.prize_down_desc_text.to_alipay_dict()
            else:
                params['prize_down_desc_text'] = self.prize_down_desc_text
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonPrizeModelVo()
        if 'prize_desc_image_url' in d:
            o.prize_desc_image_url = d['prize_desc_image_url']
        if 'prize_down_desc_text' in d:
            o.prize_down_desc_text = d['prize_down_desc_text']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        return o


