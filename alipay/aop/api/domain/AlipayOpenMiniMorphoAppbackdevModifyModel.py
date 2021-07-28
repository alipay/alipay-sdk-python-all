#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MorphoIdentity import MorphoIdentity


class AlipayOpenMiniMorphoAppbackdevModifyModel(object):

    def __init__(self):
        self._id = None
        self._identity = None

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
        o = AlipayOpenMiniMorphoAppbackdevModifyModel()
        if 'id' in d:
            o.id = d['id']
        if 'identity' in d:
            o.identity = d['identity']
        return o


