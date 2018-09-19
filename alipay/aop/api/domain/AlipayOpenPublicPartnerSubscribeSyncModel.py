#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicPartnerSubscribeSyncModel(object):

    def __init__(self):
        self._accept_msg = None
        self._follow_object_id = None
        self._operate_type = None
        self._push_switch = None
        self._source_id = None
        self._user_id = None

    @property
    def accept_msg(self):
        return self._accept_msg

    @accept_msg.setter
    def accept_msg(self, value):
        self._accept_msg = value
    @property
    def follow_object_id(self):
        return self._follow_object_id

    @follow_object_id.setter
    def follow_object_id(self, value):
        self._follow_object_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def push_switch(self):
        return self._push_switch

    @push_switch.setter
    def push_switch(self, value):
        self._push_switch = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_msg:
            if hasattr(self.accept_msg, 'to_alipay_dict'):
                params['accept_msg'] = self.accept_msg.to_alipay_dict()
            else:
                params['accept_msg'] = self.accept_msg
        if self.follow_object_id:
            if hasattr(self.follow_object_id, 'to_alipay_dict'):
                params['follow_object_id'] = self.follow_object_id.to_alipay_dict()
            else:
                params['follow_object_id'] = self.follow_object_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.push_switch:
            if hasattr(self.push_switch, 'to_alipay_dict'):
                params['push_switch'] = self.push_switch.to_alipay_dict()
            else:
                params['push_switch'] = self.push_switch
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
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
        o = AlipayOpenPublicPartnerSubscribeSyncModel()
        if 'accept_msg' in d:
            o.accept_msg = d['accept_msg']
        if 'follow_object_id' in d:
            o.follow_object_id = d['follow_object_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'push_switch' in d:
            o.push_switch = d['push_switch']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


