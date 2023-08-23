#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessRelationShopMemberDigest(object):

    def __init__(self):
        self._gmt_create = None
        self._member_id = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessRelationShopMemberDigest()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'member_id' in d:
            o.member_id = d['member_id']
        return o


