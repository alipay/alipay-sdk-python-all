#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchScoreInfoBO(object):

    def __init__(self):
        self._authority_score = None
        self._quality_score = None
        self._relevance_score = None
        self._timeliness_score = None

    @property
    def authority_score(self):
        return self._authority_score

    @authority_score.setter
    def authority_score(self, value):
        self._authority_score = value
    @property
    def quality_score(self):
        return self._quality_score

    @quality_score.setter
    def quality_score(self, value):
        self._quality_score = value
    @property
    def relevance_score(self):
        return self._relevance_score

    @relevance_score.setter
    def relevance_score(self, value):
        self._relevance_score = value
    @property
    def timeliness_score(self):
        return self._timeliness_score

    @timeliness_score.setter
    def timeliness_score(self, value):
        self._timeliness_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.authority_score:
            if hasattr(self.authority_score, 'to_alipay_dict'):
                params['authority_score'] = self.authority_score.to_alipay_dict()
            else:
                params['authority_score'] = self.authority_score
        if self.quality_score:
            if hasattr(self.quality_score, 'to_alipay_dict'):
                params['quality_score'] = self.quality_score.to_alipay_dict()
            else:
                params['quality_score'] = self.quality_score
        if self.relevance_score:
            if hasattr(self.relevance_score, 'to_alipay_dict'):
                params['relevance_score'] = self.relevance_score.to_alipay_dict()
            else:
                params['relevance_score'] = self.relevance_score
        if self.timeliness_score:
            if hasattr(self.timeliness_score, 'to_alipay_dict'):
                params['timeliness_score'] = self.timeliness_score.to_alipay_dict()
            else:
                params['timeliness_score'] = self.timeliness_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchScoreInfoBO()
        if 'authority_score' in d:
            o.authority_score = d['authority_score']
        if 'quality_score' in d:
            o.quality_score = d['quality_score']
        if 'relevance_score' in d:
            o.relevance_score = d['relevance_score']
        if 'timeliness_score' in d:
            o.timeliness_score = d['timeliness_score']
        return o


