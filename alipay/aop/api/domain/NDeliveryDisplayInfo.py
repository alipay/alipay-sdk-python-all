#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NDeliveryDisplayInfo(object):

    def __init__(self):
        self._card_visual_style = None
        self._main_title = None
        self._sub_title = None

    @property
    def card_visual_style(self):
        return self._card_visual_style

    @card_visual_style.setter
    def card_visual_style(self, value):
        self._card_visual_style = value
    @property
    def main_title(self):
        return self._main_title

    @main_title.setter
    def main_title(self, value):
        self._main_title = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_visual_style:
            if hasattr(self.card_visual_style, 'to_alipay_dict'):
                params['card_visual_style'] = self.card_visual_style.to_alipay_dict()
            else:
                params['card_visual_style'] = self.card_visual_style
        if self.main_title:
            if hasattr(self.main_title, 'to_alipay_dict'):
                params['main_title'] = self.main_title.to_alipay_dict()
            else:
                params['main_title'] = self.main_title
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NDeliveryDisplayInfo()
        if 'card_visual_style' in d:
            o.card_visual_style = d['card_visual_style']
        if 'main_title' in d:
            o.main_title = d['main_title']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        return o


