#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingDataDeerInsightQueryModel(object):

    def __init__(self):
        self._alias = None
        self._app = None
        self._auth = None
        self._force = None
        self._force_update = None
        self._group_domain = None
        self._insight_domain = None
        self._params = None
        self._system = None

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value
    @property
    def app(self):
        return self._app

    @app.setter
    def app(self, value):
        self._app = value
    @property
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self, value):
        self._auth = value
    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, value):
        self._force = value
    @property
    def force_update(self):
        return self._force_update

    @force_update.setter
    def force_update(self, value):
        self._force_update = value
    @property
    def group_domain(self):
        return self._group_domain

    @group_domain.setter
    def group_domain(self, value):
        self._group_domain = value
    @property
    def insight_domain(self):
        return self._insight_domain

    @insight_domain.setter
    def insight_domain(self, value):
        self._insight_domain = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, value):
        self._system = value


    def to_alipay_dict(self):
        params = dict()
        if self.alias:
            if hasattr(self.alias, 'to_alipay_dict'):
                params['alias'] = self.alias.to_alipay_dict()
            else:
                params['alias'] = self.alias
        if self.app:
            if hasattr(self.app, 'to_alipay_dict'):
                params['app'] = self.app.to_alipay_dict()
            else:
                params['app'] = self.app
        if self.auth:
            if hasattr(self.auth, 'to_alipay_dict'):
                params['auth'] = self.auth.to_alipay_dict()
            else:
                params['auth'] = self.auth
        if self.force:
            if hasattr(self.force, 'to_alipay_dict'):
                params['force'] = self.force.to_alipay_dict()
            else:
                params['force'] = self.force
        if self.force_update:
            if hasattr(self.force_update, 'to_alipay_dict'):
                params['force_update'] = self.force_update.to_alipay_dict()
            else:
                params['force_update'] = self.force_update
        if self.group_domain:
            if hasattr(self.group_domain, 'to_alipay_dict'):
                params['group_domain'] = self.group_domain.to_alipay_dict()
            else:
                params['group_domain'] = self.group_domain
        if self.insight_domain:
            if hasattr(self.insight_domain, 'to_alipay_dict'):
                params['insight_domain'] = self.insight_domain.to_alipay_dict()
            else:
                params['insight_domain'] = self.insight_domain
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.system:
            if hasattr(self.system, 'to_alipay_dict'):
                params['system'] = self.system.to_alipay_dict()
            else:
                params['system'] = self.system
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingDataDeerInsightQueryModel()
        if 'alias' in d:
            o.alias = d['alias']
        if 'app' in d:
            o.app = d['app']
        if 'auth' in d:
            o.auth = d['auth']
        if 'force' in d:
            o.force = d['force']
        if 'force_update' in d:
            o.force_update = d['force_update']
        if 'group_domain' in d:
            o.group_domain = d['group_domain']
        if 'insight_domain' in d:
            o.insight_domain = d['insight_domain']
        if 'params' in d:
            o.params = d['params']
        if 'system' in d:
            o.system = d['system']
        return o


