#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TimeCardItemExtendInfo(object):

    def __init__(self):
        self._action_link = None

    @property
    def action_link(self):
        return self._action_link

    @action_link.setter
    def action_link(self, value):
        self._action_link = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_link:
            if hasattr(self.action_link, 'to_alipay_dict'):
                params['action_link'] = self.action_link.to_alipay_dict()
            else:
                params['action_link'] = self.action_link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TimeCardItemExtendInfo()
        if 'action_link' in d:
            o.action_link = d['action_link']
        return o


