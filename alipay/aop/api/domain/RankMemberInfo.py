#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RankMemberInfo(object):

    def __init__(self):
        self._group_name = None
        self._member_name = None
        self._out_member_id = None
        self._rank = None
        self._rank_detail = None

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def member_name(self):
        return self._member_name

    @member_name.setter
    def member_name(self, value):
        self._member_name = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        self._out_member_id = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def rank_detail(self):
        return self._rank_detail

    @rank_detail.setter
    def rank_detail(self, value):
        self._rank_detail = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.member_name:
            if hasattr(self.member_name, 'to_alipay_dict'):
                params['member_name'] = self.member_name.to_alipay_dict()
            else:
                params['member_name'] = self.member_name
        if self.out_member_id:
            if hasattr(self.out_member_id, 'to_alipay_dict'):
                params['out_member_id'] = self.out_member_id.to_alipay_dict()
            else:
                params['out_member_id'] = self.out_member_id
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.rank_detail:
            if hasattr(self.rank_detail, 'to_alipay_dict'):
                params['rank_detail'] = self.rank_detail.to_alipay_dict()
            else:
                params['rank_detail'] = self.rank_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RankMemberInfo()
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'member_name' in d:
            o.member_name = d['member_name']
        if 'out_member_id' in d:
            o.out_member_id = d['out_member_id']
        if 'rank' in d:
            o.rank = d['rank']
        if 'rank_detail' in d:
            o.rank_detail = d['rank_detail']
        return o


