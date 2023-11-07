#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FxiaokeCreateCustomerChannelAccountResponse(object):

    def __init__(self):
        self._channel = None
        self._channel_uid = None
        self._cid = None
        self._id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def channel_uid(self):
        return self._channel_uid

    @channel_uid.setter
    def channel_uid(self, value):
        self._channel_uid = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.channel_uid:
            if hasattr(self.channel_uid, 'to_alipay_dict'):
                params['channel_uid'] = self.channel_uid.to_alipay_dict()
            else:
                params['channel_uid'] = self.channel_uid
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FxiaokeCreateCustomerChannelAccountResponse()
        if 'channel' in d:
            o.channel = d['channel']
        if 'channel_uid' in d:
            o.channel_uid = d['channel_uid']
        if 'cid' in d:
            o.cid = d['cid']
        if 'id' in d:
            o.id = d['id']
        return o


