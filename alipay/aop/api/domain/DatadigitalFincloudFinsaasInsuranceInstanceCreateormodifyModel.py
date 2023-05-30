#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasInsuranceInstanceCreateormodifyModel(object):

    def __init__(self):
        self._channel = None
        self._command = None
        self._outer_goods_id = None
        self._outer_instance_id = None
        self._outer_tenant = None
        self._outer_tenant_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value
    @property
    def outer_goods_id(self):
        return self._outer_goods_id

    @outer_goods_id.setter
    def outer_goods_id(self, value):
        self._outer_goods_id = value
    @property
    def outer_instance_id(self):
        return self._outer_instance_id

    @outer_instance_id.setter
    def outer_instance_id(self, value):
        self._outer_instance_id = value
    @property
    def outer_tenant(self):
        return self._outer_tenant

    @outer_tenant.setter
    def outer_tenant(self, value):
        self._outer_tenant = value
    @property
    def outer_tenant_id(self):
        return self._outer_tenant_id

    @outer_tenant_id.setter
    def outer_tenant_id(self, value):
        self._outer_tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.command:
            if hasattr(self.command, 'to_alipay_dict'):
                params['command'] = self.command.to_alipay_dict()
            else:
                params['command'] = self.command
        if self.outer_goods_id:
            if hasattr(self.outer_goods_id, 'to_alipay_dict'):
                params['outer_goods_id'] = self.outer_goods_id.to_alipay_dict()
            else:
                params['outer_goods_id'] = self.outer_goods_id
        if self.outer_instance_id:
            if hasattr(self.outer_instance_id, 'to_alipay_dict'):
                params['outer_instance_id'] = self.outer_instance_id.to_alipay_dict()
            else:
                params['outer_instance_id'] = self.outer_instance_id
        if self.outer_tenant:
            if hasattr(self.outer_tenant, 'to_alipay_dict'):
                params['outer_tenant'] = self.outer_tenant.to_alipay_dict()
            else:
                params['outer_tenant'] = self.outer_tenant
        if self.outer_tenant_id:
            if hasattr(self.outer_tenant_id, 'to_alipay_dict'):
                params['outer_tenant_id'] = self.outer_tenant_id.to_alipay_dict()
            else:
                params['outer_tenant_id'] = self.outer_tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasInsuranceInstanceCreateormodifyModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'command' in d:
            o.command = d['command']
        if 'outer_goods_id' in d:
            o.outer_goods_id = d['outer_goods_id']
        if 'outer_instance_id' in d:
            o.outer_instance_id = d['outer_instance_id']
        if 'outer_tenant' in d:
            o.outer_tenant = d['outer_tenant']
        if 'outer_tenant_id' in d:
            o.outer_tenant_id = d['outer_tenant_id']
        return o


