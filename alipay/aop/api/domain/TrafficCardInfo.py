#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrafficCardInfo(object):

    def __init__(self):
        self._card_title = None
        self._card_use_url = None
        self._image_url = None
        self._logo_url = None

    @property
    def card_title(self):
        return self._card_title

    @card_title.setter
    def card_title(self, value):
        self._card_title = value
    @property
    def card_use_url(self):
        return self._card_use_url

    @card_use_url.setter
    def card_use_url(self, value):
        self._card_use_url = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_title:
            if hasattr(self.card_title, 'to_alipay_dict'):
                params['card_title'] = self.card_title.to_alipay_dict()
            else:
                params['card_title'] = self.card_title
        if self.card_use_url:
            if hasattr(self.card_use_url, 'to_alipay_dict'):
                params['card_use_url'] = self.card_use_url.to_alipay_dict()
            else:
                params['card_use_url'] = self.card_use_url
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficCardInfo()
        if 'card_title' in d:
            o.card_title = d['card_title']
        if 'card_use_url' in d:
            o.card_use_url = d['card_use_url']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        return o


