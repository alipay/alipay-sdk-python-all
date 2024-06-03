#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenGoodsCheckDetail import OpenGoodsCheckDetail


class OpenContentGoodsCheckResult(object):

    def __init__(self):
        self._sub_detail_list = None
        self._summary_result = None

    @property
    def sub_detail_list(self):
        return self._sub_detail_list

    @sub_detail_list.setter
    def sub_detail_list(self, value):
        if isinstance(value, list):
            self._sub_detail_list = list()
            for i in value:
                if isinstance(i, OpenGoodsCheckDetail):
                    self._sub_detail_list.append(i)
                else:
                    self._sub_detail_list.append(OpenGoodsCheckDetail.from_alipay_dict(i))
    @property
    def summary_result(self):
        return self._summary_result

    @summary_result.setter
    def summary_result(self, value):
        self._summary_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_detail_list:
            if isinstance(self.sub_detail_list, list):
                for i in range(0, len(self.sub_detail_list)):
                    element = self.sub_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_detail_list, 'to_alipay_dict'):
                params['sub_detail_list'] = self.sub_detail_list.to_alipay_dict()
            else:
                params['sub_detail_list'] = self.sub_detail_list
        if self.summary_result:
            if hasattr(self.summary_result, 'to_alipay_dict'):
                params['summary_result'] = self.summary_result.to_alipay_dict()
            else:
                params['summary_result'] = self.summary_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenContentGoodsCheckResult()
        if 'sub_detail_list' in d:
            o.sub_detail_list = d['sub_detail_list']
        if 'summary_result' in d:
            o.summary_result = d['summary_result']
        return o


