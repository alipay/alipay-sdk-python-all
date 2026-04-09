#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelThemeVO(object):

    def __init__(self):
        self._hotelmind_bg = None
        self._hotelmind_btn_text = None
        self._hotelmind_title = None
        self._person_logo = None

    @property
    def hotelmind_bg(self):
        return self._hotelmind_bg

    @hotelmind_bg.setter
    def hotelmind_bg(self, value):
        self._hotelmind_bg = value
    @property
    def hotelmind_btn_text(self):
        return self._hotelmind_btn_text

    @hotelmind_btn_text.setter
    def hotelmind_btn_text(self, value):
        self._hotelmind_btn_text = value
    @property
    def hotelmind_title(self):
        return self._hotelmind_title

    @hotelmind_title.setter
    def hotelmind_title(self, value):
        self._hotelmind_title = value
    @property
    def person_logo(self):
        return self._person_logo

    @person_logo.setter
    def person_logo(self, value):
        self._person_logo = value


    def to_alipay_dict(self):
        params = dict()
        if self.hotelmind_bg:
            if hasattr(self.hotelmind_bg, 'to_alipay_dict'):
                params['hotelmind_bg'] = self.hotelmind_bg.to_alipay_dict()
            else:
                params['hotelmind_bg'] = self.hotelmind_bg
        if self.hotelmind_btn_text:
            if hasattr(self.hotelmind_btn_text, 'to_alipay_dict'):
                params['hotelmind_btn_text'] = self.hotelmind_btn_text.to_alipay_dict()
            else:
                params['hotelmind_btn_text'] = self.hotelmind_btn_text
        if self.hotelmind_title:
            if hasattr(self.hotelmind_title, 'to_alipay_dict'):
                params['hotelmind_title'] = self.hotelmind_title.to_alipay_dict()
            else:
                params['hotelmind_title'] = self.hotelmind_title
        if self.person_logo:
            if hasattr(self.person_logo, 'to_alipay_dict'):
                params['person_logo'] = self.person_logo.to_alipay_dict()
            else:
                params['person_logo'] = self.person_logo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelThemeVO()
        if 'hotelmind_bg' in d:
            o.hotelmind_bg = d['hotelmind_bg']
        if 'hotelmind_btn_text' in d:
            o.hotelmind_btn_text = d['hotelmind_btn_text']
        if 'hotelmind_title' in d:
            o.hotelmind_title = d['hotelmind_title']
        if 'person_logo' in d:
            o.person_logo = d['person_logo']
        return o


