#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoteDataModel import PromoteDataModel
from alipay.aop.api.domain.PromoteDataModel import PromoteDataModel


class PromoteDetailChannelModel(object):

    def __init__(self):
        self._channel_id = None
        self._channel_name = None
        self._part_promote_data = None
        self._total_promote_data = None

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value
    @property
    def part_promote_data(self):
        return self._part_promote_data

    @part_promote_data.setter
    def part_promote_data(self, value):
        if isinstance(value, PromoteDataModel):
            self._part_promote_data = value
        else:
            self._part_promote_data = PromoteDataModel.from_alipay_dict(value)
    @property
    def total_promote_data(self):
        return self._total_promote_data

    @total_promote_data.setter
    def total_promote_data(self, value):
        if isinstance(value, PromoteDataModel):
            self._total_promote_data = value
        else:
            self._total_promote_data = PromoteDataModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.channel_name:
            if hasattr(self.channel_name, 'to_alipay_dict'):
                params['channel_name'] = self.channel_name.to_alipay_dict()
            else:
                params['channel_name'] = self.channel_name
        if self.part_promote_data:
            if hasattr(self.part_promote_data, 'to_alipay_dict'):
                params['part_promote_data'] = self.part_promote_data.to_alipay_dict()
            else:
                params['part_promote_data'] = self.part_promote_data
        if self.total_promote_data:
            if hasattr(self.total_promote_data, 'to_alipay_dict'):
                params['total_promote_data'] = self.total_promote_data.to_alipay_dict()
            else:
                params['total_promote_data'] = self.total_promote_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoteDetailChannelModel()
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'channel_name' in d:
            o.channel_name = d['channel_name']
        if 'part_promote_data' in d:
            o.part_promote_data = d['part_promote_data']
        if 'total_promote_data' in d:
            o.total_promote_data = d['total_promote_data']
        return o


