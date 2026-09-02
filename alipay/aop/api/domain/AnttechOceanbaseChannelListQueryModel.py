#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChannelListQueryRequest import ChannelListQueryRequest


class AnttechOceanbaseChannelListQueryModel(object):

    def __init__(self):
        self._channel_list_query_request = None

    @property
    def channel_list_query_request(self):
        return self._channel_list_query_request

    @channel_list_query_request.setter
    def channel_list_query_request(self, value):
        if isinstance(value, ChannelListQueryRequest):
            self._channel_list_query_request = value
        else:
            self._channel_list_query_request = ChannelListQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.channel_list_query_request:
            if hasattr(self.channel_list_query_request, 'to_alipay_dict'):
                params['channel_list_query_request'] = self.channel_list_query_request.to_alipay_dict()
            else:
                params['channel_list_query_request'] = self.channel_list_query_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseChannelListQueryModel()
        if 'channel_list_query_request' in d:
            o.channel_list_query_request = d['channel_list_query_request']
        return o


