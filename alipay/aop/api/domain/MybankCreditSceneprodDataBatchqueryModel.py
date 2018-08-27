#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneProdDataQueryParam import SceneProdDataQueryParam


class MybankCreditSceneprodDataBatchqueryModel(object):

    def __init__(self):
        self._app_seqno_list = None

    @property
    def app_seqno_list(self):
        return self._app_seqno_list

    @app_seqno_list.setter
    def app_seqno_list(self, value):
        if isinstance(value, list):
            self._app_seqno_list = list()
            for i in value:
                if isinstance(i, SceneProdDataQueryParam):
                    self._app_seqno_list.append(i)
                else:
                    self._app_seqno_list.append(SceneProdDataQueryParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.app_seqno_list:
            if isinstance(self.app_seqno_list, list):
                for i in range(0, len(self.app_seqno_list)):
                    element = self.app_seqno_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_seqno_list[i] = element.to_alipay_dict()
            if hasattr(self.app_seqno_list, 'to_alipay_dict'):
                params['app_seqno_list'] = self.app_seqno_list.to_alipay_dict()
            else:
                params['app_seqno_list'] = self.app_seqno_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodDataBatchqueryModel()
        if 'app_seqno_list' in d:
            o.app_seqno_list = d['app_seqno_list']
        return o


