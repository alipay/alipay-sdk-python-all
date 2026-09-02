#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SourceUidPidQueryRequest import SourceUidPidQueryRequest


class AnttechOceanbaseSourceuidPidQueryModel(object):

    def __init__(self):
        self._source_uid_pid_query_request = None

    @property
    def source_uid_pid_query_request(self):
        return self._source_uid_pid_query_request

    @source_uid_pid_query_request.setter
    def source_uid_pid_query_request(self, value):
        if isinstance(value, SourceUidPidQueryRequest):
            self._source_uid_pid_query_request = value
        else:
            self._source_uid_pid_query_request = SourceUidPidQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.source_uid_pid_query_request:
            if hasattr(self.source_uid_pid_query_request, 'to_alipay_dict'):
                params['source_uid_pid_query_request'] = self.source_uid_pid_query_request.to_alipay_dict()
            else:
                params['source_uid_pid_query_request'] = self.source_uid_pid_query_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseSourceuidPidQueryModel()
        if 'source_uid_pid_query_request' in d:
            o.source_uid_pid_query_request = d['source_uid_pid_query_request']
        return o


