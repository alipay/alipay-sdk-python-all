#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupWelcomeMsgVO import GroupWelcomeMsgVO


class AlipayMerchantGroupWelcomemsgModifyModel(object):

    def __init__(self):
        self._group_ids = None
        self._welcome_msg = None

    @property
    def group_ids(self):
        return self._group_ids

    @group_ids.setter
    def group_ids(self, value):
        if isinstance(value, list):
            self._group_ids = list()
            for i in value:
                self._group_ids.append(i)
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
        if self.group_ids:
            if isinstance(self.group_ids, list):
                for i in range(0, len(self.group_ids)):
                    element = self.group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_ids[i] = element.to_alipay_dict()
            if hasattr(self.group_ids, 'to_alipay_dict'):
                params['group_ids'] = self.group_ids.to_alipay_dict()
            else:
                params['group_ids'] = self.group_ids
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
        o = AlipayMerchantGroupWelcomemsgModifyModel()
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        if 'welcome_msg' in d:
            o.welcome_msg = d['welcome_msg']
        return o


