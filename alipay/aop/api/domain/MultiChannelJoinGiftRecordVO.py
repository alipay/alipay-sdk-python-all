#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MultiChannelJoinGiftRecordVO(object):

    def __init__(self):
        self._channel_list = None
        self._channel_name_list = None
        self._expire_cnt = None
        self._gift_cnt = None
        self._group_id = None
        self._group_name = None
        self._init_cnt = None
        self._invalid_cnt = None
        self._suspend_cnt = None
        self._valid_cnt = None

    @property
    def channel_list(self):
        return self._channel_list

    @channel_list.setter
    def channel_list(self, value):
        if isinstance(value, list):
            self._channel_list = list()
            for i in value:
                self._channel_list.append(i)
    @property
    def channel_name_list(self):
        return self._channel_name_list

    @channel_name_list.setter
    def channel_name_list(self, value):
        if isinstance(value, list):
            self._channel_name_list = list()
            for i in value:
                self._channel_name_list.append(i)
    @property
    def expire_cnt(self):
        return self._expire_cnt

    @expire_cnt.setter
    def expire_cnt(self, value):
        self._expire_cnt = value
    @property
    def gift_cnt(self):
        return self._gift_cnt

    @gift_cnt.setter
    def gift_cnt(self, value):
        self._gift_cnt = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def init_cnt(self):
        return self._init_cnt

    @init_cnt.setter
    def init_cnt(self, value):
        self._init_cnt = value
    @property
    def invalid_cnt(self):
        return self._invalid_cnt

    @invalid_cnt.setter
    def invalid_cnt(self, value):
        self._invalid_cnt = value
    @property
    def suspend_cnt(self):
        return self._suspend_cnt

    @suspend_cnt.setter
    def suspend_cnt(self, value):
        self._suspend_cnt = value
    @property
    def valid_cnt(self):
        return self._valid_cnt

    @valid_cnt.setter
    def valid_cnt(self, value):
        self._valid_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_list:
            if isinstance(self.channel_list, list):
                for i in range(0, len(self.channel_list)):
                    element = self.channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_list[i] = element.to_alipay_dict()
            if hasattr(self.channel_list, 'to_alipay_dict'):
                params['channel_list'] = self.channel_list.to_alipay_dict()
            else:
                params['channel_list'] = self.channel_list
        if self.channel_name_list:
            if isinstance(self.channel_name_list, list):
                for i in range(0, len(self.channel_name_list)):
                    element = self.channel_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_name_list[i] = element.to_alipay_dict()
            if hasattr(self.channel_name_list, 'to_alipay_dict'):
                params['channel_name_list'] = self.channel_name_list.to_alipay_dict()
            else:
                params['channel_name_list'] = self.channel_name_list
        if self.expire_cnt:
            if hasattr(self.expire_cnt, 'to_alipay_dict'):
                params['expire_cnt'] = self.expire_cnt.to_alipay_dict()
            else:
                params['expire_cnt'] = self.expire_cnt
        if self.gift_cnt:
            if hasattr(self.gift_cnt, 'to_alipay_dict'):
                params['gift_cnt'] = self.gift_cnt.to_alipay_dict()
            else:
                params['gift_cnt'] = self.gift_cnt
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.init_cnt:
            if hasattr(self.init_cnt, 'to_alipay_dict'):
                params['init_cnt'] = self.init_cnt.to_alipay_dict()
            else:
                params['init_cnt'] = self.init_cnt
        if self.invalid_cnt:
            if hasattr(self.invalid_cnt, 'to_alipay_dict'):
                params['invalid_cnt'] = self.invalid_cnt.to_alipay_dict()
            else:
                params['invalid_cnt'] = self.invalid_cnt
        if self.suspend_cnt:
            if hasattr(self.suspend_cnt, 'to_alipay_dict'):
                params['suspend_cnt'] = self.suspend_cnt.to_alipay_dict()
            else:
                params['suspend_cnt'] = self.suspend_cnt
        if self.valid_cnt:
            if hasattr(self.valid_cnt, 'to_alipay_dict'):
                params['valid_cnt'] = self.valid_cnt.to_alipay_dict()
            else:
                params['valid_cnt'] = self.valid_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiChannelJoinGiftRecordVO()
        if 'channel_list' in d:
            o.channel_list = d['channel_list']
        if 'channel_name_list' in d:
            o.channel_name_list = d['channel_name_list']
        if 'expire_cnt' in d:
            o.expire_cnt = d['expire_cnt']
        if 'gift_cnt' in d:
            o.gift_cnt = d['gift_cnt']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'init_cnt' in d:
            o.init_cnt = d['init_cnt']
        if 'invalid_cnt' in d:
            o.invalid_cnt = d['invalid_cnt']
        if 'suspend_cnt' in d:
            o.suspend_cnt = d['suspend_cnt']
        if 'valid_cnt' in d:
            o.valid_cnt = d['valid_cnt']
        return o


