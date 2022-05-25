#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiDailyScheduleVO import OpenApiDailyScheduleVO


class OpenApiUserScheduleVO(object):

    def __init__(self):
        self._over_limit = None
        self._schedule_content = None
        self._schedule_id = None

    @property
    def over_limit(self):
        return self._over_limit

    @over_limit.setter
    def over_limit(self, value):
        self._over_limit = value
    @property
    def schedule_content(self):
        return self._schedule_content

    @schedule_content.setter
    def schedule_content(self, value):
        if isinstance(value, list):
            self._schedule_content = list()
            for i in value:
                if isinstance(i, OpenApiDailyScheduleVO):
                    self._schedule_content.append(i)
                else:
                    self._schedule_content.append(OpenApiDailyScheduleVO.from_alipay_dict(i))
    @property
    def schedule_id(self):
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, value):
        self._schedule_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.over_limit:
            if hasattr(self.over_limit, 'to_alipay_dict'):
                params['over_limit'] = self.over_limit.to_alipay_dict()
            else:
                params['over_limit'] = self.over_limit
        if self.schedule_content:
            if isinstance(self.schedule_content, list):
                for i in range(0, len(self.schedule_content)):
                    element = self.schedule_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.schedule_content[i] = element.to_alipay_dict()
            if hasattr(self.schedule_content, 'to_alipay_dict'):
                params['schedule_content'] = self.schedule_content.to_alipay_dict()
            else:
                params['schedule_content'] = self.schedule_content
        if self.schedule_id:
            if hasattr(self.schedule_id, 'to_alipay_dict'):
                params['schedule_id'] = self.schedule_id.to_alipay_dict()
            else:
                params['schedule_id'] = self.schedule_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiUserScheduleVO()
        if 'over_limit' in d:
            o.over_limit = d['over_limit']
        if 'schedule_content' in d:
            o.schedule_content = d['schedule_content']
        if 'schedule_id' in d:
            o.schedule_id = d['schedule_id']
        return o


