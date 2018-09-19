#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PubChannelDTO(object):

    def __init__(self):
        self._ext_info = None
        self._pub_channel = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def pub_channel(self):
        return self._pub_channel

    @pub_channel.setter
    def pub_channel(self, value):
        self._pub_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.pub_channel:
            if hasattr(self.pub_channel, 'to_alipay_dict'):
                params['pub_channel'] = self.pub_channel.to_alipay_dict()
            else:
                params['pub_channel'] = self.pub_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PubChannelDTO()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'pub_channel' in d:
            o.pub_channel = d['pub_channel']
        return o


