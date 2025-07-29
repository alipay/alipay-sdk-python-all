#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WorkPlace import WorkPlace


class AlipayCommerceLogisticsPointWorkCreateModel(object):

    def __init__(self):
        self._expire_time = None
        self._work_biz_no = None
        self._work_place_list = None
        self._work_point_id = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def work_biz_no(self):
        return self._work_biz_no

    @work_biz_no.setter
    def work_biz_no(self, value):
        self._work_biz_no = value
    @property
    def work_place_list(self):
        return self._work_place_list

    @work_place_list.setter
    def work_place_list(self, value):
        if isinstance(value, list):
            self._work_place_list = list()
            for i in value:
                if isinstance(i, WorkPlace):
                    self._work_place_list.append(i)
                else:
                    self._work_place_list.append(WorkPlace.from_alipay_dict(i))
    @property
    def work_point_id(self):
        return self._work_point_id

    @work_point_id.setter
    def work_point_id(self, value):
        self._work_point_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.work_biz_no:
            if hasattr(self.work_biz_no, 'to_alipay_dict'):
                params['work_biz_no'] = self.work_biz_no.to_alipay_dict()
            else:
                params['work_biz_no'] = self.work_biz_no
        if self.work_place_list:
            if isinstance(self.work_place_list, list):
                for i in range(0, len(self.work_place_list)):
                    element = self.work_place_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_place_list[i] = element.to_alipay_dict()
            if hasattr(self.work_place_list, 'to_alipay_dict'):
                params['work_place_list'] = self.work_place_list.to_alipay_dict()
            else:
                params['work_place_list'] = self.work_place_list
        if self.work_point_id:
            if hasattr(self.work_point_id, 'to_alipay_dict'):
                params['work_point_id'] = self.work_point_id.to_alipay_dict()
            else:
                params['work_point_id'] = self.work_point_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsPointWorkCreateModel()
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'work_biz_no' in d:
            o.work_biz_no = d['work_biz_no']
        if 'work_place_list' in d:
            o.work_place_list = d['work_place_list']
        if 'work_point_id' in d:
            o.work_point_id = d['work_point_id']
        return o


