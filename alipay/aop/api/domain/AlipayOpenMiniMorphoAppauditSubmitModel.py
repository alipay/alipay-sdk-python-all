#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MorphoIdentity import MorphoIdentity


class AlipayOpenMiniMorphoAppauditSubmitModel(object):

    def __init__(self):
        self._id = None
        self._identity = None
        self._screen_shots = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
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
    def screen_shots(self):
        return self._screen_shots

    @screen_shots.setter
    def screen_shots(self, value):
        self._screen_shots = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.screen_shots:
            if hasattr(self.screen_shots, 'to_alipay_dict'):
                params['screen_shots'] = self.screen_shots.to_alipay_dict()
            else:
                params['screen_shots'] = self.screen_shots
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMorphoAppauditSubmitModel()
        if 'id' in d:
            o.id = d['id']
        if 'identity' in d:
            o.identity = d['identity']
        if 'screen_shots' in d:
            o.screen_shots = d['screen_shots']
        return o


