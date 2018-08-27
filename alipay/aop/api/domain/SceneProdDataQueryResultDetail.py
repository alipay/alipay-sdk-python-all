#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneProdDataQueryResultDetail(object):

    def __init__(self):
        self._app_seqno = None
        self._result = None

    @property
    def app_seqno(self):
        return self._app_seqno

    @app_seqno.setter
    def app_seqno(self, value):
        self._app_seqno = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_seqno:
            if hasattr(self.app_seqno, 'to_alipay_dict'):
                params['app_seqno'] = self.app_seqno.to_alipay_dict()
            else:
                params['app_seqno'] = self.app_seqno
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneProdDataQueryResultDetail()
        if 'app_seqno' in d:
            o.app_seqno = d['app_seqno']
        if 'result' in d:
            o.result = d['result']
        return o


