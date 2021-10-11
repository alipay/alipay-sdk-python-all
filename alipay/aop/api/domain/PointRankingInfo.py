#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RankingDetailInfo import RankingDetailInfo


class PointRankingInfo(object):

    def __init__(self):
        self._current_ranking = None
        self._ranking_list = None
        self._total = None

    @property
    def current_ranking(self):
        return self._current_ranking

    @current_ranking.setter
    def current_ranking(self, value):
        self._current_ranking = value
    @property
    def ranking_list(self):
        return self._ranking_list

    @ranking_list.setter
    def ranking_list(self, value):
        if isinstance(value, list):
            self._ranking_list = list()
            for i in value:
                if isinstance(i, RankingDetailInfo):
                    self._ranking_list.append(i)
                else:
                    self._ranking_list.append(RankingDetailInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_ranking:
            if hasattr(self.current_ranking, 'to_alipay_dict'):
                params['current_ranking'] = self.current_ranking.to_alipay_dict()
            else:
                params['current_ranking'] = self.current_ranking
        if self.ranking_list:
            if isinstance(self.ranking_list, list):
                for i in range(0, len(self.ranking_list)):
                    element = self.ranking_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ranking_list[i] = element.to_alipay_dict()
            if hasattr(self.ranking_list, 'to_alipay_dict'):
                params['ranking_list'] = self.ranking_list.to_alipay_dict()
            else:
                params['ranking_list'] = self.ranking_list
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PointRankingInfo()
        if 'current_ranking' in d:
            o.current_ranking = d['current_ranking']
        if 'ranking_list' in d:
            o.ranking_list = d['ranking_list']
        if 'total' in d:
            o.total = d['total']
        return o


