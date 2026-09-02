#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Channels(object):

    def __init__(self):
        self._channel = None
        self._short_link = None
        self._template_no = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def short_link(self):
        return self._short_link

    @short_link.setter
    def short_link(self, value):
        self._short_link = value
    @property
    def template_no(self):
        return self._template_no

    @template_no.setter
    def template_no(self, value):
        self._template_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.short_link:
            if hasattr(self.short_link, 'to_alipay_dict'):
                params['short_link'] = self.short_link.to_alipay_dict()
            else:
                params['short_link'] = self.short_link
        if self.template_no:
            if hasattr(self.template_no, 'to_alipay_dict'):
                params['template_no'] = self.template_no.to_alipay_dict()
            else:
                params['template_no'] = self.template_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Channels()
        if 'channel' in d:
            o.channel = d['channel']
        if 'short_link' in d:
            o.short_link = d['short_link']
        if 'template_no' in d:
            o.template_no = d['template_no']
        return o


