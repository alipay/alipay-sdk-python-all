#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GiftUserTemplateInfo(object):

    def __init__(self):
        self._template_down_url = None
        self._template_thumb_nail = None
        self._template_up_url = None
        self._valid = None
        self._valid_end_time = None
        self._valid_start_time = None

    @property
    def template_down_url(self):
        return self._template_down_url

    @template_down_url.setter
    def template_down_url(self, value):
        self._template_down_url = value
    @property
    def template_thumb_nail(self):
        return self._template_thumb_nail

    @template_thumb_nail.setter
    def template_thumb_nail(self, value):
        self._template_thumb_nail = value
    @property
    def template_up_url(self):
        return self._template_up_url

    @template_up_url.setter
    def template_up_url(self, value):
        self._template_up_url = value
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value
    @property
    def valid_start_time(self):
        return self._valid_start_time

    @valid_start_time.setter
    def valid_start_time(self, value):
        self._valid_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.template_down_url:
            if hasattr(self.template_down_url, 'to_alipay_dict'):
                params['template_down_url'] = self.template_down_url.to_alipay_dict()
            else:
                params['template_down_url'] = self.template_down_url
        if self.template_thumb_nail:
            if hasattr(self.template_thumb_nail, 'to_alipay_dict'):
                params['template_thumb_nail'] = self.template_thumb_nail.to_alipay_dict()
            else:
                params['template_thumb_nail'] = self.template_thumb_nail
        if self.template_up_url:
            if hasattr(self.template_up_url, 'to_alipay_dict'):
                params['template_up_url'] = self.template_up_url.to_alipay_dict()
            else:
                params['template_up_url'] = self.template_up_url
        if self.valid:
            if hasattr(self.valid, 'to_alipay_dict'):
                params['valid'] = self.valid.to_alipay_dict()
            else:
                params['valid'] = self.valid
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        if self.valid_start_time:
            if hasattr(self.valid_start_time, 'to_alipay_dict'):
                params['valid_start_time'] = self.valid_start_time.to_alipay_dict()
            else:
                params['valid_start_time'] = self.valid_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftUserTemplateInfo()
        if 'template_down_url' in d:
            o.template_down_url = d['template_down_url']
        if 'template_thumb_nail' in d:
            o.template_thumb_nail = d['template_thumb_nail']
        if 'template_up_url' in d:
            o.template_up_url = d['template_up_url']
        if 'valid' in d:
            o.valid = d['valid']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        if 'valid_start_time' in d:
            o.valid_start_time = d['valid_start_time']
        return o


