#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportNdeviceResourceSendModel(object):

    def __init__(self):
        self._release_type = None
        self._resource_channel = None
        self._resource_tag = None
        self._sn = None

    @property
    def release_type(self):
        return self._release_type

    @release_type.setter
    def release_type(self, value):
        self._release_type = value
    @property
    def resource_channel(self):
        return self._resource_channel

    @resource_channel.setter
    def resource_channel(self, value):
        self._resource_channel = value
    @property
    def resource_tag(self):
        return self._resource_tag

    @resource_tag.setter
    def resource_tag(self, value):
        self._resource_tag = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.release_type:
            if hasattr(self.release_type, 'to_alipay_dict'):
                params['release_type'] = self.release_type.to_alipay_dict()
            else:
                params['release_type'] = self.release_type
        if self.resource_channel:
            if hasattr(self.resource_channel, 'to_alipay_dict'):
                params['resource_channel'] = self.resource_channel.to_alipay_dict()
            else:
                params['resource_channel'] = self.resource_channel
        if self.resource_tag:
            if hasattr(self.resource_tag, 'to_alipay_dict'):
                params['resource_tag'] = self.resource_tag.to_alipay_dict()
            else:
                params['resource_tag'] = self.resource_tag
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportNdeviceResourceSendModel()
        if 'release_type' in d:
            o.release_type = d['release_type']
        if 'resource_channel' in d:
            o.resource_channel = d['resource_channel']
        if 'resource_tag' in d:
            o.resource_tag = d['resource_tag']
        if 'sn' in d:
            o.sn = d['sn']
        return o


