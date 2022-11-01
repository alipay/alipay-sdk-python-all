#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsPolicyLinkDTO(object):

    def __init__(self):
        self._authed_token = None
        self._authed_url = None
        self._expiration = None
        self._policy_status = None
        self._product_code = None
        self._product_icon = None
        self._product_name = None
        self._product_plan_id = None

    @property
    def authed_token(self):
        return self._authed_token

    @authed_token.setter
    def authed_token(self, value):
        self._authed_token = value
    @property
    def authed_url(self):
        return self._authed_url

    @authed_url.setter
    def authed_url(self, value):
        self._authed_url = value
    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        self._expiration = value
    @property
    def policy_status(self):
        return self._policy_status

    @policy_status.setter
    def policy_status(self, value):
        self._policy_status = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_icon(self):
        return self._product_icon

    @product_icon.setter
    def product_icon(self, value):
        self._product_icon = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.authed_token:
            if hasattr(self.authed_token, 'to_alipay_dict'):
                params['authed_token'] = self.authed_token.to_alipay_dict()
            else:
                params['authed_token'] = self.authed_token
        if self.authed_url:
            if hasattr(self.authed_url, 'to_alipay_dict'):
                params['authed_url'] = self.authed_url.to_alipay_dict()
            else:
                params['authed_url'] = self.authed_url
        if self.expiration:
            if hasattr(self.expiration, 'to_alipay_dict'):
                params['expiration'] = self.expiration.to_alipay_dict()
            else:
                params['expiration'] = self.expiration
        if self.policy_status:
            if hasattr(self.policy_status, 'to_alipay_dict'):
                params['policy_status'] = self.policy_status.to_alipay_dict()
            else:
                params['policy_status'] = self.policy_status
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_icon:
            if hasattr(self.product_icon, 'to_alipay_dict'):
                params['product_icon'] = self.product_icon.to_alipay_dict()
            else:
                params['product_icon'] = self.product_icon
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsPolicyLinkDTO()
        if 'authed_token' in d:
            o.authed_token = d['authed_token']
        if 'authed_url' in d:
            o.authed_url = d['authed_url']
        if 'expiration' in d:
            o.expiration = d['expiration']
        if 'policy_status' in d:
            o.policy_status = d['policy_status']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_icon' in d:
            o.product_icon = d['product_icon']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        return o


