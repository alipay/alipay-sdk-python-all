#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainWfLimitamountQueryModel(object):

    def __init__(self):
        self._scene = None
        self._site = None
        self._siteuserid = None

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def siteuserid(self):
        return self._siteuserid

    @siteuserid.setter
    def siteuserid(self, value):
        self._siteuserid = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.siteuserid:
            if hasattr(self.siteuserid, 'to_alipay_dict'):
                params['siteuserid'] = self.siteuserid.to_alipay_dict()
            else:
                params['siteuserid'] = self.siteuserid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainWfLimitamountQueryModel()
        if 'scene' in d:
            o.scene = d['scene']
        if 'site' in d:
            o.site = d['site']
        if 'siteuserid' in d:
            o.siteuserid = d['siteuserid']
        return o


