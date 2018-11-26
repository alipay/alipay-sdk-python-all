#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DefaultInCartInfo(object):

    def __init__(self):
        self._default_num = None
        self._link_guest = None
        self._per_num = None

    @property
    def default_num(self):
        return self._default_num

    @default_num.setter
    def default_num(self, value):
        self._default_num = value
    @property
    def link_guest(self):
        return self._link_guest

    @link_guest.setter
    def link_guest(self, value):
        self._link_guest = value
    @property
    def per_num(self):
        return self._per_num

    @per_num.setter
    def per_num(self, value):
        self._per_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.default_num:
            if hasattr(self.default_num, 'to_alipay_dict'):
                params['default_num'] = self.default_num.to_alipay_dict()
            else:
                params['default_num'] = self.default_num
        if self.link_guest:
            if hasattr(self.link_guest, 'to_alipay_dict'):
                params['link_guest'] = self.link_guest.to_alipay_dict()
            else:
                params['link_guest'] = self.link_guest
        if self.per_num:
            if hasattr(self.per_num, 'to_alipay_dict'):
                params['per_num'] = self.per_num.to_alipay_dict()
            else:
                params['per_num'] = self.per_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DefaultInCartInfo()
        if 'default_num' in d:
            o.default_num = d['default_num']
        if 'link_guest' in d:
            o.link_guest = d['link_guest']
        if 'per_num' in d:
            o.per_num = d['per_num']
        return o


