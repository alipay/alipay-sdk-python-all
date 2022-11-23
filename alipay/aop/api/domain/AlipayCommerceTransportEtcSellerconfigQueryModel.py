#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcSellerconfigQueryModel(object):

    def __init__(self):
        self._agent_appid = None
        self._agent_pid = None
        self._open_id = None
        self._query_scopes = None
        self._seller_id = None
        self._user_id = None

    @property
    def agent_appid(self):
        return self._agent_appid

    @agent_appid.setter
    def agent_appid(self, value):
        self._agent_appid = value
    @property
    def agent_pid(self):
        return self._agent_pid

    @agent_pid.setter
    def agent_pid(self, value):
        self._agent_pid = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def query_scopes(self):
        return self._query_scopes

    @query_scopes.setter
    def query_scopes(self, value):
        if isinstance(value, list):
            self._query_scopes = list()
            for i in value:
                self._query_scopes.append(i)
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_appid:
            if hasattr(self.agent_appid, 'to_alipay_dict'):
                params['agent_appid'] = self.agent_appid.to_alipay_dict()
            else:
                params['agent_appid'] = self.agent_appid
        if self.agent_pid:
            if hasattr(self.agent_pid, 'to_alipay_dict'):
                params['agent_pid'] = self.agent_pid.to_alipay_dict()
            else:
                params['agent_pid'] = self.agent_pid
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.query_scopes:
            if isinstance(self.query_scopes, list):
                for i in range(0, len(self.query_scopes)):
                    element = self.query_scopes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_scopes[i] = element.to_alipay_dict()
            if hasattr(self.query_scopes, 'to_alipay_dict'):
                params['query_scopes'] = self.query_scopes.to_alipay_dict()
            else:
                params['query_scopes'] = self.query_scopes
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcSellerconfigQueryModel()
        if 'agent_appid' in d:
            o.agent_appid = d['agent_appid']
        if 'agent_pid' in d:
            o.agent_pid = d['agent_pid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query_scopes' in d:
            o.query_scopes = d['query_scopes']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


