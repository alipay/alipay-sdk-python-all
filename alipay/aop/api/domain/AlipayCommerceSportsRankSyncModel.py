#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RankMemberInfo import RankMemberInfo


class AlipayCommerceSportsRankSyncModel(object):

    def __init__(self):
        self._out_ranking_id = None
        self._rank_members = None
        self._ranking_name = None

    @property
    def out_ranking_id(self):
        return self._out_ranking_id

    @out_ranking_id.setter
    def out_ranking_id(self, value):
        self._out_ranking_id = value
    @property
    def rank_members(self):
        return self._rank_members

    @rank_members.setter
    def rank_members(self, value):
        if isinstance(value, list):
            self._rank_members = list()
            for i in value:
                if isinstance(i, RankMemberInfo):
                    self._rank_members.append(i)
                else:
                    self._rank_members.append(RankMemberInfo.from_alipay_dict(i))
    @property
    def ranking_name(self):
        return self._ranking_name

    @ranking_name.setter
    def ranking_name(self, value):
        self._ranking_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_ranking_id:
            if hasattr(self.out_ranking_id, 'to_alipay_dict'):
                params['out_ranking_id'] = self.out_ranking_id.to_alipay_dict()
            else:
                params['out_ranking_id'] = self.out_ranking_id
        if self.rank_members:
            if isinstance(self.rank_members, list):
                for i in range(0, len(self.rank_members)):
                    element = self.rank_members[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rank_members[i] = element.to_alipay_dict()
            if hasattr(self.rank_members, 'to_alipay_dict'):
                params['rank_members'] = self.rank_members.to_alipay_dict()
            else:
                params['rank_members'] = self.rank_members
        if self.ranking_name:
            if hasattr(self.ranking_name, 'to_alipay_dict'):
                params['ranking_name'] = self.ranking_name.to_alipay_dict()
            else:
                params['ranking_name'] = self.ranking_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsRankSyncModel()
        if 'out_ranking_id' in d:
            o.out_ranking_id = d['out_ranking_id']
        if 'rank_members' in d:
            o.rank_members = d['rank_members']
        if 'ranking_name' in d:
            o.ranking_name = d['ranking_name']
        return o


