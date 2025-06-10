#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleZmInfo(object):

    def __init__(self):
        self._cancel_back_link = None
        self._enable = None
        self._return_back_link = None

    @property
    def cancel_back_link(self):
        return self._cancel_back_link

    @cancel_back_link.setter
    def cancel_back_link(self, value):
        self._cancel_back_link = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def return_back_link(self):
        return self._return_back_link

    @return_back_link.setter
    def return_back_link(self, value):
        self._return_back_link = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_back_link:
            if hasattr(self.cancel_back_link, 'to_alipay_dict'):
                params['cancel_back_link'] = self.cancel_back_link.to_alipay_dict()
            else:
                params['cancel_back_link'] = self.cancel_back_link
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.return_back_link:
            if hasattr(self.return_back_link, 'to_alipay_dict'):
                params['return_back_link'] = self.return_back_link.to_alipay_dict()
            else:
                params['return_back_link'] = self.return_back_link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleZmInfo()
        if 'cancel_back_link' in d:
            o.cancel_back_link = d['cancel_back_link']
        if 'enable' in d:
            o.enable = d['enable']
        if 'return_back_link' in d:
            o.return_back_link = d['return_back_link']
        return o


