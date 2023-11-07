#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObArtifacOnlineVersionQueryResponse import ObArtifacOnlineVersionQueryResponse
from alipay.aop.api.domain.ObArtifacOnlineVersionQueryResponse import ObArtifacOnlineVersionQueryResponse


class ApplicableVersionDTO(object):

    def __init__(self):
        self._other_online_versions = None
        self._standard_online_versions = None

    @property
    def other_online_versions(self):
        return self._other_online_versions

    @other_online_versions.setter
    def other_online_versions(self, value):
        if isinstance(value, list):
            self._other_online_versions = list()
            for i in value:
                if isinstance(i, ObArtifacOnlineVersionQueryResponse):
                    self._other_online_versions.append(i)
                else:
                    self._other_online_versions.append(ObArtifacOnlineVersionQueryResponse.from_alipay_dict(i))
    @property
    def standard_online_versions(self):
        return self._standard_online_versions

    @standard_online_versions.setter
    def standard_online_versions(self, value):
        if isinstance(value, list):
            self._standard_online_versions = list()
            for i in value:
                if isinstance(i, ObArtifacOnlineVersionQueryResponse):
                    self._standard_online_versions.append(i)
                else:
                    self._standard_online_versions.append(ObArtifacOnlineVersionQueryResponse.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.other_online_versions:
            if isinstance(self.other_online_versions, list):
                for i in range(0, len(self.other_online_versions)):
                    element = self.other_online_versions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_online_versions[i] = element.to_alipay_dict()
            if hasattr(self.other_online_versions, 'to_alipay_dict'):
                params['other_online_versions'] = self.other_online_versions.to_alipay_dict()
            else:
                params['other_online_versions'] = self.other_online_versions
        if self.standard_online_versions:
            if isinstance(self.standard_online_versions, list):
                for i in range(0, len(self.standard_online_versions)):
                    element = self.standard_online_versions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.standard_online_versions[i] = element.to_alipay_dict()
            if hasattr(self.standard_online_versions, 'to_alipay_dict'):
                params['standard_online_versions'] = self.standard_online_versions.to_alipay_dict()
            else:
                params['standard_online_versions'] = self.standard_online_versions
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplicableVersionDTO()
        if 'other_online_versions' in d:
            o.other_online_versions = d['other_online_versions']
        if 'standard_online_versions' in d:
            o.standard_online_versions = d['standard_online_versions']
        return o


