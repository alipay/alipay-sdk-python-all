#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupGiftVO import GroupGiftVO


class MultiChannelJoinGiftVO(object):

    def __init__(self):
        self._group_id = None
        self._group_name = None
        self._join_gifts = None

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
    def join_gifts(self):
        return self._join_gifts

    @join_gifts.setter
    def join_gifts(self, value):
        if isinstance(value, list):
            self._join_gifts = list()
            for i in value:
                if isinstance(i, GroupGiftVO):
                    self._join_gifts.append(i)
                else:
                    self._join_gifts.append(GroupGiftVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
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
        if self.join_gifts:
            if isinstance(self.join_gifts, list):
                for i in range(0, len(self.join_gifts)):
                    element = self.join_gifts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.join_gifts[i] = element.to_alipay_dict()
            if hasattr(self.join_gifts, 'to_alipay_dict'):
                params['join_gifts'] = self.join_gifts.to_alipay_dict()
            else:
                params['join_gifts'] = self.join_gifts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiChannelJoinGiftVO()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'join_gifts' in d:
            o.join_gifts = d['join_gifts']
        return o


