#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupGroupinstanceinfoQueryModel(object):

    def __init__(self):
        self._group_instance_id = None
        self._need_member = None

    @property
    def group_instance_id(self):
        return self._group_instance_id

    @group_instance_id.setter
    def group_instance_id(self, value):
        self._group_instance_id = value
    @property
    def need_member(self):
        return self._need_member

    @need_member.setter
    def need_member(self, value):
        self._need_member = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_instance_id:
            if hasattr(self.group_instance_id, 'to_alipay_dict'):
                params['group_instance_id'] = self.group_instance_id.to_alipay_dict()
            else:
                params['group_instance_id'] = self.group_instance_id
        if self.need_member:
            if hasattr(self.need_member, 'to_alipay_dict'):
                params['need_member'] = self.need_member.to_alipay_dict()
            else:
                params['need_member'] = self.need_member
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupGroupinstanceinfoQueryModel()
        if 'group_instance_id' in d:
            o.group_instance_id = d['group_instance_id']
        if 'need_member' in d:
            o.need_member = d['need_member']
        return o


