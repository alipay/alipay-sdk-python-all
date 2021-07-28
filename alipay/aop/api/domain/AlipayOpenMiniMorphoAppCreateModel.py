#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MorphoCreateApp import MorphoCreateApp
from alipay.aop.api.domain.MorphoIdentity import MorphoIdentity
from alipay.aop.api.domain.MorphoCreateSource import MorphoCreateSource
from alipay.aop.api.domain.MorphoTemplate import MorphoTemplate


class AlipayOpenMiniMorphoAppCreateModel(object):

    def __init__(self):
        self._application = None
        self._identity = None
        self._source = None
        self._template = None

    @property
    def application(self):
        return self._application

    @application.setter
    def application(self, value):
        if isinstance(value, MorphoCreateApp):
            self._application = value
        else:
            self._application = MorphoCreateApp.from_alipay_dict(value)
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
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if isinstance(value, MorphoCreateSource):
            self._source = value
        else:
            self._source = MorphoCreateSource.from_alipay_dict(value)
    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        if isinstance(value, MorphoTemplate):
            self._template = value
        else:
            self._template = MorphoTemplate.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.application:
            if hasattr(self.application, 'to_alipay_dict'):
                params['application'] = self.application.to_alipay_dict()
            else:
                params['application'] = self.application
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.template:
            if hasattr(self.template, 'to_alipay_dict'):
                params['template'] = self.template.to_alipay_dict()
            else:
                params['template'] = self.template
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMorphoAppCreateModel()
        if 'application' in d:
            o.application = d['application']
        if 'identity' in d:
            o.identity = d['identity']
        if 'source' in d:
            o.source = d['source']
        if 'template' in d:
            o.template = d['template']
        return o


