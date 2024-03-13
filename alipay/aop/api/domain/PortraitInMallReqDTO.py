#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PortraitInMallReqDTO(object):

    def __init__(self):
        self._live_user_tag = None
        self._settled_user_tag = None
        self._work_user_tag = None

    @property
    def live_user_tag(self):
        return self._live_user_tag

    @live_user_tag.setter
    def live_user_tag(self, value):
        if isinstance(value, list):
            self._live_user_tag = list()
            for i in value:
                self._live_user_tag.append(i)
    @property
    def settled_user_tag(self):
        return self._settled_user_tag

    @settled_user_tag.setter
    def settled_user_tag(self, value):
        if isinstance(value, list):
            self._settled_user_tag = list()
            for i in value:
                self._settled_user_tag.append(i)
    @property
    def work_user_tag(self):
        return self._work_user_tag

    @work_user_tag.setter
    def work_user_tag(self, value):
        if isinstance(value, list):
            self._work_user_tag = list()
            for i in value:
                self._work_user_tag.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.live_user_tag:
            if isinstance(self.live_user_tag, list):
                for i in range(0, len(self.live_user_tag)):
                    element = self.live_user_tag[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.live_user_tag[i] = element.to_alipay_dict()
            if hasattr(self.live_user_tag, 'to_alipay_dict'):
                params['live_user_tag'] = self.live_user_tag.to_alipay_dict()
            else:
                params['live_user_tag'] = self.live_user_tag
        if self.settled_user_tag:
            if isinstance(self.settled_user_tag, list):
                for i in range(0, len(self.settled_user_tag)):
                    element = self.settled_user_tag[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settled_user_tag[i] = element.to_alipay_dict()
            if hasattr(self.settled_user_tag, 'to_alipay_dict'):
                params['settled_user_tag'] = self.settled_user_tag.to_alipay_dict()
            else:
                params['settled_user_tag'] = self.settled_user_tag
        if self.work_user_tag:
            if isinstance(self.work_user_tag, list):
                for i in range(0, len(self.work_user_tag)):
                    element = self.work_user_tag[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_user_tag[i] = element.to_alipay_dict()
            if hasattr(self.work_user_tag, 'to_alipay_dict'):
                params['work_user_tag'] = self.work_user_tag.to_alipay_dict()
            else:
                params['work_user_tag'] = self.work_user_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortraitInMallReqDTO()
        if 'live_user_tag' in d:
            o.live_user_tag = d['live_user_tag']
        if 'settled_user_tag' in d:
            o.settled_user_tag = d['settled_user_tag']
        if 'work_user_tag' in d:
            o.work_user_tag = d['work_user_tag']
        return o


