#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StillList(object):

    def __init__(self):
        self._olonk = None
        self._tlink = None

    @property
    def olonk(self):
        return self._olonk

    @olonk.setter
    def olonk(self, value):
        self._olonk = value
    @property
    def tlink(self):
        return self._tlink

    @tlink.setter
    def tlink(self, value):
        self._tlink = value


    def to_alipay_dict(self):
        params = dict()
        if self.olonk:
            if hasattr(self.olonk, 'to_alipay_dict'):
                params['olonk'] = self.olonk.to_alipay_dict()
            else:
                params['olonk'] = self.olonk
        if self.tlink:
            if hasattr(self.tlink, 'to_alipay_dict'):
                params['tlink'] = self.tlink.to_alipay_dict()
            else:
                params['tlink'] = self.tlink
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StillList()
        if 'olonk' in d:
            o.olonk = d['olonk']
        if 'tlink' in d:
            o.tlink = d['tlink']
        return o


