#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WorldErrorIndicator(object):

    def __init__(self):
        self._action_button = None
        self._action_url = None
        self._alipay_inside_tips = None
        self._clean_card = None
        self._default_button = None
        self._default_url = None
        self._desc = None
        self._error_code = None
        self._tips = None
        self._type = None

    @property
    def action_button(self):
        return self._action_button

    @action_button.setter
    def action_button(self, value):
        self._action_button = value
    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def alipay_inside_tips(self):
        return self._alipay_inside_tips

    @alipay_inside_tips.setter
    def alipay_inside_tips(self, value):
        self._alipay_inside_tips = value
    @property
    def clean_card(self):
        return self._clean_card

    @clean_card.setter
    def clean_card(self, value):
        self._clean_card = value
    @property
    def default_button(self):
        return self._default_button

    @default_button.setter
    def default_button(self, value):
        self._default_button = value
    @property
    def default_url(self):
        return self._default_url

    @default_url.setter
    def default_url(self, value):
        self._default_url = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_button:
            if hasattr(self.action_button, 'to_alipay_dict'):
                params['action_button'] = self.action_button.to_alipay_dict()
            else:
                params['action_button'] = self.action_button
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.alipay_inside_tips:
            if hasattr(self.alipay_inside_tips, 'to_alipay_dict'):
                params['alipay_inside_tips'] = self.alipay_inside_tips.to_alipay_dict()
            else:
                params['alipay_inside_tips'] = self.alipay_inside_tips
        if self.clean_card:
            if hasattr(self.clean_card, 'to_alipay_dict'):
                params['clean_card'] = self.clean_card.to_alipay_dict()
            else:
                params['clean_card'] = self.clean_card
        if self.default_button:
            if hasattr(self.default_button, 'to_alipay_dict'):
                params['default_button'] = self.default_button.to_alipay_dict()
            else:
                params['default_button'] = self.default_button
        if self.default_url:
            if hasattr(self.default_url, 'to_alipay_dict'):
                params['default_url'] = self.default_url.to_alipay_dict()
            else:
                params['default_url'] = self.default_url
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.tips:
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorldErrorIndicator()
        if 'action_button' in d:
            o.action_button = d['action_button']
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'alipay_inside_tips' in d:
            o.alipay_inside_tips = d['alipay_inside_tips']
        if 'clean_card' in d:
            o.clean_card = d['clean_card']
        if 'default_button' in d:
            o.default_button = d['default_button']
        if 'default_url' in d:
            o.default_url = d['default_url']
        if 'desc' in d:
            o.desc = d['desc']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'tips' in d:
            o.tips = d['tips']
        if 'type' in d:
            o.type = d['type']
        return o


