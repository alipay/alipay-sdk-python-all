#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppletTaskDisplayVO(object):

    def __init__(self):
        self._button_text = None
        self._button_text_disabled = None
        self._link = None
        self._promo_link = None
        self._tag_icon = None
        self._tag_suffix = None
        self._task_desc = None
        self._task_icon = None
        self._task_title = None

    @property
    def button_text(self):
        return self._button_text

    @button_text.setter
    def button_text(self, value):
        self._button_text = value
    @property
    def button_text_disabled(self):
        return self._button_text_disabled

    @button_text_disabled.setter
    def button_text_disabled(self, value):
        self._button_text_disabled = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def promo_link(self):
        return self._promo_link

    @promo_link.setter
    def promo_link(self, value):
        self._promo_link = value
    @property
    def tag_icon(self):
        return self._tag_icon

    @tag_icon.setter
    def tag_icon(self, value):
        self._tag_icon = value
    @property
    def tag_suffix(self):
        return self._tag_suffix

    @tag_suffix.setter
    def tag_suffix(self, value):
        self._tag_suffix = value
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_icon(self):
        return self._task_icon

    @task_icon.setter
    def task_icon(self, value):
        self._task_icon = value
    @property
    def task_title(self):
        return self._task_title

    @task_title.setter
    def task_title(self, value):
        self._task_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.button_text:
            if hasattr(self.button_text, 'to_alipay_dict'):
                params['button_text'] = self.button_text.to_alipay_dict()
            else:
                params['button_text'] = self.button_text
        if self.button_text_disabled:
            if hasattr(self.button_text_disabled, 'to_alipay_dict'):
                params['button_text_disabled'] = self.button_text_disabled.to_alipay_dict()
            else:
                params['button_text_disabled'] = self.button_text_disabled
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.promo_link:
            if hasattr(self.promo_link, 'to_alipay_dict'):
                params['promo_link'] = self.promo_link.to_alipay_dict()
            else:
                params['promo_link'] = self.promo_link
        if self.tag_icon:
            if hasattr(self.tag_icon, 'to_alipay_dict'):
                params['tag_icon'] = self.tag_icon.to_alipay_dict()
            else:
                params['tag_icon'] = self.tag_icon
        if self.tag_suffix:
            if hasattr(self.tag_suffix, 'to_alipay_dict'):
                params['tag_suffix'] = self.tag_suffix.to_alipay_dict()
            else:
                params['tag_suffix'] = self.tag_suffix
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_icon:
            if hasattr(self.task_icon, 'to_alipay_dict'):
                params['task_icon'] = self.task_icon.to_alipay_dict()
            else:
                params['task_icon'] = self.task_icon
        if self.task_title:
            if hasattr(self.task_title, 'to_alipay_dict'):
                params['task_title'] = self.task_title.to_alipay_dict()
            else:
                params['task_title'] = self.task_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppletTaskDisplayVO()
        if 'button_text' in d:
            o.button_text = d['button_text']
        if 'button_text_disabled' in d:
            o.button_text_disabled = d['button_text_disabled']
        if 'link' in d:
            o.link = d['link']
        if 'promo_link' in d:
            o.promo_link = d['promo_link']
        if 'tag_icon' in d:
            o.tag_icon = d['tag_icon']
        if 'tag_suffix' in d:
            o.tag_suffix = d['tag_suffix']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_icon' in d:
            o.task_icon = d['task_icon']
        if 'task_title' in d:
            o.task_title = d['task_title']
        return o


