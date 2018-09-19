#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertAdvContentResponse import KbAdvertAdvContentResponse


class KbAdvertAdvChannelResponse(object):

    def __init__(self):
        self._adv_content_list = None
        self._adv_id = None
        self._channel_id = None
        self._channel_name = None
        self._channel_type = None

    @property
    def adv_content_list(self):
        return self._adv_content_list

    @adv_content_list.setter
    def adv_content_list(self, value):
        if isinstance(value, list):
            self._adv_content_list = list()
            for i in value:
                if isinstance(i, KbAdvertAdvContentResponse):
                    self._adv_content_list.append(i)
                else:
                    self._adv_content_list.append(KbAdvertAdvContentResponse.from_alipay_dict(i))
    @property
    def adv_id(self):
        return self._adv_id

    @adv_id.setter
    def adv_id(self, value):
        self._adv_id = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.adv_content_list:
            if isinstance(self.adv_content_list, list):
                for i in range(0, len(self.adv_content_list)):
                    element = self.adv_content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.adv_content_list[i] = element.to_alipay_dict()
            if hasattr(self.adv_content_list, 'to_alipay_dict'):
                params['adv_content_list'] = self.adv_content_list.to_alipay_dict()
            else:
                params['adv_content_list'] = self.adv_content_list
        if self.adv_id:
            if hasattr(self.adv_id, 'to_alipay_dict'):
                params['adv_id'] = self.adv_id.to_alipay_dict()
            else:
                params['adv_id'] = self.adv_id
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.channel_name:
            if hasattr(self.channel_name, 'to_alipay_dict'):
                params['channel_name'] = self.channel_name.to_alipay_dict()
            else:
                params['channel_name'] = self.channel_name
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertAdvChannelResponse()
        if 'adv_content_list' in d:
            o.adv_content_list = d['adv_content_list']
        if 'adv_id' in d:
            o.adv_id = d['adv_id']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'channel_name' in d:
            o.channel_name = d['channel_name']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        return o


