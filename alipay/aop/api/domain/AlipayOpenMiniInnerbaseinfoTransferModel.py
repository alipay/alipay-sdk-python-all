#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerbaseinfoTransferModel(object):

    def __init__(self):
        self._app_origin = None
        self._login_id = None
        self._mini_app_id = None
        self._owner_entity = None
        self._partner_domain = None
        self._pid = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def owner_entity(self):
        return self._owner_entity

    @owner_entity.setter
    def owner_entity(self, value):
        self._owner_entity = value
    @property
    def partner_domain(self):
        return self._partner_domain

    @partner_domain.setter
    def partner_domain(self, value):
        self._partner_domain = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.owner_entity:
            if hasattr(self.owner_entity, 'to_alipay_dict'):
                params['owner_entity'] = self.owner_entity.to_alipay_dict()
            else:
                params['owner_entity'] = self.owner_entity
        if self.partner_domain:
            if hasattr(self.partner_domain, 'to_alipay_dict'):
                params['partner_domain'] = self.partner_domain.to_alipay_dict()
            else:
                params['partner_domain'] = self.partner_domain
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerbaseinfoTransferModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'owner_entity' in d:
            o.owner_entity = d['owner_entity']
        if 'partner_domain' in d:
            o.partner_domain = d['partner_domain']
        if 'pid' in d:
            o.pid = d['pid']
        return o


