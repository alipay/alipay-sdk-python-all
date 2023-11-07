#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseRedisInstanceGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseRedisInstanceGetResponse, self).__init__()
        self._architecture_type = None
        self._instance_name = None
        self._instance_spec = None
        self._node_type = None
        self._proxy_port = None
        self._proxy_url = None
        self._proxy_version = None
        self._redis_version = None
        self._region = None
        self._shard_number = None
        self._status = None

    @property
    def architecture_type(self):
        return self._architecture_type

    @architecture_type.setter
    def architecture_type(self, value):
        self._architecture_type = value
    @property
    def instance_name(self):
        return self._instance_name

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = value
    @property
    def instance_spec(self):
        return self._instance_spec

    @instance_spec.setter
    def instance_spec(self, value):
        self._instance_spec = value
    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
    @property
    def proxy_port(self):
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, value):
        self._proxy_port = value
    @property
    def proxy_url(self):
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, value):
        self._proxy_url = value
    @property
    def proxy_version(self):
        return self._proxy_version

    @proxy_version.setter
    def proxy_version(self, value):
        self._proxy_version = value
    @property
    def redis_version(self):
        return self._redis_version

    @redis_version.setter
    def redis_version(self, value):
        self._redis_version = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def shard_number(self):
        return self._shard_number

    @shard_number.setter
    def shard_number(self, value):
        self._shard_number = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseRedisInstanceGetResponse, self).parse_response_content(response_content)
        if 'architecture_type' in response:
            self.architecture_type = response['architecture_type']
        if 'instance_name' in response:
            self.instance_name = response['instance_name']
        if 'instance_spec' in response:
            self.instance_spec = response['instance_spec']
        if 'node_type' in response:
            self.node_type = response['node_type']
        if 'proxy_port' in response:
            self.proxy_port = response['proxy_port']
        if 'proxy_url' in response:
            self.proxy_url = response['proxy_url']
        if 'proxy_version' in response:
            self.proxy_version = response['proxy_version']
        if 'redis_version' in response:
            self.redis_version = response['redis_version']
        if 'region' in response:
            self.region = response['region']
        if 'shard_number' in response:
            self.shard_number = response['shard_number']
        if 'status' in response:
            self.status = response['status']
