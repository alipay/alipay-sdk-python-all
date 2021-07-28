#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniDeploypackageQueryModel(object):

    def __init__(self):
        self._bundle_id = None
        self._channel = None
        self._client = None
        self._diu = None
        self._env = None
        self._existed = None
        self._gray_rules = None
        self._local_app_info = None
        self._platform = None
        self._prefer_local = None
        self._protocol = None
        self._query = None
        self._req_mode = None
        self._sdk = None
        self._stable_rpc = None
        self._system = None
        self._user_id = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value
    @property
    def diu(self):
        return self._diu

    @diu.setter
    def diu(self, value):
        self._diu = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def existed(self):
        return self._existed

    @existed.setter
    def existed(self, value):
        self._existed = value
    @property
    def gray_rules(self):
        return self._gray_rules

    @gray_rules.setter
    def gray_rules(self, value):
        self._gray_rules = value
    @property
    def local_app_info(self):
        return self._local_app_info

    @local_app_info.setter
    def local_app_info(self, value):
        self._local_app_info = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def prefer_local(self):
        return self._prefer_local

    @prefer_local.setter
    def prefer_local(self, value):
        self._prefer_local = value
    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        self._protocol = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def req_mode(self):
        return self._req_mode

    @req_mode.setter
    def req_mode(self, value):
        self._req_mode = value
    @property
    def sdk(self):
        return self._sdk

    @sdk.setter
    def sdk(self, value):
        self._sdk = value
    @property
    def stable_rpc(self):
        return self._stable_rpc

    @stable_rpc.setter
    def stable_rpc(self, value):
        self._stable_rpc = value
    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, value):
        self._system = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.client:
            if hasattr(self.client, 'to_alipay_dict'):
                params['client'] = self.client.to_alipay_dict()
            else:
                params['client'] = self.client
        if self.diu:
            if hasattr(self.diu, 'to_alipay_dict'):
                params['diu'] = self.diu.to_alipay_dict()
            else:
                params['diu'] = self.diu
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.existed:
            if hasattr(self.existed, 'to_alipay_dict'):
                params['existed'] = self.existed.to_alipay_dict()
            else:
                params['existed'] = self.existed
        if self.gray_rules:
            if hasattr(self.gray_rules, 'to_alipay_dict'):
                params['gray_rules'] = self.gray_rules.to_alipay_dict()
            else:
                params['gray_rules'] = self.gray_rules
        if self.local_app_info:
            if hasattr(self.local_app_info, 'to_alipay_dict'):
                params['local_app_info'] = self.local_app_info.to_alipay_dict()
            else:
                params['local_app_info'] = self.local_app_info
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.prefer_local:
            if hasattr(self.prefer_local, 'to_alipay_dict'):
                params['prefer_local'] = self.prefer_local.to_alipay_dict()
            else:
                params['prefer_local'] = self.prefer_local
        if self.protocol:
            if hasattr(self.protocol, 'to_alipay_dict'):
                params['protocol'] = self.protocol.to_alipay_dict()
            else:
                params['protocol'] = self.protocol
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.req_mode:
            if hasattr(self.req_mode, 'to_alipay_dict'):
                params['req_mode'] = self.req_mode.to_alipay_dict()
            else:
                params['req_mode'] = self.req_mode
        if self.sdk:
            if hasattr(self.sdk, 'to_alipay_dict'):
                params['sdk'] = self.sdk.to_alipay_dict()
            else:
                params['sdk'] = self.sdk
        if self.stable_rpc:
            if hasattr(self.stable_rpc, 'to_alipay_dict'):
                params['stable_rpc'] = self.stable_rpc.to_alipay_dict()
            else:
                params['stable_rpc'] = self.stable_rpc
        if self.system:
            if hasattr(self.system, 'to_alipay_dict'):
                params['system'] = self.system.to_alipay_dict()
            else:
                params['system'] = self.system
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
        o = AlipayOpenMiniDeploypackageQueryModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'client' in d:
            o.client = d['client']
        if 'diu' in d:
            o.diu = d['diu']
        if 'env' in d:
            o.env = d['env']
        if 'existed' in d:
            o.existed = d['existed']
        if 'gray_rules' in d:
            o.gray_rules = d['gray_rules']
        if 'local_app_info' in d:
            o.local_app_info = d['local_app_info']
        if 'platform' in d:
            o.platform = d['platform']
        if 'prefer_local' in d:
            o.prefer_local = d['prefer_local']
        if 'protocol' in d:
            o.protocol = d['protocol']
        if 'query' in d:
            o.query = d['query']
        if 'req_mode' in d:
            o.req_mode = d['req_mode']
        if 'sdk' in d:
            o.sdk = d['sdk']
        if 'stable_rpc' in d:
            o.stable_rpc = d['stable_rpc']
        if 'system' in d:
            o.system = d['system']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


