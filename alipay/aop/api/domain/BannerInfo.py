#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BannerInfo(object):

    def __init__(self):
        self._click_url = None
        self._end_time = None
        self._img_url = None
        self._start_time = None

    @property
    def click_url(self):
        return self._click_url

    @click_url.setter
    def click_url(self, value):
        self._click_url = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.click_url:
            if hasattr(self.click_url, 'to_alipay_dict'):
                params['click_url'] = self.click_url.to_alipay_dict()
            else:
                params['click_url'] = self.click_url
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BannerInfo()
        if 'click_url' in d:
            o.click_url = d['click_url']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


