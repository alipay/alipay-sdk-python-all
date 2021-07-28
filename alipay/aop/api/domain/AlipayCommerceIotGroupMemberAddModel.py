#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotGroupMemberAddModel(object):

    def __init__(self):
        self._group_id = None
        self._sn_list = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def sn_list(self):
        return self._sn_list

    @sn_list.setter
    def sn_list(self, value):
        if isinstance(value, list):
            self._sn_list = list()
            for i in value:
                self._sn_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.sn_list:
            if isinstance(self.sn_list, list):
                for i in range(0, len(self.sn_list)):
                    element = self.sn_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn_list[i] = element.to_alipay_dict()
            if hasattr(self.sn_list, 'to_alipay_dict'):
                params['sn_list'] = self.sn_list.to_alipay_dict()
            else:
                params['sn_list'] = self.sn_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotGroupMemberAddModel()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'sn_list' in d:
            o.sn_list = d['sn_list']
        return o


