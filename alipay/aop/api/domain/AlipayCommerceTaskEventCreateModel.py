#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTaskEventCreateModel(object):

    def __init__(self):
        self._event_list = None
        self._out_biz_no = None
        self._template_id = None

    @property
    def event_list(self):
        return self._event_list

    @event_list.setter
    def event_list(self, value):
        if isinstance(value, list):
            self._event_list = list()
            for i in value:
                self._event_list.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_list:
            if isinstance(self.event_list, list):
                for i in range(0, len(self.event_list)):
                    element = self.event_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.event_list[i] = element.to_alipay_dict()
            if hasattr(self.event_list, 'to_alipay_dict'):
                params['event_list'] = self.event_list.to_alipay_dict()
            else:
                params['event_list'] = self.event_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTaskEventCreateModel()
        if 'event_list' in d:
            o.event_list = d['event_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


