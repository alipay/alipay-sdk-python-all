#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupBaseInfoVO import GroupBaseInfoVO
from alipay.aop.api.domain.GroupInstanceInfoVO import GroupInstanceInfoVO
from alipay.aop.api.domain.GroupWelcomeMsgVO import GroupWelcomeMsgVO


class GroupDetailVO(object):

    def __init__(self):
        self._group_base_info = None
        self._group_instance_info = None
        self._welcome_msg = None

    @property
    def group_base_info(self):
        return self._group_base_info

    @group_base_info.setter
    def group_base_info(self, value):
        if isinstance(value, GroupBaseInfoVO):
            self._group_base_info = value
        else:
            self._group_base_info = GroupBaseInfoVO.from_alipay_dict(value)
    @property
    def group_instance_info(self):
        return self._group_instance_info

    @group_instance_info.setter
    def group_instance_info(self, value):
        if isinstance(value, GroupInstanceInfoVO):
            self._group_instance_info = value
        else:
            self._group_instance_info = GroupInstanceInfoVO.from_alipay_dict(value)
    @property
    def welcome_msg(self):
        return self._welcome_msg

    @welcome_msg.setter
    def welcome_msg(self, value):
        if isinstance(value, GroupWelcomeMsgVO):
            self._welcome_msg = value
        else:
            self._welcome_msg = GroupWelcomeMsgVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.group_base_info:
            if hasattr(self.group_base_info, 'to_alipay_dict'):
                params['group_base_info'] = self.group_base_info.to_alipay_dict()
            else:
                params['group_base_info'] = self.group_base_info
        if self.group_instance_info:
            if hasattr(self.group_instance_info, 'to_alipay_dict'):
                params['group_instance_info'] = self.group_instance_info.to_alipay_dict()
            else:
                params['group_instance_info'] = self.group_instance_info
        if self.welcome_msg:
            if hasattr(self.welcome_msg, 'to_alipay_dict'):
                params['welcome_msg'] = self.welcome_msg.to_alipay_dict()
            else:
                params['welcome_msg'] = self.welcome_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupDetailVO()
        if 'group_base_info' in d:
            o.group_base_info = d['group_base_info']
        if 'group_instance_info' in d:
            o.group_instance_info = d['group_instance_info']
        if 'welcome_msg' in d:
            o.welcome_msg = d['welcome_msg']
        return o


