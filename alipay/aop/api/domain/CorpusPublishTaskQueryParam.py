#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorpusPublishTaskQueryParam(object):

    def __init__(self):
        self._corpus_type = None
        self._publish_type = None
        self._status = None

    @property
    def corpus_type(self):
        return self._corpus_type

    @corpus_type.setter
    def corpus_type(self, value):
        self._corpus_type = value
    @property
    def publish_type(self):
        return self._publish_type

    @publish_type.setter
    def publish_type(self, value):
        self._publish_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.corpus_type:
            if hasattr(self.corpus_type, 'to_alipay_dict'):
                params['corpus_type'] = self.corpus_type.to_alipay_dict()
            else:
                params['corpus_type'] = self.corpus_type
        if self.publish_type:
            if hasattr(self.publish_type, 'to_alipay_dict'):
                params['publish_type'] = self.publish_type.to_alipay_dict()
            else:
                params['publish_type'] = self.publish_type
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
        o = CorpusPublishTaskQueryParam()
        if 'corpus_type' in d:
            o.corpus_type = d['corpus_type']
        if 'publish_type' in d:
            o.publish_type = d['publish_type']
        if 'status' in d:
            o.status = d['status']
        return o


