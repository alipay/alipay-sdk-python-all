#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MorphoIdentity import MorphoIdentity


class AlipayOpenMiniMorphoAppgrayOnlineModel(object):

    def __init__(self):
        self._gray_strategy = None
        self._id = None
        self._identity = None

    @property
    def gray_strategy(self):
        return self._gray_strategy

    @gray_strategy.setter
    def gray_strategy(self, value):
        self._gray_strategy = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.gray_strategy:
            if hasattr(self.gray_strategy, 'to_alipay_dict'):
                params['gray_strategy'] = self.gray_strategy.to_alipay_dict()
            else:
                params['gray_strategy'] = self.gray_strategy
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMorphoAppgrayOnlineModel()
        if 'gray_strategy' in d:
            o.gray_strategy = d['gray_strategy']
        if 'id' in d:
            o.id = d['id']
        if 'identity' in d:
            o.identity = d['identity']
        return o


