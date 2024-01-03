#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegressionInDomian import RegressionInDomian
from alipay.aop.api.domain.RegressionPrivate import RegressionPrivate
from alipay.aop.api.domain.RegressionPublic import RegressionPublic


class DomainNestOther(object):

    def __init__(self):
        self._com_domain = None
        self._com_private = None
        self._com_public = None

    @property
    def com_domain(self):
        return self._com_domain

    @com_domain.setter
    def com_domain(self, value):
        if isinstance(value, RegressionInDomian):
            self._com_domain = value
        else:
            self._com_domain = RegressionInDomian.from_alipay_dict(value)
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
    def com_public(self):
        return self._com_public

    @com_public.setter
    def com_public(self, value):
        if isinstance(value, RegressionPublic):
            self._com_public = value
        else:
            self._com_public = RegressionPublic.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.com_domain:
            if hasattr(self.com_domain, 'to_alipay_dict'):
                params['com_domain'] = self.com_domain.to_alipay_dict()
            else:
                params['com_domain'] = self.com_domain
        if self.com_private:
            if hasattr(self.com_private, 'to_alipay_dict'):
                params['com_private'] = self.com_private.to_alipay_dict()
            else:
                params['com_private'] = self.com_private
        if self.com_public:
            if hasattr(self.com_public, 'to_alipay_dict'):
                params['com_public'] = self.com_public.to_alipay_dict()
            else:
                params['com_public'] = self.com_public
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DomainNestOther()
        if 'com_domain' in d:
            o.com_domain = d['com_domain']
        if 'com_private' in d:
            o.com_private = d['com_private']
        if 'com_public' in d:
            o.com_public = d['com_public']
        return o


