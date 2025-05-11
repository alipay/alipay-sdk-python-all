#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAppRes(object):

    def __init__(self):
        self._action_type = None
        self._app_principal_risk_memo = None
        self._app_risk_memo = None
        self._app_status = None
        self._desc = None
        self._icon = None
        self._limitation_tag = None
        self._mini_app_id = None
        self._name = None
        self._risk_type = None
        self._url = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def app_principal_risk_memo(self):
        return self._app_principal_risk_memo

    @app_principal_risk_memo.setter
    def app_principal_risk_memo(self, value):
        self._app_principal_risk_memo = value
    @property
    def app_risk_memo(self):
        return self._app_risk_memo

    @app_risk_memo.setter
    def app_risk_memo(self, value):
        self._app_risk_memo = value
    @property
    def app_status(self):
        return self._app_status

    @app_status.setter
    def app_status(self, value):
        self._app_status = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def limitation_tag(self):
        return self._limitation_tag

    @limitation_tag.setter
    def limitation_tag(self, value):
        self._limitation_tag = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.app_principal_risk_memo:
            if hasattr(self.app_principal_risk_memo, 'to_alipay_dict'):
                params['app_principal_risk_memo'] = self.app_principal_risk_memo.to_alipay_dict()
            else:
                params['app_principal_risk_memo'] = self.app_principal_risk_memo
        if self.app_risk_memo:
            if hasattr(self.app_risk_memo, 'to_alipay_dict'):
                params['app_risk_memo'] = self.app_risk_memo.to_alipay_dict()
            else:
                params['app_risk_memo'] = self.app_risk_memo
        if self.app_status:
            if hasattr(self.app_status, 'to_alipay_dict'):
                params['app_status'] = self.app_status.to_alipay_dict()
            else:
                params['app_status'] = self.app_status
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.limitation_tag:
            if hasattr(self.limitation_tag, 'to_alipay_dict'):
                params['limitation_tag'] = self.limitation_tag.to_alipay_dict()
            else:
                params['limitation_tag'] = self.limitation_tag
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAppRes()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'app_principal_risk_memo' in d:
            o.app_principal_risk_memo = d['app_principal_risk_memo']
        if 'app_risk_memo' in d:
            o.app_risk_memo = d['app_risk_memo']
        if 'app_status' in d:
            o.app_status = d['app_status']
        if 'desc' in d:
            o.desc = d['desc']
        if 'icon' in d:
            o.icon = d['icon']
        if 'limitation_tag' in d:
            o.limitation_tag = d['limitation_tag']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'name' in d:
            o.name = d['name']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'url' in d:
            o.url = d['url']
        return o


