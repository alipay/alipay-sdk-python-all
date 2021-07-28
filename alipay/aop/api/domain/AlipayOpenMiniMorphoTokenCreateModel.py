#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MorphoIdentity import MorphoIdentity


class AlipayOpenMiniMorphoTokenCreateModel(object):

    def __init__(self):
        self._aid = None
        self._identity = None
        self._sid = None

    @property
    def aid(self):
        return self._aid

    @aid.setter
    def aid(self, value):
        self._aid = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        if isinstance(value, MorphoIdentity):
            self._identity = value
        else:
            self._identity = MorphoIdentity.from_alipay_dict(value)
    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, value):
        self._sid = value


    def to_alipay_dict(self):
        params = dict()
        if self.aid:
            if hasattr(self.aid, 'to_alipay_dict'):
                params['aid'] = self.aid.to_alipay_dict()
            else:
                params['aid'] = self.aid
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.sid:
            if hasattr(self.sid, 'to_alipay_dict'):
                params['sid'] = self.sid.to_alipay_dict()
            else:
                params['sid'] = self.sid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMorphoTokenCreateModel()
        if 'aid' in d:
            o.aid = d['aid']
        if 'identity' in d:
            o.identity = d['identity']
        if 'sid' in d:
            o.sid = d['sid']
        return o


