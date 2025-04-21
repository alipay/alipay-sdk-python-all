#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryObArtifactListRequest import QueryObArtifactListRequest


class AnttechOceanbaseObglobalArtifactlistQueryModel(object):

    def __init__(self):
        self._query_ob_artifact_list_request = None

    @property
    def query_ob_artifact_list_request(self):
        return self._query_ob_artifact_list_request

    @query_ob_artifact_list_request.setter
    def query_ob_artifact_list_request(self, value):
        if isinstance(value, QueryObArtifactListRequest):
            self._query_ob_artifact_list_request = value
        else:
            self._query_ob_artifact_list_request = QueryObArtifactListRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.query_ob_artifact_list_request:
            if hasattr(self.query_ob_artifact_list_request, 'to_alipay_dict'):
                params['query_ob_artifact_list_request'] = self.query_ob_artifact_list_request.to_alipay_dict()
            else:
                params['query_ob_artifact_list_request'] = self.query_ob_artifact_list_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalArtifactlistQueryModel()
        if 'query_ob_artifact_list_request' in d:
            o.query_ob_artifact_list_request = d['query_ob_artifact_list_request']
        return o


