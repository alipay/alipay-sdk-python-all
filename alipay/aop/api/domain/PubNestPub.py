#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegressionInDomian import RegressionInDomian
from alipay.aop.api.domain.RegressionPrivate import RegressionPrivate
from alipay.aop.api.domain.RegressionPublic import RegressionPublic


class PubNestPub(object):

    def __init__(self):
        self._comp_indomain = None
        self._comp_private = None
        self._complex = None

    @property
    def comp_indomain(self):
        return self._comp_indomain

    @comp_indomain.setter
    def comp_indomain(self, value):
        if isinstance(value, RegressionInDomian):
            self._comp_indomain = value
        else:
            self._comp_indomain = RegressionInDomian.from_alipay_dict(value)
    @property
    def comp_private(self):
        return self._comp_private

    @comp_private.setter
    def comp_private(self, value):
        if isinstance(value, RegressionPrivate):
            self._comp_private = value
        else:
            self._comp_private = RegressionPrivate.from_alipay_dict(value)
    @property
    def complex(self):
        return self._complex

    @complex.setter
    def complex(self, value):
        if isinstance(value, RegressionPublic):
            self._complex = value
        else:
            self._complex = RegressionPublic.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.comp_indomain:
            if hasattr(self.comp_indomain, 'to_alipay_dict'):
                params['comp_indomain'] = self.comp_indomain.to_alipay_dict()
            else:
                params['comp_indomain'] = self.comp_indomain
        if self.comp_private:
            if hasattr(self.comp_private, 'to_alipay_dict'):
                params['comp_private'] = self.comp_private.to_alipay_dict()
            else:
                params['comp_private'] = self.comp_private
        if self.complex:
            if hasattr(self.complex, 'to_alipay_dict'):
                params['complex'] = self.complex.to_alipay_dict()
            else:
                params['complex'] = self.complex
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PubNestPub()
        if 'comp_indomain' in d:
            o.comp_indomain = d['comp_indomain']
        if 'comp_private' in d:
            o.comp_private = d['comp_private']
        if 'complex' in d:
            o.complex = d['complex']
        return o


