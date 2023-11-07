#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObArtifactVersionQueryRequest import ObArtifactVersionQueryRequest


class AnttechOceanbaseObglobalApplicableversionQueryModel(object):

    def __init__(self):
        self._query_applicable_version_request = None

    @property
    def query_applicable_version_request(self):
        return self._query_applicable_version_request

    @query_applicable_version_request.setter
    def query_applicable_version_request(self, value):
        if isinstance(value, ObArtifactVersionQueryRequest):
            self._query_applicable_version_request = value
        else:
            self._query_applicable_version_request = ObArtifactVersionQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.query_applicable_version_request:
            if hasattr(self.query_applicable_version_request, 'to_alipay_dict'):
                params['query_applicable_version_request'] = self.query_applicable_version_request.to_alipay_dict()
            else:
                params['query_applicable_version_request'] = self.query_applicable_version_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalApplicableversionQueryModel()
        if 'query_applicable_version_request' in d:
            o.query_applicable_version_request = d['query_applicable_version_request']
        return o


