#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseBcGroupQueryModel(object):

    def __init__(self):
        self._group_id = None
        self._need_member = None
        self._operate_business_id = None
        self._tenant_id = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def need_member(self):
        return self._need_member

    @need_member.setter
    def need_member(self, value):
        self._need_member = value
    @property
    def operate_business_id(self):
        return self._operate_business_id

    @operate_business_id.setter
    def operate_business_id(self, value):
        self._operate_business_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.need_member:
            if hasattr(self.need_member, 'to_alipay_dict'):
                params['need_member'] = self.need_member.to_alipay_dict()
            else:
                params['need_member'] = self.need_member
        if self.operate_business_id:
            if hasattr(self.operate_business_id, 'to_alipay_dict'):
                params['operate_business_id'] = self.operate_business_id.to_alipay_dict()
            else:
                params['operate_business_id'] = self.operate_business_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseBcGroupQueryModel()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'need_member' in d:
            o.need_member = d['need_member']
        if 'operate_business_id' in d:
            o.operate_business_id = d['operate_business_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


