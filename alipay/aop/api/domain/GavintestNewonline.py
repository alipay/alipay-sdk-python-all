#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class GavintestNewonline(object):

    def __init__(self):
        self._dem = None
        self._string = None

    @property
    def dem(self):
        return self._dem

    @dem.setter
    def dem(self, value):
        if isinstance(value, list):
            self._dem = list()
            for i in value:
                self._dem.append(i)
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        if isinstance(value, GavintestNewLeveaOne):
            self._string = value
        else:
            self._string = GavintestNewLeveaOne.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.dem:
            if isinstance(self.dem, list):
                for i in range(0, len(self.dem)):
                    element = self.dem[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dem[i] = element.to_alipay_dict()
            if hasattr(self.dem, 'to_alipay_dict'):
                params['dem'] = self.dem.to_alipay_dict()
            else:
                params['dem'] = self.dem
        if self.string:
            if hasattr(self.string, 'to_alipay_dict'):
                params['string'] = self.string.to_alipay_dict()
            else:
                params['string'] = self.string
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GavintestNewonline()
        if 'dem' in d:
            o.dem = d['dem']
        if 'string' in d:
            o.string = d['string']
        return o


