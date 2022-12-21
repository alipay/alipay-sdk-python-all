#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommonPrizeVo(object):

    def __init__(self):
        self._prize_desc = None
        self._prize_image_url = None
        self._prize_name = None
        self._prize_num = None

    @property
    def prize_desc(self):
        return self._prize_desc

    @prize_desc.setter
    def prize_desc(self, value):
        self._prize_desc = value
    @property
    def prize_image_url(self):
        return self._prize_image_url

    @prize_image_url.setter
    def prize_image_url(self, value):
        self._prize_image_url = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_num(self):
        return self._prize_num

    @prize_num.setter
    def prize_num(self, value):
        self._prize_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_desc:
            if hasattr(self.prize_desc, 'to_alipay_dict'):
                params['prize_desc'] = self.prize_desc.to_alipay_dict()
            else:
                params['prize_desc'] = self.prize_desc
        if self.prize_image_url:
            if hasattr(self.prize_image_url, 'to_alipay_dict'):
                params['prize_image_url'] = self.prize_image_url.to_alipay_dict()
            else:
                params['prize_image_url'] = self.prize_image_url
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_num:
            if hasattr(self.prize_num, 'to_alipay_dict'):
                params['prize_num'] = self.prize_num.to_alipay_dict()
            else:
                params['prize_num'] = self.prize_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonPrizeVo()
        if 'prize_desc' in d:
            o.prize_desc = d['prize_desc']
        if 'prize_image_url' in d:
            o.prize_image_url = d['prize_image_url']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_num' in d:
            o.prize_num = d['prize_num']
        return o


