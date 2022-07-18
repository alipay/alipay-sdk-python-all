#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppxVersionConfigVo(object):

    def __init__(self):
        self._id = None
        self._proportion = None
        self._ver = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def proportion(self):
        return self._proportion

    @proportion.setter
    def proportion(self, value):
        self._proportion = value
    @property
    def ver(self):
        return self._ver

    @ver.setter
    def ver(self, value):
        self._ver = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.proportion:
            if hasattr(self.proportion, 'to_alipay_dict'):
                params['proportion'] = self.proportion.to_alipay_dict()
            else:
                params['proportion'] = self.proportion
        if self.ver:
            if hasattr(self.ver, 'to_alipay_dict'):
                params['ver'] = self.ver.to_alipay_dict()
            else:
                params['ver'] = self.ver
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppxVersionConfigVo()
        if 'id' in d:
            o.id = d['id']
        if 'proportion' in d:
            o.proportion = d['proportion']
        if 'ver' in d:
            o.ver = d['ver']
        return o


