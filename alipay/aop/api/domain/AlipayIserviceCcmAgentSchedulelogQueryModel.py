#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmAgentSchedulelogQueryModel(object):

    def __init__(self):
        self._agent_ids = None
        self._ccs_instance_id = None
        self._end_time = None
        self._limit = None
        self._page_num = None
        self._page_size = None
        self._start_id = None
        self._start_time = None

    @property
    def agent_ids(self):
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, value):
        if isinstance(value, list):
            self._agent_ids = list()
            for i in value:
                self._agent_ids.append(i)
    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def start_id(self):
        return self._start_id

    @start_id.setter
    def start_id(self, value):
        self._start_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_ids:
            if isinstance(self.agent_ids, list):
                for i in range(0, len(self.agent_ids)):
                    element = self.agent_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agent_ids[i] = element.to_alipay_dict()
            if hasattr(self.agent_ids, 'to_alipay_dict'):
                params['agent_ids'] = self.agent_ids.to_alipay_dict()
            else:
                params['agent_ids'] = self.agent_ids
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.limit:
            if hasattr(self.limit, 'to_alipay_dict'):
                params['limit'] = self.limit.to_alipay_dict()
            else:
                params['limit'] = self.limit
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.start_id:
            if hasattr(self.start_id, 'to_alipay_dict'):
                params['start_id'] = self.start_id.to_alipay_dict()
            else:
                params['start_id'] = self.start_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmAgentSchedulelogQueryModel()
        if 'agent_ids' in d:
            o.agent_ids = d['agent_ids']
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'limit' in d:
            o.limit = d['limit']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_id' in d:
            o.start_id = d['start_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


