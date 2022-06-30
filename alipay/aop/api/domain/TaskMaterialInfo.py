#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskMaterialInfo(object):

    def __init__(self):
        self._button_text_award = None
        self._button_text_done = None
        self._button_text_signup = None
        self._icon = None
        self._link = None
        self._sub_title = None
        self._title = None

    @property
    def button_text_award(self):
        return self._button_text_award

    @button_text_award.setter
    def button_text_award(self, value):
        self._button_text_award = value
    @property
    def button_text_done(self):
        return self._button_text_done

    @button_text_done.setter
    def button_text_done(self, value):
        self._button_text_done = value
    @property
    def button_text_signup(self):
        return self._button_text_signup

    @button_text_signup.setter
    def button_text_signup(self, value):
        self._button_text_signup = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.button_text_award:
            if hasattr(self.button_text_award, 'to_alipay_dict'):
                params['button_text_award'] = self.button_text_award.to_alipay_dict()
            else:
                params['button_text_award'] = self.button_text_award
        if self.button_text_done:
            if hasattr(self.button_text_done, 'to_alipay_dict'):
                params['button_text_done'] = self.button_text_done.to_alipay_dict()
            else:
                params['button_text_done'] = self.button_text_done
        if self.button_text_signup:
            if hasattr(self.button_text_signup, 'to_alipay_dict'):
                params['button_text_signup'] = self.button_text_signup.to_alipay_dict()
            else:
                params['button_text_signup'] = self.button_text_signup
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskMaterialInfo()
        if 'button_text_award' in d:
            o.button_text_award = d['button_text_award']
        if 'button_text_done' in d:
            o.button_text_done = d['button_text_done']
        if 'button_text_signup' in d:
            o.button_text_signup = d['button_text_signup']
        if 'icon' in d:
            o.icon = d['icon']
        if 'link' in d:
            o.link = d['link']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        return o


