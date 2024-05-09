#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupMsgVO import GroupMsgVO


class GroupWelcomeMsgVO(object):

    def __init__(self):
        self._welcome_group_msg = None
        self._welcome_text = None

    @property
    def welcome_group_msg(self):
        return self._welcome_group_msg

    @welcome_group_msg.setter
    def welcome_group_msg(self, value):
        if isinstance(value, GroupMsgVO):
            self._welcome_group_msg = value
        else:
            self._welcome_group_msg = GroupMsgVO.from_alipay_dict(value)
    @property
    def welcome_text(self):
        return self._welcome_text

    @welcome_text.setter
    def welcome_text(self, value):
        self._welcome_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.welcome_group_msg:
            if hasattr(self.welcome_group_msg, 'to_alipay_dict'):
                params['welcome_group_msg'] = self.welcome_group_msg.to_alipay_dict()
            else:
                params['welcome_group_msg'] = self.welcome_group_msg
        if self.welcome_text:
            if hasattr(self.welcome_text, 'to_alipay_dict'):
                params['welcome_text'] = self.welcome_text.to_alipay_dict()
            else:
                params['welcome_text'] = self.welcome_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupWelcomeMsgVO()
        if 'welcome_group_msg' in d:
            o.welcome_group_msg = d['welcome_group_msg']
        if 'welcome_text' in d:
            o.welcome_text = d['welcome_text']
        return o


