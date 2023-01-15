#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdSelectTagOpenRequest import CrowdSelectTagOpenRequest


class AlipayMarketingQipanCrowdwithtagQueryModel(object):

    def __init__(self):
        self._crowd_id = None
        self._select_tag_list = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def select_tag_list(self):
        return self._select_tag_list

    @select_tag_list.setter
    def select_tag_list(self, value):
        if isinstance(value, list):
            self._select_tag_list = list()
            for i in value:
                if isinstance(i, CrowdSelectTagOpenRequest):
                    self._select_tag_list.append(i)
                else:
                    self._select_tag_list.append(CrowdSelectTagOpenRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.select_tag_list:
            if isinstance(self.select_tag_list, list):
                for i in range(0, len(self.select_tag_list)):
                    element = self.select_tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.select_tag_list[i] = element.to_alipay_dict()
            if hasattr(self.select_tag_list, 'to_alipay_dict'):
                params['select_tag_list'] = self.select_tag_list.to_alipay_dict()
            else:
                params['select_tag_list'] = self.select_tag_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingQipanCrowdwithtagQueryModel()
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'select_tag_list' in d:
            o.select_tag_list = d['select_tag_list']
        return o


