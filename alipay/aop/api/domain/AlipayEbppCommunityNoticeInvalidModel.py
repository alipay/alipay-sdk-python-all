#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityNoticeInvalidModel(object):

    def __init__(self):
        self._alipay_notice_id = None
        self._alipay_user_id = None
        self._community_short_name = None
        self._open_id = None
        self._out_community_id = None

    @property
    def alipay_notice_id(self):
        return self._alipay_notice_id

    @alipay_notice_id.setter
    def alipay_notice_id(self, value):
        self._alipay_notice_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_community_id(self):
        return self._out_community_id

    @out_community_id.setter
    def out_community_id(self, value):
        self._out_community_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_notice_id:
            if hasattr(self.alipay_notice_id, 'to_alipay_dict'):
                params['alipay_notice_id'] = self.alipay_notice_id.to_alipay_dict()
            else:
                params['alipay_notice_id'] = self.alipay_notice_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_community_id:
            if hasattr(self.out_community_id, 'to_alipay_dict'):
                params['out_community_id'] = self.out_community_id.to_alipay_dict()
            else:
                params['out_community_id'] = self.out_community_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityNoticeInvalidModel()
        if 'alipay_notice_id' in d:
            o.alipay_notice_id = d['alipay_notice_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_community_id' in d:
            o.out_community_id = d['out_community_id']
        return o


