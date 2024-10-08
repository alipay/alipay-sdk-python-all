#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupActivityRecordVO(object):

    def __init__(self):
        self._biz_type = None
        self._client_position = None
        self._gmt_end = None
        self._gmt_start = None
        self._group_activity_id = None
        self._group_cnt = None
        self._group_ids = None
        self._priority = None
        self._status = None
        self._title = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def client_position(self):
        return self._client_position

    @client_position.setter
    def client_position(self, value):
        self._client_position = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def group_activity_id(self):
        return self._group_activity_id

    @group_activity_id.setter
    def group_activity_id(self, value):
        self._group_activity_id = value
    @property
    def group_cnt(self):
        return self._group_cnt

    @group_cnt.setter
    def group_cnt(self, value):
        self._group_cnt = value
    @property
    def group_ids(self):
        return self._group_ids

    @group_ids.setter
    def group_ids(self, value):
        if isinstance(value, list):
            self._group_ids = list()
            for i in value:
                self._group_ids.append(i)
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.client_position:
            if hasattr(self.client_position, 'to_alipay_dict'):
                params['client_position'] = self.client_position.to_alipay_dict()
            else:
                params['client_position'] = self.client_position
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.group_activity_id:
            if hasattr(self.group_activity_id, 'to_alipay_dict'):
                params['group_activity_id'] = self.group_activity_id.to_alipay_dict()
            else:
                params['group_activity_id'] = self.group_activity_id
        if self.group_cnt:
            if hasattr(self.group_cnt, 'to_alipay_dict'):
                params['group_cnt'] = self.group_cnt.to_alipay_dict()
            else:
                params['group_cnt'] = self.group_cnt
        if self.group_ids:
            if isinstance(self.group_ids, list):
                for i in range(0, len(self.group_ids)):
                    element = self.group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_ids[i] = element.to_alipay_dict()
            if hasattr(self.group_ids, 'to_alipay_dict'):
                params['group_ids'] = self.group_ids.to_alipay_dict()
            else:
                params['group_ids'] = self.group_ids
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupActivityRecordVO()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'client_position' in d:
            o.client_position = d['client_position']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'group_activity_id' in d:
            o.group_activity_id = d['group_activity_id']
        if 'group_cnt' in d:
            o.group_cnt = d['group_cnt']
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        if 'priority' in d:
            o.priority = d['priority']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        return o


