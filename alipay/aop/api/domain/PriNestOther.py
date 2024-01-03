#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegressionInDomian import RegressionInDomian
from alipay.aop.api.domain.RegressionPrivate import RegressionPrivate
from alipay.aop.api.domain.RegressionPublic import RegressionPublic


class PriNestOther(object):

    def __init__(self):
        self._com_indomain = None
        self._com_private = None
        self._com_pub = None

    @property
    def com_indomain(self):
        return self._com_indomain

    @com_indomain.setter
    def com_indomain(self, value):
        if isinstance(value, RegressionInDomian):
            self._com_indomain = value
        else:
            self._com_indomain = RegressionInDomian.from_alipay_dict(value)
    @property
    def com_private(self):
        return self._com_private

    @com_private.setter
    def com_private(self, value):
        if isinstance(value, RegressionPrivate):
            self._com_private = value
        else:
            self._com_private = RegressionPrivate.from_alipay_dict(value)
    @property
    def com_pub(self):
        return self._com_pub

    @com_pub.setter
    def com_pub(self, value):
        if isinstance(value, RegressionPublic):
            self._com_pub = value
        else:
            self._com_pub = RegressionPublic.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.com_indomain:
            if hasattr(self.com_indomain, 'to_alipay_dict'):
                params['com_indomain'] = self.com_indomain.to_alipay_dict()
            else:
                params['com_indomain'] = self.com_indomain
        if self.com_private:
            if hasattr(self.com_private, 'to_alipay_dict'):
                params['com_private'] = self.com_private.to_alipay_dict()
            else:
                params['com_private'] = self.com_private
        if self.com_pub:
            if hasattr(self.com_pub, 'to_alipay_dict'):
                params['com_pub'] = self.com_pub.to_alipay_dict()
            else:
                params['com_pub'] = self.com_pub
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PriNestOther()
        if 'com_indomain' in d:
            o.com_indomain = d['com_indomain']
        if 'com_private' in d:
            o.com_private = d['com_private']
        if 'com_pub' in d:
            o.com_pub = d['com_pub']
        return o


