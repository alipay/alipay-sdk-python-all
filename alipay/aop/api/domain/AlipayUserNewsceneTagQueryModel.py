#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayUserPrincipalInfo import AlipayUserPrincipalInfo


class AlipayUserNewsceneTagQueryModel(object):

    def __init__(self):
        self._principal = None
        self._query_tags = None
        self._scene = None

    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        if isinstance(value, AlipayUserPrincipalInfo):
            self._principal = value
        else:
            self._principal = AlipayUserPrincipalInfo.from_alipay_dict(value)
    @property
    def query_tags(self):
        return self._query_tags

    @query_tags.setter
    def query_tags(self, value):
        self._query_tags = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.query_tags:
            if hasattr(self.query_tags, 'to_alipay_dict'):
                params['query_tags'] = self.query_tags.to_alipay_dict()
            else:
                params['query_tags'] = self.query_tags
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserNewsceneTagQueryModel()
        if 'principal' in d:
            o.principal = d['principal']
        if 'query_tags' in d:
            o.query_tags = d['query_tags']
        if 'scene' in d:
            o.scene = d['scene']
        return o


