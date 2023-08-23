#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertContentShareCodeModify(object):

    def __init__(self):
        self._display_title = None

    @property
    def display_title(self):
        return self._display_title

    @display_title.setter
    def display_title(self, value):
        self._display_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_title:
            if hasattr(self.display_title, 'to_alipay_dict'):
                params['display_title'] = self.display_title.to_alipay_dict()
            else:
                params['display_title'] = self.display_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertContentShareCodeModify()
        if 'display_title' in d:
            o.display_title = d['display_title']
        return o


