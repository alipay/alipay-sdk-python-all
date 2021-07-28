#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignPrizepoolPrizeDeleteModel(object):

    def __init__(self):
        self._out_biz_id = None
        self._pool_id = None
        self._prize_id = None
        self._source = None
        self._status = None

    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def pool_id(self):
        return self._pool_id

    @pool_id.setter
    def pool_id(self, value):
        self._pool_id = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.pool_id:
            if hasattr(self.pool_id, 'to_alipay_dict'):
                params['pool_id'] = self.pool_id.to_alipay_dict()
            else:
                params['pool_id'] = self.pool_id
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignPrizepoolPrizeDeleteModel()
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'pool_id' in d:
            o.pool_id = d['pool_id']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        return o


