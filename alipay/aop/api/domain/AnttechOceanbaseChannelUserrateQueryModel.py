#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChannelUserRateQueryRequest import ChannelUserRateQueryRequest


class AnttechOceanbaseChannelUserrateQueryModel(object):

    def __init__(self):
        self._channel_user_rate_query_request = None

    @property
    def channel_user_rate_query_request(self):
        return self._channel_user_rate_query_request

    @channel_user_rate_query_request.setter
    def channel_user_rate_query_request(self, value):
        if isinstance(value, ChannelUserRateQueryRequest):
            self._channel_user_rate_query_request = value
        else:
            self._channel_user_rate_query_request = ChannelUserRateQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.channel_user_rate_query_request:
            if hasattr(self.channel_user_rate_query_request, 'to_alipay_dict'):
                params['channel_user_rate_query_request'] = self.channel_user_rate_query_request.to_alipay_dict()
            else:
                params['channel_user_rate_query_request'] = self.channel_user_rate_query_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseChannelUserrateQueryModel()
        if 'channel_user_rate_query_request' in d:
            o.channel_user_rate_query_request = d['channel_user_rate_query_request']
        return o


