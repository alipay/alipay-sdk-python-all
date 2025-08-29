#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssistantRedPacketVO(object):

    def __init__(self):
        self._red_packet_id = None
        self._visible_users = None

    @property
    def red_packet_id(self):
        return self._red_packet_id

    @red_packet_id.setter
    def red_packet_id(self, value):
        self._red_packet_id = value
    @property
    def visible_users(self):
        return self._visible_users

    @visible_users.setter
    def visible_users(self, value):
        self._visible_users = value


    def to_alipay_dict(self):
        params = dict()
        if self.red_packet_id:
            if hasattr(self.red_packet_id, 'to_alipay_dict'):
                params['red_packet_id'] = self.red_packet_id.to_alipay_dict()
            else:
                params['red_packet_id'] = self.red_packet_id
        if self.visible_users:
            if hasattr(self.visible_users, 'to_alipay_dict'):
                params['visible_users'] = self.visible_users.to_alipay_dict()
            else:
                params['visible_users'] = self.visible_users
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssistantRedPacketVO()
        if 'red_packet_id' in d:
            o.red_packet_id = d['red_packet_id']
        if 'visible_users' in d:
            o.visible_users = d['visible_users']
        return o


