#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FlowStatsEntry(object):

    def __init__(self):
        self._count = None
        self._rank = None
        self._source_ip = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def source_ip(self):
        return self._source_ip

    @source_ip.setter
    def source_ip(self, value):
        self._source_ip = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.source_ip:
            if hasattr(self.source_ip, 'to_alipay_dict'):
                params['source_ip'] = self.source_ip.to_alipay_dict()
            else:
                params['source_ip'] = self.source_ip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FlowStatsEntry()
        if 'count' in d:
            o.count = d['count']
        if 'rank' in d:
            o.rank = d['rank']
        if 'source_ip' in d:
            o.source_ip = d['source_ip']
        return o


