#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PortraitDataVO import PortraitDataVO
from alipay.aop.api.domain.TgiTagVO import TgiTagVO


class PortraitsDataTgiVO(object):

    def __init__(self):
        self._portraits = None
        self._top_tgi_tags = None

    @property
    def portraits(self):
        return self._portraits

    @portraits.setter
    def portraits(self, value):
        if isinstance(value, list):
            self._portraits = list()
            for i in value:
                if isinstance(i, PortraitDataVO):
                    self._portraits.append(i)
                else:
                    self._portraits.append(PortraitDataVO.from_alipay_dict(i))
    @property
    def top_tgi_tags(self):
        return self._top_tgi_tags

    @top_tgi_tags.setter
    def top_tgi_tags(self, value):
        if isinstance(value, TgiTagVO):
            self._top_tgi_tags = value
        else:
            self._top_tgi_tags = TgiTagVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.portraits:
            if isinstance(self.portraits, list):
                for i in range(0, len(self.portraits)):
                    element = self.portraits[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.portraits[i] = element.to_alipay_dict()
            if hasattr(self.portraits, 'to_alipay_dict'):
                params['portraits'] = self.portraits.to_alipay_dict()
            else:
                params['portraits'] = self.portraits
        if self.top_tgi_tags:
            if hasattr(self.top_tgi_tags, 'to_alipay_dict'):
                params['top_tgi_tags'] = self.top_tgi_tags.to_alipay_dict()
            else:
                params['top_tgi_tags'] = self.top_tgi_tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortraitsDataTgiVO()
        if 'portraits' in d:
            o.portraits = d['portraits']
        if 'top_tgi_tags' in d:
            o.top_tgi_tags = d['top_tgi_tags']
        return o


